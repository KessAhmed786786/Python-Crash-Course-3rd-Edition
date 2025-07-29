# Chapter 8 - Functions
# Kess Ahmed, 29th July 2025
# Create a function called make_album(), build a dictionary describing album. artist name, album title, return these two pieced of information, make three albums, for loop to print all info related to album. Use None to add optional parameter for number of songs.

# Create a function
def make_album(artist_name, album_name, num_songs=None):
    """Create a dictionary about album information, artist, name, songs"""
    
    # Add required variables to a dictionary
    album = {'artist': artist_name, 'album': album_name}
    
    # Optional num_songs
    if num_songs:
        album['songs'] = num_songs
    
    # Return album dictionary
    return album

# Create 3 albums, one with optional song number
album_0 = make_album('250','PPONG')
album_1 = make_album('Gipsy Kings', 'Mosaique')
album_2 = make_album('Jake Chudnow', 'Prelude To Shona', 23)

# Add to a list
albums = [album_0, album_1, album_2]

# Print album and information related to each album
for album in albums:
    print(album['album']) 
    for key,value in album.items():
        print(f"\t{key.title()}: {value}")


