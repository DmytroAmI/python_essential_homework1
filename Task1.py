class Book:
    """Model a book"""

    def __init__(self, author, book_name, year, genre):
        """Initialize the attributes that describe the book"""
        self.author = author
        self.book_name = book_name
        self.year = year
        self.genre = genre

    def __str__(self):
        """Print book description"""
        return f"'{self.book_name}': {self.author}, {self.year}, {self.genre}"

    def __repr__(self):
        """Print book description"""
        return f"({self.author}, {self.book_name}, {self.year}, {self.genre})"


book1 = Book("Stephen King", "The Shining", 1977, "horror")
book2 = Book("George Orwell", "1984", 1949, "dystopia")

print(book1)
book3 = (book1, book2)
print(book3)


