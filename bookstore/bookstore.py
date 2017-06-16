class Bookstore(object):
#storing books, adding/get/search for books

    def __init__(self, name):
        self.name = name
        self.book_list = []
        
    def add_book(self, book):
        self.book_list.append(book)
        
        
    def get_books(self):
        return self.book_list
        
    
    def search_books(self, author=None, title=None):
        requested_books = []
        if author == None and title == None:
            return 'invalid'
        elif author == None: # searching for title!
            for book in self.book_list:
                if title.lower() in book.title.lower():
                    requested_books.append(book)
        elif title == None: # searching for author!
            for book in self.book_list:
                if author.name.lower() in book.author.name.lower():
                    requested_books.append(book)
        else:
            for book in self.book_list:
                if title.lower() in book.title.lower() and author.name.lower() in book.author.name.lower():
                    requested_books.append(book)
        return requested_books        
        #can search by book title or book author, or both title and author


class Author(object):
#creates an author 
    def __init__(self, name, nationality):
        self.nationality = nationality
        self.name = name
        self.author_books = []
        #Do we need each author to have their own list of books???
        
    def get_books(self):
        return self.author_books

#author1 = Author('Alex','US')
#print(author1)


class Book(object):
#creates a book using: title and author
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.author_books.append(self)
        
# book1 = Book("Computers Are Neat", "Alex")
# print(book1)