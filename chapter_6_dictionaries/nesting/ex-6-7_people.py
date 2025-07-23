# Chapter 6 - Dictionaries
# Kess Ahmed, 23nd July 2025
# Copy a dictionary, using the same structure generate 3 more people, store in a list

# Copy previous dictionary
person_0 = {'first_name':'Kess', 'last_name':'Ahmed', 'age':'23', 'city':'London',}

# Person 1 dictionary
person_1 = {'first_name':'Daniel', 'last_name':'Aguilar', 'age':'24', 'city':'San Jose',}

# Person 2 dictionary
person_2 = {'first_name':'Rocky', 'last_name':'Jackson', 'age':'32', 'city':'California',}

# Add to list called people
people = [person_0, person_1, person_2]

# Loop and format nicely
for person in people:
    print(f"\nHey {person['first_name'].title()} "
          f"{person['last_name'].title()}")
    print("Here is some information:")
    print(f"\t First Name: {person['first_name']}")
    print(f"\t Last Name: {person['last_name']}")
    print(f"\t Age: {person['age']}")
    print(f"\t City: {person['city']}")
