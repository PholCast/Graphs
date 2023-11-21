from Graph import Graph
from datetime import datetime

class Services:
    def __init__(self, graph):
        
        self.graph = graph
        self.graph.load_from_json("BooksData.json")
    
    def getBooksByAuthor(self, author): #Listar los libros del autor X ordenados por fecha de lanzamiento.
        
        if not self.graph.isRelated(author, "Autor", 11):
            print(" El autor no existe ....")
            return None
        
        books = []
        
        relations = self.graph.list[author] 
        for relation in relations:
            if relation[1] == 2:
                books.append(relation[0])
        
        nonvalidBooks = []
        valid_books = []
        
        for book in books:
            fecha = self.graph.getNodesByWeight(book, 3) 
            try:
                datetime.strptime(fecha, "%d/%m/%Y")
                valid_books.append(book)
            except ValueError:
                nonvalidBooks.append(book)
                
        valid_books = sorted(valid_books, key=lambda x: datetime.strptime(self.graph.getNodesByWeight(x, 3), "%d/%m/%Y")) 
            
        return nonvalidBooks + valid_books 
    
    def RecommendBooksByBook(self, book):#Recomendar N libros del mismo género y de la misma década que el libro X.
        
        originalBook = book
        
        if not self.graph.isRelated(book, "Libro", 11):
            print(" El libro no existe ....")
            return None
        
        books = []
        genres = []
        booksFromGenres = []
        
        relations = self.graph.list[book]
        for relation in relations:
            if relation[1] == 9:
                genres.append(relation[0])
                print(relation[0])
        
        for genre in genres:
            genre_relations = self.graph.list[genre] 
            for relation in genre_relations:
                if relation[1] == 10 and relation[0] not in booksFromGenres:
                    booksFromGenres.append(relation[0]) 
                    print(relation[0])
        
        # Aquí se filtra el tema de la decada...
        # primero ver cual sería la decada del libro dado :
        
        relations = self.graph.list[book]
        for relation in relations:
            if relation[1] == 3:
                targetDate = relation[0]
        
        targetYear = int(targetDate.split("/")[-1])
        # Calcular la década
        targetDecade = (targetYear // 10) * 10
        
        print("el año de publicación del libro es: ", targetDate)
        
        # ahora mirar que libros son de esa misma decada
        for book in booksFromGenres:
            relations = self.graph.list[book]
            for relation in relations:
                if relation[1] == 3:
                    date = relation[0] 
            
            if not date:
                print ("wtf dizque no tiene fecha")
            
            # Extraer el año de la fecha
            año = int(date.split("/")[-1])
            # Calcular la década
            decada = (año // 10) * 10
            
            if decada == targetDecade:
                books.append(book)
                if book != originalBook:
                    print("libro que es de la misma decada :", book, " que se publicó en el :", date)
        
        # que no se le recomiende el mismo libro
        books.remove(originalBook)
        
        return books
    




    #Listar a los autores del género X ordenados por la cantidad de libros escritos en este género.
    
    def GetAuthorsByGenre(self, genre): 
        
        if not self.graph.isRelated(genre, "Genero", 11):
            print("tení que mandarle un genre 😡")
            return None
        
        # se meterá todo en un diccionario pa después ordenarlo 🧐
        authors = {}
        
        books = self.graph.getNodesByWeight(genre, 10)
        
        if books == []:
            print("no hay libros con ese genero ")
            return None
        
        for book in books:
            author = self.graph.getNodesByWeight(book, 1) 
            
            if type(author) == list:
                print("dizque el libro tiene varios autores")
                return None
            
            if author:
                if author not in authors:
                    authors[author] = 1
                else:
                    authors[author] += 1
        
        # Ordenar el diccionario por los valores en orden descendente
        orderedAuthors = dict(sorted(authors.items(), key=lambda x: x[1], reverse=True))

        # Imprimir el diccionario ordenado
        #print(orderedAuthors)
        
        return orderedAuthors
    



    #Recomendar libros de puntaje mayor a X (número entero de 1 a 5) dentro de un grupo de géneros (pueden ser 1 o varios). 
    def RecommendBooksByScore(self, genres, score):
        
        genresbooks = []
        
        for genre in genres:
            
            books = self.graph.getNodesByWeight(genre, 10)
            
            if books == []:
                print(f"no hay libros con el genero {genre}  ")
                return None
            
            for book in books:
            
                # Puntaje como string
                string_score = self.graph.getNodesByWeight(book, 7)
                
                if type(string_score) == list:
                    print("dizque el libro tiene varios puntajes")
                    return None
                
                # Convertir la cadena a un número decimal (punto flotante)
                decimal_score = float(string_score)

                # Verificar si el puntaje decimal es mayor que el número entero
                if decimal_score > score:
                    genresbooks.append(book)
    
        print (genresbooks)
        return genresbooks
    



    #Recomendar lista de compras para obtener el mayor número de 
    # libros con base en X cantidad de dinero y un grupo de géneros (pueden ser 1 o varios).
    def RecommendShoppingList(self, genres, amount):
        
        shoppingList = []
        
        pricedBooks = {}
        
        for genre in genres:
            
            books = self.graph.getNodesByWeight(genre, 10)
            
            if books == []:
                print("no hay libros con ese genero ")
                return None
            
            for book in books:
                if book not in pricedBooks:
                    
                    price = self.graph.getNodesByWeight(book, 5)
                    
                    if type(price) == list:
                        print("dizque el libro tiene varios precios")
                        return None
                    
                    pricedBooks[book] = price
                    
        # Ordenar el diccionario por los valores en orden ascendente
        orderedBooksByPrice = dict(sorted(pricedBooks.items(), key=lambda x: x[1], reverse=False))
        
        currentAmount = 0
        
        for book, price in orderedBooksByPrice.items():
            if currentAmount > amount:
                shoppingList.remove(shoppingList[-1])
                break
            shoppingList.append(book)
            currentAmount += price
        
        print(shoppingList)
        return shoppingList
    
# Ejemplo de uso


# for book in services.RecommendShoppingList(["Fiction", "Fantasy"], 0):
#     print("Se agregó el libro ", book, " con precio ", services.graph.getNodesByWeight(book, 5), " a la lista de compras")
