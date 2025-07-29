# Chapter 8 - Functions
# Kess Ahmed, 29th July 2025
# Write function called make_shirt, parameters size and text, with output being a message. Call using positional arguments, and then again using keyword

# Create a function
def make_shirt(shirt_size, shirt_text):
    """Prints a summar of shirt size and text"""
    print(f"Shirt size: {shirt_size}, Shirt text: {shirt_text}")

# Positional calling
make_shirt('large', 'dreamer')

# Keyword calling
make_shirt(shirt_text='nightmare', shirt_size='small')
