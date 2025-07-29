# Chapter 8 - Functions
# Kess Ahmed, 29th July 2025
# Adjust the last program, prove that the lists are the same

# Create a function
def generate_messages(message):
    """Auto populate a list, 20 times, then return"""
    auto_list = []
    for value in range(20):
        auto_list.append(f"{message}: {value}")
    return auto_list

# Genereate a list of messages
new_messages = generate_messages('Hey this is a message')

# Generate empty list for sent_messages
sent_messages = []

# Create a function
def show_messages(messages):
    """Show each message in list on each line"""
    for message in messages:
        print(message)

# Use the list and print messages
show_messages(new_messages)

# Create a function
def send_messages(messages, sent_messages):
    """Convert and move each message from one list to another"""
    while messages:
        current_message = messages.pop()
        print(f"Sending... : {current_message}")
        sent_messages.append(current_message)

# Send messages <- ADDED SLICE TO KEEP ORIGINAL
send_messages(new_messages[:], sent_messages)

# Show both lists
show_messages(new_messages)
show_messages(reversed(sent_messages))
print(len(new_messages))
print(len(sent_messages))


