class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books += [book]

class Book:
    def __init__(self, title):
        self.title = title

my_library = Library()
print(my_library)                           # <__main__.Library objec at 0x...>

book_1 = Book('The Grapes of Wrath')
my_library.add_book(book_1)

print(my_library.books[0].title)                           # 'The Grapes of Wrath'