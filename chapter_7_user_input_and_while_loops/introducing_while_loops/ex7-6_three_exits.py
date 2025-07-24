# Chapter 7 - User Input and while Loops
# Kess Ahmed, 24th July 2025
# Change 7-4, use conditional test in the while statement to stop the loop, use an active variable to contorl how long the loop runs, use a break statement to exit th eloop when the user enters a 'quit' value.

# Prompts for all
prompt = ("\nEnter a pizza topping: ")
prompt += ("\nEnter 'quit' to end the program. ")

# Empty string ready
pizza_topping = ""

while pizza_topping != 'quit':
    pizza_topping = input(prompt)

    # Making sure only toppings and not quit printed
    if pizza_topping != 'quit':
        print(pizza_topping)
    
print("\nProgram has ended")


# Active variable to control to control loop size
# Active control variable ready
active_control = 0
while active_control < 5:
    # User infroming of uses left
    print(f"\nYou have {5 - active_control} inputs left...")
    pizza_topping = input(prompt)
    print(pizza_topping)

    # Increment active_control
    active_control += 1
    
print("\nProgram has ended")


# Use break statement
while True:
    pizza_topping = input(prompt)
    if pizza_topping == 'quit':
        break
    else:
        print(pizza_topping)
print("\nProgram has ended")



# Original basic version
active = True
while active:
    pizza_topping = input(prompt)
    if pizza_topping == 'quit':
        active = False
    else:
        print(pizza_topping)
print("\nProgram has ended")

