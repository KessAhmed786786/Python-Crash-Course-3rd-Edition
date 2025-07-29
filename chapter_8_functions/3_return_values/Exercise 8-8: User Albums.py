# Chapter 8 - Functions
# Kess Ahmed, 29th July 2025
# Recreate last exercise using a while loop, add artist and albums via user input and then print the dictionary that is created, be sure to quit using break

# Adjust the function
def make_album(artist_name, album_name):
    """Create a dictionary about album information, artist, name, songs"""    
    album = {'artist': artist_name, 'album': album_name}
    return album

# Empty list
albums = []

# Create a while loop
while True:
    # Intro statement
    print("\nEnter an artist and then album:")
    print("('Enter 'q' at any point to quit')")

    # Artist input, with quit
    user_artist = input("Enter arist name: ")
    if user_artist == 'q':
        break

    # Album input, with quit
    user_album = input("Enter their album name: ")
    if user_album == 'q':
        break

    # Output user inputs from dictionary
    album = make_album(user_artist, user_album)
    for key, value in album.items():
        print(f"{key}: {value}")
    
    # Add to list
    albums.append(album)

# Counter
count = 1

# Print album and information related to each album
for album in albums:
    print(f"Album {count}") 
    count += 1
    for key,value in album.items():
        print(f"\t{key.title()}: {value}")
