# Chapter 7 - User Input and while Loops
# Kess Ahmed, 24th July 2025
# Make a list called sandwich_orders and fill with names of various sandwiches, then empty list called finished_sandwiches. Loop through list of orders and print a message for each order. Then for loop all finished sandwiches

# Create list sandwich_orders
sandwich_orders = ['cheese and tomato sandwich', 'tuna sandwich', 'beef sandwich', 'chicken mayo sandwich', 'lettuce sandwich', 'cheese and tomato sandwich', 'tuna sandwich', 'beef sandwich', 'chicken mayo sandwich', 'lettuce sandwich', 'cheese and tomato sandwich', 'tuna sandwich', 'beef sandwich', 'chicken mayo sandwich', 'lettuce sandwich', 'cheese and tomato sandwich', 'tuna sandwich', 'beef sandwich', 'chicken mayo sandwich', 'lettuce sandwich', ]

# Create list finished_sandwiches
finished_sandwiches = []

# While loop
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Completing order: {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

# For loop
print("\nList of completed sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(f"\t -{finished_sandwich}")
