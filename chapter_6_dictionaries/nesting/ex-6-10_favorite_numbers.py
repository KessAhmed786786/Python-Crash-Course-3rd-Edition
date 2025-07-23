# Chapter 6 - Dictionaries
# Kess Ahmed, 23nd July 2025
# Modify so each person can have more that one favorite number, print name alongside favorite numbers

# Create a dictionary
favorite_numbers = {
    'kess': [12,34,56],
    'ttar': [12,34],
    'blunder': [89,90],
    'tdweeb': [1,2,3,4,5,6,7,8,9],
    'russ': [1219021, 122423],
}

# Print each key and value in same string
for name, numbers in favorite_numbers.items():
    print(f"\n {name}")
    for number in numbers:
        print(f"\t{number}")
