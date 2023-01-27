# An example of a list of strings.
coffee_order = [
    "Alex - Cortado",
    "Ben - Latte",
    "Charlie - Whatever's New"
]
print (coffee_order)
print (coffee_order[2])
# Just like strings, you can pick out a position in the list.
coffee_order[1] = "Ann - Vanilla Latte"
print (coffee_order)
# Just like strings, you can retrieve the length of a list.
print (len(coffee_order))
# The append method adds another entry to the end of the list.
coffee_order.append("Donna - Espresso")
print (coffee_order)
# The pop method removes the final list entry.
coffee_order.pop()
print (coffee_order)
# You can also pop a specific position by putting the position number in the brackets.
coffee_order.pop(1)
print (coffee_order)
# You can also insert an entry into any position you want, too.
coffee_order.insert(1, "Ben - Latte")
print (coffee_order)
print ()
print ()
print ()

# ----- Moving on to For & While Loops -----
# Creating a list of drinks.
fav_drinks = [
    "Coke",
    "Fanta",
    "Tonic"
]

# For each drink that is in the fav_drinks list, it will print its name.
for i in fav_drinks:
    print (i)
print ()

# Using a range instead of a list will print 10 numeral positions from 0.
for i in range(10):
    print(i)
print ()

# Printing a range between 5 and15, however to include the actual result of 15, I put 16 instead.
for i in range (5, 16):
    print(i)
print ()

# Printing a range between 0 and 10 but jumping up in 3's.
for i in range (0, 10, 2):
    print(i)
print ()