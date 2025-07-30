# Chapter 8 - Functions
# Kess Ahmed, 30th July 2025
# Write function that accepts a list of items a person wants on a sandwich. Use one for positional and anoother arbitrary tuple


# Create a function
def make_sandwich(name, *fillings):
    print(f"\nMaking a {name} sandwich, with the filling:")
    for filling in fillings:
        print(f"- {filling}")


# Call function
make_sandwich("BLT", "bacon", "lettuce", "tomato")

make_sandwich("CLT", "chicken", "lettuce", "tomato")

make_sandwich("VLT", "veggie", "lettuce", "tomato")
