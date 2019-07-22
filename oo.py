"""
1. Discussion
-------------

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.
   -Easily organizing things into groups and subgroups while keeping them connected
   -Easy to change attributes of values
   -Functions (methods) that apply to specific types of objects

2. What is a class?
-a way to group values that share similar attributes and expected functions

3. What is a method?
-a function in a class that applies to objects of that class

4. What is an instance in object orientation?
-an instantiated object of a class - has class atributes and 
access to class methods

5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.
-a class attribute is an attribute that is initially set 
the same for each instance within a class 
ex- a tax specific to domestic melon orders in a DomesticMelonOrder class
-a instance attribute is takes input to set specifically for an instance
ex- a qty of an order in a DomesticMelonOrder class

"""


# 2. Road Class
# #############################################################################

# Create your Road class here
class Road():
    """Class track number of lanes and speed limit of roads"""
    num_lanes = 2
    speed_limit = 25

# Instantiate Road objects here
road1 = Road()
road2 = Road()
road1.num_lanes = 4
road1.speed_limit = 60

print(road1.num_lanes, road1.speed_limit, road2.num_lanes, road2.speed_limit)

# 3. Update Password
# #############################################################################
class User(object):
    """A user object."""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    # method to change password attribute
    def update_password(self, current_password, new_password):
        if self.password == current_password:
            self.password = new_password
        else:
            print("Invalid password")




# 4. Build a Library
# #############################################################################
class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create your Library class here
class Library():
    """Class that includes a collection of books"""
    books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def find_books_by_author(self, author):
        authors_books = []
        for book in self.books:
            if book.author == author:
                authors_books.append(book)
        return authors_books

    def print_books(self, books):
        # for testing code
        for book in books:
            print(book.title, book.author)












