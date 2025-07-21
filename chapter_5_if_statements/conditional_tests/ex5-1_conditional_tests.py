# Chapter 5 - If Statements
# Kess Ahmed, 21st July 2025
# Write a series of conditional tests, print statements describing each test

# Test 1
# Assign value
car = 'subaru'

# Print prediction
print("Is car == 'subaru'? I predict True.")

# Print test
print(car == 'subaru')


# Other tests, numerical, and, or
#Test 2
car = 'subaru'
print("Is car == 'audi'? I predict False.")
print(car == 'audi')

#Test 3
car = 'subaru'
print("Is car != 'audi'? I predict True.")
print(car != 'audi')

#Test 4
car = 'subaru'
print("Is car != 'subaru'? I predict False.")
print(car != 'subaru')

# Test 5
age = 25
print("Is age > 18? I predict True.")
print (age > 18)

# Test 6
age = 18
print("Is age < 12? I predict False.")
print (age < 12)

# Test 7
age_0, age_1 = 18, 25
print("Is (age_0 > 10 and age_1 > 10? I predict True.")
print (age_0 > 10 and age_1 > 10)

# Test 8
age_0, age_1 = 18, 25
print("Is (age_0 > 20 and age_1 > 20? I predict False.")
print (age_0 > 20 and age_1 > 20)

# Test 9
age_0, age_1 = 18, 25
print("Is (age_0 > 20 or age_1 > 20? I predict True.")
print (age_0 > 20 or age_1 > 20)

# Test 10
age_0, age_1 = 18, 25
print("Is (age_0 > 20 or age_1 > 20? I predict False.")
print (age_0 > 100 or age_1 > 100)
