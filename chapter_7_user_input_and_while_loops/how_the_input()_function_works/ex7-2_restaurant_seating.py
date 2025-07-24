# Chapter 7 - User Input and while Loops
# Kess Ahmed, 24th July 2025
# Ask for how many people are in their dinner group, if more than eight say wait else ready

# Message variable
message = "How many people are attending your dinner group? "

# Input variable
response = input(message)

# Convert into int()
response = int(response)

# If statement block
if response > 8:
    print("Sorry, you will have to wait a table")
else:
    print("Your table is ready!")
