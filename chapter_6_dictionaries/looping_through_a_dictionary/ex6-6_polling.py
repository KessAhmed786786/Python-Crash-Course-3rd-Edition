# Chapter 6 - Dictionaries
# Kess Ahmed, 23nd July 2025
# Use code before, list people who should take poll from inside key's favorite_language and not. Loop, list and if yes thank, if not invite

# Copy code, dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

# Create a list
people_list = ['daniel',
               'jen',
               'sarah',
               'edward',
               'henry',
               'jon',
               'phil',
               'hyunjin',
               ]

# Loop throuhg each person in person list
for person in people_list:
    if person in favorite_languages.keys():
        print(f"Thank you for taking our poll {person.title()}")
    else:
        print(f"Would you like to take our poll {person.title()}?")
