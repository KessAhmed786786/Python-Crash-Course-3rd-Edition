# Chapter 5 - If Statements
# Kess Ahmed, 22nd July 2025
# Make a list of usernames, including 'admin' print a greeting for each, making sure admin is special

# Genereate a list of usernames
usernames = ['admin', 'JohnSmith', 'Jaden', 'SupaFriend', 'Waterbucket']

# For loop for each username
for username in usernames:
    # If admin, print special message
    if username == 'admin':
        print(f"Hello {username}, would you like to see a status report?")
    # Else print generic message
    else:
        print(f"Hello {username}, thank you for logging in again.")

