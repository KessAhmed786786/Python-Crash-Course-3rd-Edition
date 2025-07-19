# Chapter 3 - Introducing Lists
# ex3-8_seeing_the_world.py
# Think of at least five places in the world you’d like to visit. •Store the locations in a list. Make sure the list is not in alphabetical order. •Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list. •Use sorted() to print your list in alphabetical order without modifying the actual list.•Show that your list is still in its original order by printing it. •Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list. •Show that your list is still in its original order by printing it again. •Use reverse() to change the order of your list. Print the list to show that its order has changed. •Use reverse() to change the order of your list again. Print the list to show it’s back to its original order. •Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed. •Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.
# Kess Ahmed, 19th July 2025

# Create a list called places
places = ['Overworld', 'Nether', 'The End', 'Ocean', 'Desert', 'Jungle']

# Print raw python list: original list
print(places)

# Print raw python list: sorted(), print alphabetically
print(sorted(places))
print(places)

# Print raw python list: reverse sorted(), print reverse alphabetically
print(sorted(places, reverse=True))
print(places)

# Print raw python list: reverse permanetly
places.reverse()
print(places)

# Print raw python list: revert original permanetly
places.reverse()
print(places)

# Print raw python list: alphabetically permanetly
places.sort()
print(places)

# Print raw python list: reverse alphabetically permanetly
places.sort(reverse=True)
print(places)
