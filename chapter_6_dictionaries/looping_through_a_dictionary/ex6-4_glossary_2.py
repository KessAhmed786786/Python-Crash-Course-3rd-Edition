# Chapter 6 - Dictionaries
# Kess Ahmed, 23nd July 2025
# Replace previous print calls with a for loop, key and value, then add more terms

# Copy dictionary
glossary = {
    'dictionary':'A collection of key-value pairs', 'key':'First part of the pair, connected by colon', 
    'value':'Value that is associated to the key',
    '.get()':'Error handle if you think the value does not exist, default value',
    'modify':'Call dictionary name, then in [] find key and assign new value with =',
    'water':'a drinkable liquid',
    'fire':'a hot plasma with various uses',
    'earth':'a substance made of soil, rocks found in the ground',
    'air':'an invisible substance used to breath',
    'grass':'a living organism that sustains a bioculture'
    }

# Ignore title list
ignore_title_list = ['.get()']

# For loop loop through key and value
for key, value in glossary.items():
    if key in ignore_title_list:
        print(f"\n {key}: {value}")
    else:
        print(f"\n {key.title()}: {value}")

# For loop loop renamed for better naming
for word, definition in glossary.items():
    if word in ignore_title_list:
        print(f"\n {word}: {definition}")
    else:
        print(f"\n {word.title()}: {definition}")
