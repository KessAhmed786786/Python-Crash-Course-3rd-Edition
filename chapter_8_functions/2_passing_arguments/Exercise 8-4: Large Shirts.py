# Chapter 8 - Functions
# Kess Ahmed, 29th July 2025
# Modify make_shirt(), large by default value and text default value "I love Python", make a large and medium with default values, and then another any size with any message

# Create a function
def make_shirt(shirt_size='large', shirt_text='I love Python'):
    """Prints a summar of shirt size and text"""
    print(f"Shirt size: {shirt_size}, Shirt text: {shirt_text}")

# Large, I love Python
make_shirt()

# Medium, I love Python
make_shirt(shirt_size='medium')

# Small, I love pizza
make_shirt(shirt_text='I love pizza', shirt_size='small')
