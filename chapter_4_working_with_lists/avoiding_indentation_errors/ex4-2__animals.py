# Chapter 4 - Working with Lists
# ex4-2_animals.py
# Think of at least three different animals that have a common characteristic. Store the names of these animals in a list, and then use a for loop to print out the name of each animal. •Modify your program to print a statement about each animal, such as A dog would make a great pet. •Add a line at the end of your program, stating what these animals have incommon. You could print a sentence, such as Any of these animals would make a great pet!
# Kess Ahmed, 20th July 2025

# Create a lits called common_animals
common_animals = ['Dog', 'Cat', 'Horse']

# Use a for loop to print each element
for common_animal in common_animals:
    print(common_animal)

# Modifyed using f-string
for commmon_animal in common_animals:
    print(f"A {commmon_animal.lower()} would make a great pet.")

# Summary print statement
print("Any of these animals would make a great pet!")
