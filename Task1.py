class Book:
    """Model a book"""

    def __init__(self, author, name, year, genre):
        """Initialize the attributes that describe the book"""
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.reviews = []

    def add_review(self, review):
        """Add new review in the list"""
        self.reviews.append(review)

    def __str__(self):
        """Print book description"""
        result = f"'{self.name}': {self.author}, {self.year}, {self.genre}"

        if not self.reviews:
            return result + ", reviews: no reviews yet"

        for review in self.reviews:
            result += f"\nReview: {review}"

        return result

    def __repr__(self):
        return (f"Book(author={self.author}, "
                f"name={self.name}, "
                f"year={self.year}, "
                f"genre={self.genre}, "
                f"reviews={self.reviews})")


class Review:
    """Describes the book review"""

    def __init__(self, text, rating, author):
        """
        Initialize review attribute
        The rating cannot be more than 100
        """
        self.text = text
        self.rating = rating
        self.author = author

        if rating > 100:
            self.rating = 100

    def __str__(self):
        """Print review description"""
        return f"'{self.text}', user rating - {self.rating}, reviewer {self.author}"

    def __repr__(self):
        return f"Review(text={self.text}, rating={self.rating}, author={self.author})"


book1 = Book("Stephen King", "The Shining", 1977, "horror")
book2 = Book("George Orwell", "1984", 1949, "dystopia")

book1.add_review(Review("My favorite book", 1000, "Peter"))
book1.add_review(Review("Good book, recommend it", 76, "Marie"))
book1.add_review(Review("Hate this book", 22, "Tom"))

print(book1)
print(book2)
