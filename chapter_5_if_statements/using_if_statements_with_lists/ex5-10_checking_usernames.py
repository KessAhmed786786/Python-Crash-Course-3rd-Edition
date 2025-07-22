# Chapter 5 - If Statements
# Kess Ahmed, 22nd July 2025
# Simulate website username behaviour, create a list of current_users, and another new_users, then check for each new user if they are a current user, using string methods to check for various cases

# Create a list: current_users
current_users = ['shark', 'JohnSmith', 'Jaden', 'SupaFriend', 'Waterbucket']

# Create a copy of current_users, lowercase, for loop
current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())

# Create a list: new_users
new_users = ['FanOfSky', 'JohnSmith', 'EagleEye', 'SupaEnemy', 'WATERBUCKET']

# Loop through each of new_users and check with current_users
for new_user in new_users:
    # Check if new_user (lowercase) is in current users (lowercase), if print warning
    if new_user.lower() in current_users_lower:
        print(f"{new_user}: Please enter a new username.")
    # Else accept
    else:
        print(f"{new_user}: Username is available!")
