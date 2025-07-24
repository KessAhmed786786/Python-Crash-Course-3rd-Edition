# Chapter 7 - User Input and while Loops
# Kess Ahmed, 24th July 2025
# Asks the user what rental car they would like, print a message about that car.

# Message for input
message = "What rental car would you like sir?"
message += "\nSome suggestions: Subaru, Audi, Hyundai etc... "

# User input: car
rental_car = input(message)

# Make it lower()
rental_car = rental_car.lower()

# Output input as string
print(f"Let me see if I can find you a {rental_car.title()}")
