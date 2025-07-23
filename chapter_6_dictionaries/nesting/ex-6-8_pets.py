# Chapter 6 - Dictionaries
# Kess Ahmed, 23nd July 2025
# Create several dictionaries, each one represtensts a different pet. Include type:, owner_name:, store in a list called pets

# Template for unique empty pet
pet_0 = {
    'name': '',
    'species': '',
    'owner_name': '',
}


# Create empty list to store pets in
pets = []

# Make 10 pets using range() function
for pet_number in range(10):
        new_pet = pet_0 = {
        'name': 'Snow',
        'species': 'Dog',
        'owner_name': 'Kess',
    }
        pets.append(new_pet)

# Counter
number = 1

# For loop each pet in list of pets
for pet in pets:
    print(f"\nPet {number}")
    number += 1
    for key, value in pet.items():
          print(f"\t{key.title()}: {value.title()}")
