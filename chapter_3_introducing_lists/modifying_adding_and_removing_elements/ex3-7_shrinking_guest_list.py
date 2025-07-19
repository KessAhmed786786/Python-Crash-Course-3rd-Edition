# Chapter 3 - Introducing Lists
# ex3-7_shrinking_guest_list.py
# You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests. •Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner. •Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner. •Print a message to each of the two people still on your list, letting them know they’re still invited. •Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
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

# Print statment for informing table is late
print("The table is arriving late, only two guests can sit\n")

# pop() end of stack each list, print message to say sorry
dismissed_guest = guests.pop()
print(f"Sorry {dismissed_guest}, better luck next time")
dismissed_guest = guests.pop()
print(f"Sorry {dismissed_guest}, better luck next time")
dismissed_guest = guests.pop()
print(f"Sorry {dismissed_guest}, better luck next time")
dismissed_guest = guests.pop()
print(f"Sorry {dismissed_guest}, better luck next time")

# print, message for last two elements in list
print(f"You are the last guests {guests[0]}, {guests[1]}\n")

# del elements in guests, to make empty and print to prove
print("Removing all elements")
del guests[0]
del guests[0]
print(guests)
