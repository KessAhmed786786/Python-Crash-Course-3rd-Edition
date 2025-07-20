# Chapter 4 - Working with Lists
# Perform the following to a list: print first 3, print middle 3, print last 3
# Kess Ahmed, 20th July 2025

# Reuse and add to an old list
pizzas = ['cheese', 'chicken', 'hawaiian', 'veggie', 'mushrrom', 'beef', 'meat-supreme', 'pepperoni', 'donner']

# Print message 1
print("\nThe first three items in the list are:")

# Use a for loop, slice() to print the first three items
for pizza in pizzas[:3]:
    print(pizza.title())

# Print message 2
print("\nThree items from the middle of the list are:")

# Use a for loop, slice() to print the middle three items
for pizza in pizzas[3:6]:
    print(pizza.title())

# Print message 3
print("\nThe last three items in the list are:")

# Use a for loop, slice() to print the last three items
for pizza in pizzas[-3:]:
    print(pizza.title())


