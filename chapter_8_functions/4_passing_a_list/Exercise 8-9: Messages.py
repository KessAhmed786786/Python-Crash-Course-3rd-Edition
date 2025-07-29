# Chapter 8 - Functions
# Kess Ahmed, 29th July 2025
# Pass a list of messages, that contain series of message strings, and then call the function

# Create a function
def generate_messages(message):
    """Auto populate a list, 20 times, then return"""
    auto_list = []
    for value in range(20):
        auto_list.append(f"{message}: {value}")
    return auto_list

# Genereate a list of messages
messages = generate_messages('Hey this is a message')

# Create a function
def show_messages(messages):
    """Show each message in list on each line"""
    for message in messages:
        print(message)

# Use the list and print messages
show_messages(messages)
