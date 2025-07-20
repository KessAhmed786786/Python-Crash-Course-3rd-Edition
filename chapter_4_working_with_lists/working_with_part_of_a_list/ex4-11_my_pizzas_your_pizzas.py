# Chapter 4 - Working with Lists
# Copy list of pizzas, called friend_pizzas. Add new to the original, and different one to friend_pizzas, the prove using for loop
# Kess Ahmed, 20th July 2025

# Copied list from before
pizzas = ['cheese', 'chicken', 'hawaiian']

# Copy list, using slice
friend_pizzas = pizzas[:]

# Append to pizzas
pizzas.append('beef')

# Append to friend_pizzas
friend_pizzas.append('anchovy')

# for loop iteration pizzas
print("\nMy favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

# for loop iteration friend_pizzas
print("\nMy friends favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# update 
