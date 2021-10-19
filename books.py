from csv import DictReader

csv_file = 'files/books.csv'


class Book:
    title: str
    author: str
    pages: int
    genre: str

    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre

    def __str__(self):
        return "Book: title is %s, author is %s, pages is %s, genre is %s" % (
            self.title, self.author, self.pages, self.genre)


def read_books(filename):
    books = []
    with open(filename, 'r') as file:
        reader = DictReader(file)
        iterator = iter(reader)
        while True:
            try:
                row = next(iterator)
                books.append(Book(title=row['Title'], author=row['Author'], pages=row['Pages'], genre=row['Genre']))
            except StopIteration:
                break
        return books
