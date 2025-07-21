# Chapter 5 - If Statements
# Kess Ahmed, 21st July 2025
# Write an if-elif-else chain that determines a person's stage of life. Set value for the variable age and test various cases

# Create variables, uncomment to test
#person_age = -1
person_age = 3
#person_age = 12
#person_age = 19
#person_age = 30
person_age = 100

# If-elif-else block to test each case, with catch all
if person_age < 2 and person_age >= 0:
    print("You are a baby")
elif person_age < 4 and person_age >= 2:
    print("You are a toddler")
elif person_age < 13 and person_age >= 4:
    print("You are a kid")
elif person_age < 20 and person_age >= 13:
    print("You are a teenager")
elif person_age < 65 and person_age >= 20:
    print("You are a adult")
elif person_age < 120 and person_age >= 65:
    print("You are an elder")
else:
    print("Are you human?")

# Would need checking if the person_age variable is an integer, not a random string or anything else
