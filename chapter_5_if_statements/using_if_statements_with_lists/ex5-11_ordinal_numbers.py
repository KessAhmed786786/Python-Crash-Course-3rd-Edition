# Chapter 5 - If Statements
# Kess Ahmed, 22nd July 2025
# Store integers from 1-9 in a list, loop through and use if-elif-else chain to print proper ordinal ending

# Generate a list using range()
ordinals = list(range(1,10))

# Use for loop 
for ordinal in ordinals:
    # if 1, 1st
    if ordinal == 1:
        print(f"{ordinal}st")
    # elif 2, 2nd
    elif ordinal == 2:
        print(f"{ordinal}nd")
    # elif 3, 3rd
    elif ordinal == 3:
        print(f"{ordinal}rd")
    # else, end in th
    else:
        print(f"{ordinal}th")

