# Chapter 2 - Variables and Simple Data Types
# ex2-7_stripping_names.py
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
# Kess Ahmed, 16th July 2025

# Declare a variable, with whitespaces using space \t and \n
person_name_whitespace = "         \n      John John Jr \t\n\t"

# Print unedited
print(person_name_whitespace)

# Print lstrip()
print(person_name_whitespace.lstrip())

# Print rstrip()
print(person_name_whitespace.rstrip())

# Print strip()
print(person_name_whitespace.strip())
