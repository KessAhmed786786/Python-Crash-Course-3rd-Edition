# Chapter 4 - Working with Lists
# Make a list of the first 10 cubes, use a for loop to print out each cube
# Kess Ahmed, 20th July 2025

# Create a list called cubes
cubes = []

# Use a for loop to iterate 10 times
for value in range(1,11):
    # Append, modified value to cubes
    cubes.append(value**3)

# For loop to print each cube
for cube in cubes:
    print(cube)

