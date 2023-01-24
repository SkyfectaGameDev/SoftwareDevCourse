print ()

# Initial list creation.
favourite_songs = [
    "Speak - Gates",
    "Source - Fever the Ghost",
    "Lullaby - FC&TR",
    "There's A Reason Why - The Blossoms",
    "Simmer - Hayley Williams"

]
print ("Original List")
print (favourite_songs)
print ()

# Removes specific entry via a string.
favourite_songs.remove("Speak - Gates")
print ("Remove The first song:")
print (favourite_songs)
print ()

# Reverses the list.
favourite_songs.reverse()
print ("Reversing the order:")
print (favourite_songs)
print ()

# Sorts the list alphabetically, or by size when using numbers.
favourite_songs.sort()
print ("Sorts the list:")
print (favourite_songs)
print ()

# Counts the entries in the list
favourite_songs.count(3)
print ("Counts how many times 'Simmer - Hayley Williams' appears:")
print (favourite_songs.count("Simmer - Hayley Williams"))
print ()

# Extend adds one list on to the end of another.
extra_songs = [
    "There's A Honey - Pale Waves",
    "In Camera - Yumi Zouma"
]
favourite_songs.extend(extra_songs)
print ("Extends the list:")
print (favourite_songs)
print ()

# Finding the position of specific songs through the index method
source = favourite_songs.index("Source - Fever the Ghost")
print ("Locating 'Source - Fever the Ghost': ")
print (source)
print()