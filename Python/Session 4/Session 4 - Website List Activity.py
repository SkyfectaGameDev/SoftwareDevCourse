print ()

# Creating the original list
fav_websites = [
    "YouTube",
    "Twitter",
    "GitHub"
]

# Printing the original list
print ("My Favourite Websites: ")
print (fav_websites)
print ()

# Using input to create two more websites.
extra_website_1 = input ("Enter extra website #1: ")
extra_website_2 = input ("Enter extra website #2: ")
print()

# Compiling them into an extra list
extras_list = [
    extra_website_1,
    extra_website_2
]

# Adding the extras onto the original list.
fav_websites.extend(extras_list)
print (fav_websites)
print ()

# Removing the final entry
fav_websites.pop()
print (fav_websites)
print ()