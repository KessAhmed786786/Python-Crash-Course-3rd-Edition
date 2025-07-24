# Chapter 7 - User Input and while Loops
# Kess Ahmed, 24th July 2025
# Write a loop that prompts the user to enter a series of pizza toppings, until they enter 'quit' print the pizza topping added

# Create a prompt variable
prompt = ("\nEnter a pizza topping: ")

# Add another line to inform user how to exit
prompt += ("\nEnter 'quit' to end the program. ")

# Create flag variable
active = True

# Create an empty list of pizza_toppings
pizza_toppings = []

# While loop
while active:
    # Input pizza_topping
    pizza_topping = input(prompt)

    # If statement to check if pizza_topping is 'quit'
    if pizza_topping == 'quit':
        active = False
    else:
        print(pizza_topping)
        pizza_toppings.append(pizza_topping)

# Infrom user the program has ended
print("\nProgram has ended")

# Output list of toppings, printing only if unqiue
print("\nList of toppings added:")
for pizza_topping in set(pizza_toppings):
    print(f"{pizza_topping}")
