# Chapter 6 - Dictionaries
# Kess Ahmed, 23nd July 2025
# Just imporove formatting from older code

# Make an empty list for storing aliens.
aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {
        'color': 'green', 
        'points': 5, 
        'speed': 'slow'}
    aliens.append(new_alien)


# Index counter
counter = 1

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(f"Alien {counter}")
    counter += 1
    for key, value in alien.items():
        print(f"\tKey: {key}, Value: {value}")
print("...")
