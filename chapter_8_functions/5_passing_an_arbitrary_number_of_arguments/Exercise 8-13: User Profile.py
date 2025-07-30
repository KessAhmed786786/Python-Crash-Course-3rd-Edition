# Chapter 8 - Functions
# Kess Ahmed, 30th July 2025
# Create a function called, user_profile, build your profile based on first and last names and any 3 extra arbitrary values, using **kwargs


# Create a function
def user_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info


# Call function
my_profile = user_profile(
    "kess", "ahmed", location="united kingdom", field="student", fav_food="blueberries"
)


# Create a function to display dictionary
def print_profile(profile):
    print(f"{profile['first_name'].title()} {profile['last_name'].title()}")
    for key, value in profile.items():
        print(f"- {key}: {value}")


# Output dictionary
print_profile(my_profile)
