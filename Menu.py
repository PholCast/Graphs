from Services import Services
from Graph import Graph
import os
class Menu:

    services = None

    graphGenres = ['Classics', 'Fiction', 'Historical Fiction', 'Young Adult', 'Magic', 'Romance', 'Nonfiction', 'Biography', 'Dystopia', 'Fantasy', 'Science Fiction', 'School', 'Plays', 'Childrens', 'Picture Books', 'Middle Grade', 'Horror', 'History', 'Religion', 'Christian', 'Humor', 'Essays', 'Russia', 'Historical', 'Poetry', 'Christmas', 'Magical Realism', 'Literature', 'Contemporary', 'Feminism', 'Adventure', 'Psychology', 'Memoir', 'Philosophy', 'Islam', 'Africa', 'Lds', 'Mystery', 'Thriller', 'Coming Of Age', 'Epic Fantasy', 'Politics', 'Inspirational', 'Spanish Literature', 'European Literature', 'Chick Lit', 'True Crime', 'Short Stories', 'Travel', 'Crime', 'Science', 'Graphic Novels', 'Comics', 'Mythology', 'American History', 'Holocaust', 'Self Help', 'Physics', 'Christian Fiction', 'LGBT', 'France', 'Business', 'Egypt', 'Spirituality', 'Westerns', 'Sociology', 'India', 'Animals']


    @staticmethod
    def initService():
        Menu.services = Services(Graph())

    @staticmethod
    def showMenu():
        Menu.initService()
        while(True):
            print("\n\nMENU:\n")

            print("1.Listar los libros del autor X ordenados por fecha de lanzamiento.")

            print("2.Recomendar N libros del mismo género y de la misma década que el libro X.")

            print("3.Listar a los autores del género X ordenados por la cantidad de libros escritos en este género.")

            print("4.Recomendar libros de puntaje mayor a X (número entero de 1 a 5) dentro de un grupo de géneros (pueden ser 1 o varios).")

            print("5.Recomendar lista de compras para obtener el mayor número de libros con base en X cantidad de dinero y un grupo de géneros (pueden ser 1 o varios).")
            
            print("6.Salir")


            while(True):

                try:
                    option = int(input("Selecciona alguna opcion: "))

                    if 0<option<=6:
                        break
                    print("Error, selecciona una opción valida (1-6).\n")
                except:
                    print("Error, ingresa un número válido.\n")

            match option:
                case 1:
                    author = input("Ingresa el nombre de un autor: ")
                    books = Menu.services.getBooksByAuthor(author)

                    for book in books:
                        print(book)

                case 2:
                    book = input("Ingresa el nombre del libro...  ")
                    books2 = Menu.services.RecommendBooksByBook(book)

                    for book in books2:
                        print(book)
                
                case 3:
                    genre = input("Ingresa el genero...  ")
                    authors = Menu.services.GetAuthorsByGenre(genre)
                    print("")
                    for author, num in authors.items():
                        print(author,": ",num)

                case 4:
                    score = int(input("Ingresa un puntaje: "))
                    genres = []
                    print("cuando finalices presiona x")
                    while(True):
                        auxGenre = input("Ingresa un genero: ")

                        if auxGenre in "xX":
                            break

                        if auxGenre in Menu.graphGenres:
                            genres.append(auxGenre)
                        else:
                            print("Ese genero no existe, ingresa uno valido")

                        
                
                    
                    Menu.services.RecommendBooksByScore(genres, score)
                
                case 5:
                    amount = float(input("Ingresa la cantidad de dinero: "))
                    print("cuando finalices presiona x")
                    genres = []
                    while(True):
                        auxGenre = input("Ingresa un genero: ")

                        if auxGenre in "xX":
                            break

                        if auxGenre in Menu.graphGenres:
                            genres.append(auxGenre)
                        else:
                            print("Ese genero no existe, ingresa uno valido")
                    Menu.services.RecommendShoppingList(genres, amount)
                
                case 6:
                    os.system("cls")
                    print("Programa Finalizado...")
                    break
                    

                
