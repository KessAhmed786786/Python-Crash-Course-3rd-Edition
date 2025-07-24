# Chapter 7 - User Input and while Loops
# Kess Ahmed, 24th July 2025
# Ask the user for a number, then report if the number is a multiple of ten or not

# Message variable
message = "Enter a number: "

# User input a number
user_number = input(message)

# Convert to int
user_number = int(user_number)

# If block
if user_number % 10 == 0:
    print(f"{user_number}: is a multiple of 10, {int(user_number / 10)}")
else:
    print(f"{user_number}: is not a multiple of 10")
