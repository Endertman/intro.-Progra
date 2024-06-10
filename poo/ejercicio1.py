import numpy as np

# __init__ es un metodo especial en python que le permite crear atributos de una clase cuando se crea un objeto.
# self hace referencia al objeto que se esta creando.
# __str__ es un metodo que se llama cuando se imprime un objeto. 

# class Comic:
#     def __init__(self, title, editorial, version, hero):
#         self.title = title
#         self.editorial = editorial
#         self.version = version
#         self.hero = hero
    
#     def __str__(self):
#         return f'Comic(Title = {self.title}, Hero = {self.hero}, )'
class Book: 
    def __init__(self, title, author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f'Book(title = {self.title}, author = {self.author}, isbn  ={self.isbn})'

class Library:
    def __init__(self):
        self.Books = []

    def add_book(self, book):
        self.Books.append(book)
        print(f'Book {book.title} added')

    def see_books(self):
        if len(self.Books) == 0:
            print('No books')
        else:
            for book in self.Books:
                print(book)

    def find_book(self, isbn):
        for book in self.Books:
            if book.isbn == isbn:
                 break
            
    def remove_book(self, isbn):
        for book in self.Books:
            if book.isbn == isbn:
                self.Books.remove(book)
                print(f'Book with ISBN {isbn} removed')
                break
            

book1 = Book('Calculo de variables temporanas', 'James Stewart', 123)
book2 = Book('Introduccion la logica matematica', 'Enderton Hebert', {np.random.randn()})
book3 = Book('Fisica General', 'Bueche', {np.random.randn()})

library = Library()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.see_books()

library.remove_book(123)


# def get_title(self):
#     return self.title   

# def get_isbn(self):
#     return self.isbn