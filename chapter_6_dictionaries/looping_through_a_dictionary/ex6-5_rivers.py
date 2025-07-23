# Chapter 6 - Dictionaries
# Kess Ahmed, 23nd July 2025
# Make a dictionary containing three major rivers and the country, use a for loop to the print key-value, key only and value only

# Create a dictionary
rivers = {
    'nile':'eygpt', 
    'amazon':'brazil', 
    'ganges':'india', 
}

# Print title declarion
print("\n The river facts:")

# Create for loop of print: key-value
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

# Counter
number = 1
print("\n The list of only rivers:")

# Create for loop print: key only
for river in rivers.keys():
    print(f"{number}: {river.title()} ")
    number = number + 1

# Counter
number = 1
print("\n The list of only countries:")

# Create for loop print: value only
for country in rivers.values():
    print(f"{number}: {country.title()} ")
    number = number + 1


