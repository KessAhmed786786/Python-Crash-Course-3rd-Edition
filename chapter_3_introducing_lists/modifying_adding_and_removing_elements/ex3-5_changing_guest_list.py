# Chapter 3 - Introducing Lists
# ex3-5_changing_guest_list.py
# You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite. •Start with your program from Exercise 3-4. Add a print() call at the end of your program, stating the name of the guest who can’t make it. •Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting. •Print a second set of invitation messages, one for each person who is still in your list.
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
