# Chapter 4 - Working with Lists
# Write two for loops to print each list of foods
# Kess Ahmed, 20th July 2025

# Create a list called foods
foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

# Iterate over for loop
print(f"\nThe list of foods is {len(foods)} items long:")
for food in foods:
    print(food.title())

# Iterate over for loop the first 3 items
print(f"\nThe the first 3 foods are {len(foods[:3])} items long:")
for food in foods[:3]:
    print(food.title())
