# Chapter 5 - If Statements
# Kess Ahmed, 22nd July 2025
# Add an if statement to previous exercise to check if not empty, if so print warning message


# Genereate a list of usernames
usernames = ['admin', 'JohnSmith', 'Jaden', 'SupaFriend', 'Waterbucket']

# Toggle comment to check
# usernames = []

# Check if the list is empty or not
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    # Print warning
    print("We need to find some users!")

