# Chapter 5 - If Statements
# Kess Ahmed, 21st July 2025
# More tests, equaity, inequality with strings, tests using the lower method, numerical tests, and, or, in, not. Have one true and one false per

# Test equality strings
print("\nTest equality strings")

name_0 = 'John'
name_1 = 'Mark'
name_2 = 'John'

print(name_0 == name_1)
print(name_0 == name_2)

# Test equality lower() method
print("\nTest equality lower() method")

name_0 = 'Marcus'
name_1 = 'MaRcUs'

print(name_0.upper() == name_1.lower())
print(name_0.lower() == name_1.lower())

# Numerical tests, <, >, <=, >=
print("\nNumerical tests, <, >, <=, >=")

num_0 = 10
num_1 = 10
num_2 = 20
num_3 = 50

print(num_0 > num_1)
print(num_0 >= num_1)
print(num_2 < num_3)
print(num_3 <= num_2)

# Test using and, or
print("\nTest using and, or")

num_0 = 0
num_1 = 1

print(num_1 == 1 and num_1 == 1)
print(num_0 == 1 and num_1 == 1)
print(num_1 == 1 or num_1 == 1)
print(num_0 == 1 or num_0 == 1)

# Test using in
print("\nTest using in")

books = ["Othello", "A Game of Thrones", "Deep Work", "Alice in Wonderland", "Little Women"]

print("Othello" in books)
print("The Alchemist" in books)

# Test using not
print("\nTest using not")

print("Othello" not in books)
print("The Alchemist" not in books)
