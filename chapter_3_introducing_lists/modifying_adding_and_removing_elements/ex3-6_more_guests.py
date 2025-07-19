# Chapter 3 - Introducing Lists
# ex3-6_more_guests.py
# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner. •Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table. •Use insert() to add one new guest to the beginning of your list. •Use insert() to add one new guest to the middle of your list. •Use append() to add one new guest to the end of your list. •Print a new set of invitation messages, one for each person in your list.
# Kess Ahmed, 19th July 2025

# Create a list called guests
guests = ['Dog', 'Cat', 'Bird']

# Print message to invite
print(f"I invite you to dinner {guests[0]}")
print(f"I invite you to dinner {guests[1]}")
print(f"I invite you to dinner {guests[2]}")

# Print statement of excused guest
print(f"Sorry {guests[0]} was busy, could not be invited\n")

# Replace excused guest, with new value
guests[0] = 'Panda'

# Print message to invite
print(f"I invite you to dinner {guests[0]}")
print(f"I invite you to dinner {guests[1]}")
print(f"I invite you to dinner {guests[2]}")

# Print statement for infroming bigger table
print("There is more space available at the table, more guests can join\n")

# insert() new guest beginning
guests.insert(0, 'Horse')

# insert() new guest middle
guests.insert(2, 'Monkey')

# append() new guest end
guests.append('Dragon')

# Print message to invite
print(f"I invite you to dinner {guests[0]}")
print(f"I invite you to dinner {guests[1]}")
print(f"I invite you to dinner {guests[2]}")
print(f"I invite you to dinner {guests[3]}")
print(f"I invite you to dinner {guests[4]}")
print(f"I invite you to dinner {guests[5]}")
