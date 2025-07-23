# Chapter 6 - Dictionaries
# Kess Ahmed, 23nd July 2025
# Create a glossary, think of programming words, store meanings in values, then print call call key and value use a newline to seperate the key-values

# Create a dictionary
glossary = {
    'dictionary':'A collection of key-value pairs', 'key':'First part of the pair, connected by colon', 
    'value':'Value that is associated to the key',
    '.get()':'Error handle if you think the value does not exist, default value',
    'modify':'Call dictionary name, then in [] find key and assign new value with =',
    }

# print all values of glossary dictionary
print(f"\nDictionary: {glossary['dictionary']}")
print(f"\nKey: {glossary['key']}")
print(f"\nValue: {glossary['value']}")
print(f"\n.get(): {glossary['.get()']}")
print(f"\nModify: {glossary['modify']}")
