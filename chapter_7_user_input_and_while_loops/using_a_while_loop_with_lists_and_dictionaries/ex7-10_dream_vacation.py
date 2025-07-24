# Chapter 7 - User Input and while Loops
# Kess Ahmed, 24th July 2025
# Polling using a dictionary, prompt and print the results of the whole poll, while loop during the polling

# Create an empty dictionary
responses = {}

# Set flag
polling_active = True

# Prompt
v_prompt = "\nIf you could visit one place in the world, where would you go? "

# While loop prompting and adding
while polling_active:

    # Prompt and obtain name, vacation input
    name = input("\nWhat is your name? ")
    vacation = input(v_prompt)

    # Store in dictionary
    responses[name] = vacation

    # Exit loop strategy
    repeat_loop = input("Repeat? (yes/no)")
    if repeat_loop == 'no':
        polling_active = False

# Polling complete. Show results
print("\n---Results---")

# For loop dictionary
for name, vacation in responses.items():
    print(f"\tName: {name}")
    print(f"\t\tVacation: {vacation}")
