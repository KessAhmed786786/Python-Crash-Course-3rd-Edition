# Chapter 7 - User Input and while Loops
# Kess Ahmed, 24th July 2025
# Movie theater charges different ticket prices, depedning on person age. age 3, 3-12, over 12, 


# Create a prompt variable
prompt = "\nMovie Tickets: What is your age, customer? "
prompt += "\nEnter 'quit' to exit the program. "

# Create flag variable
active = True

# While loop
while active:
    # Input, ask user, via prompt
    customer_age = input(prompt)

    # If statement to check if pizza_topping is 'quit'
    if customer_age == 'quit':
        active = False
        
        # Infrom user the program has ended
        print("\nThe program has ended")
    else:
        # Convert to integer
        customer_age = int(customer_age)

        # Variable statement, changing price
        price = "The ticket costs: "

        # If-elif-else block, using one changing variable
        if customer_age < 3:
            print(price + "Free")
        elif customer_age >= 3 and customer_age <= 12:
            print(price + "$10")
        elif customer_age > 12 and customer_age <= 120:
            print(price + "$15")
        else:
            print("Are you human?")



