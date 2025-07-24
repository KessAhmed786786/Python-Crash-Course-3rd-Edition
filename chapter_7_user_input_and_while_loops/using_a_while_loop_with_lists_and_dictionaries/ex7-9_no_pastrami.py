# Chapter 7 - User Input and while Loops
# Kess Ahmed, 24th July 2025
# Add three pastrami, but remove and inform the user that the sandwich has ran out

# Create list sandwich_orders
sandwich_orders = ['cheese and tomato sandwich', 'tuna sandwich', 'pastrami', 'beef sandwich', 'chicken mayo sandwich', 'lettuce sandwich', 'cheese and tomato sandwich', 'pastrami', 'tuna sandwich', 'beef sandwich', 'chicken mayo sandwich', 'pastrami', 'lettuce sandwich', 'cheese and tomato sandwich', 'tuna sandwich', 'beef sandwich', 'chicken mayo sandwich', 'lettuce sandwich', 'cheese and tomato sandwich', 'tuna sandwich', 'beef sandwich', 'chicken mayo sandwich', 'pastrami', 'pastrami', 'lettuce sandwich', ]

# Create list finished_sandwiches
finished_sandwiches = []

# Remove pastrami sandwiches
print("\nThe deli has ran out of pastrami sandwiches!")

# Number removed declared
number_removed = 0

# While loop to remove
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    number_removed += 1

print(f"\tRemoved {number_removed} pastrami sandwiches\n")


# While loop
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Completing order: {current_sandwich.title()}")
    finished_sandwiches.append(current_sandwich)

# For loop
print("\nList of completed sandwiches:")
for finished_sandwich in finished_sandwiches:
    print(f"\t -{finished_sandwich}")
