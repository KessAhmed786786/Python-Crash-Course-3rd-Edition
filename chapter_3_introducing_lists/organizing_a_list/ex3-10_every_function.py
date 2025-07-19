# Chapter 3 - Introducing Lists
# ex3-10_every_function.py
# Think of things you could store in a list. For example, you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items and then uses each function introduced in this chapter at least once.
# Kess Ahmed, 19th July 2025

# Create a list of various items
every_item = ['Mt. Everest', 'River Nile', 'Poland', 'Cairo', 'Japanese', 'Ice-Cream', 'Oak', 'Python', 'Geography']

# Print first item and last item
print(every_item[0])
print(every_item[8])

# Print using a f-string
print(f"This is {every_item[0]}")
print(f"This is {every_item[8]}")

# Print using a string method
print(f"This is {every_item[0].upper()}")
print(f"This is {every_item[8].lower()}")

# Replace an item with another
every_item[0] = "Mt. K2"
print(f"This is {every_item[0]}")

# Insert new beginning
every_item.insert(0, 'Diamond')

# Insert new middle
every_item.insert(4, 'Diamond')

# Append at end
every_item.append('Ego')
print(every_item)

# del 1st item in every_item
del every_item[0]
print(every_item)

# pop last item in every_item
every_item.pop()
print(every_item)

# Original list
print(every_item)

# Sorted(), temp alphabetically
print(sorted(every_item))

# Sorted(), temp reveres alphabetically
print(sorted(every_item, reverse=True))

# Reverse, original perma
every_item.reverse()
print(every_item)

# Alphabetical, perma 
every_item.sort()
print(every_item)
