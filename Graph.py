import json
from datetime import datetime

class Graph:
    def __init__(self):
        self.list = {}  # Lista de adyacencia
        self.size = 0   # Número de nodos
        self.nodes = []  # Lista de nodos
        self.load_from_json("BooksData.json")

    def add_vertex(self, v):
        if v in self.list:
            print(f"El nodo {v} ya existe")
            return
        else:
            self.list[v] = []
            self.size = len(self.list)

    def add_edge(self, v1, v2, weight):
        if not v1 in self.list:
            self.add_vertex(v1)
        if not v2 in self.list:
            self.add_vertex(v2)

        # Verificar si la relación ya existe antes de agregarla
        existing_edges = [neighbor for neighbor, _ in self.list[v1]]
        if v2 in existing_edges:
            print(f"La relación entre {v1} y {v2} ya existe.")
        else:
            self.list[v1].append((v2, weight))

    def load_from_json(self, json_file):
        with open(json_file) as f:
            data = json.load(f)

        # agregando los conceptos (de los que salen las instancias)...
        self.add_vertex("Libro")
        self.add_vertex("Autor")
        self.add_vertex("Fecha Publicacion")
        self.add_vertex("Precio")
        self.add_vertex("Calificacion")
        self.add_vertex("Genero")
        
        for book, attributes in data.items():
            
            self.add_vertex(book) # Nodo para el libro
            self.add_edge(book, "Libro", 11) # relación con el concepto libro
            
            for attribute, value in attributes.items():
                
                if attribute =="Autor":
                    self.add_vertex(value)  # Nodos pal autor
                    self.add_edge(book, value, 1) 
                    self.add_edge(value, book, 2) 
                    # la relación que indica que es 
                    self.add_edge(value, "Autor", 11) 
                
                if attribute =="Fecha Publicacion":
                    self.add_vertex(value)  # Nodo pa la fecha 
                    self.add_edge(book, value, 3) 
                    self.add_edge(value, book, 4) 
                    # la relación que indica que es 
                    self.add_edge(value, "Fecha Publicacion", 11) 
                    
                if attribute == "Precio":
                    self.add_vertex(value)  # Nodo pal precio 
                    self.add_edge(book, value, 5) 
                    self.add_edge(value, book, 6) 
                    # la relación que indica que es 
                    self.add_edge(value, "Precio", 11) 
                    
                if attribute == "Calificacion":
                    self.add_vertex(value)  # Nodo pal score o rate idk
                    self.add_edge(book, value, 7) 
                    self.add_edge(value, book, 8)  
                    # la relación que indica que es 
                    self.add_edge(value, "Calificacion", 11) 
                
                if attribute == "Generos":
                    for genre in value:
                        self.add_vertex(genre)  # Nodo pal género
                        self.add_edge(book, genre, 9)  
                        self.add_edge(genre, book, 10) 
                        # la relación que indica que es 
                        self.add_edge(genre, "Genero", 11) 
                
    def print_graph(self):
        for node, edges in self.list.items():
            print(f"{node}: {edges}")
    
    def printGrafoFacherito(self):
        for node, edges in self.list.items():
            edge_str = ", ".join(f"{neighbor} ({weight})" for neighbor, weight in edges)
            print(f"{node} -> {edge_str}")

    # Según entiendo, la idea es que usar la lista de adyacencia para obtener un nodo de interés, 
    # y a partir de es nodo obtener información apartir de las relaciones...
    
    # este método me podría servir para simplificar algo...
    def isRelated(self, v1, v2, weight):
        for node, relation in self.list[v1]:
            if node == v2 and relation == weight:
                return True
        return False
    
    def getNodesByWeight(self, v, weight):
        
        nodes = []
        for node, relation in self.list[v]:
            if relation == weight:
                nodes.append(node)
        if len(nodes) <= 1:
            return nodes[0]
        
        return nodes
    

# Ejemplo de uso
#grafo = Graph()
#grafo.load_from_json("BooksData.json")
#grafo.printGrafoFacherito()

"""print (grafo.isRelated('New Moon', 'Stephenie Meyer', 1))
print (grafo.isRelated('New Moon', 'The Foundation Trilogy', 2)) 

books = grafo.FifthFunction(["Fiction"], 14.99)
"""

#pruebita
#fecha = grafo.getNodesByWeight("The Foundation Trilogy", 3)

#print(isinstance(fecha, datetime))
