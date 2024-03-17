class Book:
    """Model a book"""

    def __init__(self, author, book_name, year, genre):
        """Initialize the attributes that describe the book"""
        self.author = author
        self.book_name = book_name
        self.year = year
        self.genre = genre
        self.review_list = []

    def add_review(self, review):
        """Add new review in the list"""
        self.review_list.append(review)

    def __str__(self):
        """Print book description"""
        print_book = f"'{self.book_name}': {self.author}, {self.year}, {self.genre}"

        if self.review_list:
            return print_book + f", reviews: {self.review_list}"
        else:
            return print_book + ", reviews: no reviews yet"

    def __repr__(self):
        """Print book description"""
        return f"({self.author}, {self.book_name}, {self.year}, {self.genre})"


class Review:
    """Describes the book review"""

    def __init__(self, review_text, rating, author_review):
        """
        Initialize review attribute
        The rating cannot be more than 100
        """
        self.review_text = review_text
        self.rating = rating
        self.author_review = author_review

        if rating > 100:
            self.rating = 100

    def __str__(self):
        """Print review description"""
        return f"'{self.review_text}', user rating - {self.rating}, reviewer {self.author_review}"

    def __repr__(self):
        """Print review description in list"""
        return f"('{self.review_text}', {self.rating}/100, reviewer {self.author_review})"


book1 = Book("Stephen King", "The Shining", 1977, "horror")
book2 = Book("George Orwell", "1984", 1949, "dystopia")

book1.add_review(Review("My favorite book", 1000, "Peter"))
book1.add_review(Review("Good book, recommend it", 76, "Marie"))
book1.add_review(Review("Hate this book", 22, "Tom"))

print(book1)
print(book2)
