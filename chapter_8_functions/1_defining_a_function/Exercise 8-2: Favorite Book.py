# Chapter 8 - Functions
# Kess Ahmed, 29th July 2025
# Write a function called favorite_book(), accept one parameter, title. Print a message using argument, and call.

# Create function 
def favorite_book(title):
    """Parameter, book title, output simple message"""
    print(f"My favorite book is {title.title()}")

# Call function
favorite_book('The Hobbit')
favorite_book('The Lord of the Rings')
favorite_book('A Game of Thrones')
