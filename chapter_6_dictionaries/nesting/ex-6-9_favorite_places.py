# Chapter 6 - Dictionaries
# Kess Ahmed, 23nd July 2025
# Create a dictionary called favorite_places, three keys, names of people and then a list for places they enjoy

# Create a dictionary called favorite_places
favorite_places = {
    'Kess': ['Forest', 'Mountain', 'Tundra'], 
    'Daniel': ['Beach'], 
    'Rocky': ['Hotel', 'Bed'], 
}

# For loop to loop each key and list value
for name, places in favorite_places.items():
    # Print key
    print(f"\n{name}")
    # Loop through each item in list value
    for place in places:
        # Print list item value
        print(f"\t- {place}")
