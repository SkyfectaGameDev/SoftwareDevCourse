import random

a = 1
b = 2

if a == 1:
    print ("Hello")
else:
    print ("Goodbye")
# A double equals symbol means that you are comparing whether the two values are equal.

music = "classical"
if music == "classical":
    print ("Oh no it's that classical again")
elif music == "no music":
    print ("Arh, peace and quiet")
else:
    print ("Nice and Noisy")
# "elif" is simply short for else if, and looks for another option before moving on to "else".

a = 3
b = 4
c = 5

if b > a:
    print ("B is greater than A")
if c >= a:
    print ("C is greater or equal to A")
if a < c:
    print ("A is less than C")
if b <= c:
    print ("B is less or equal to C")
# These operators compare values in different ways.

age = random.randint(10, 30)
country = "UK"

print (f"You are {age} years old.")
print (f"Your home country is: {country}.")
if age > 17 and country.upper() == "UK":
    print ("You are old enough for the UK's age laws.")
elif age > 17 and country.upper() != "UK":
    print ("What country are you from?")
else:
    print ("You are not old enough for the UK's age laws.")
# Here we are checking if the person is at least 18 years old and from the UK. We are also forcing the UK text to be uppercase, so even if it was typed in lowercase, it will still recognise it.

day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print ("It's the weekend!")
else:
    print ("When's the weekend?")
# This is an example of an "or" statement

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
print ()
print ()
print ()
# Begin boiling kettle
# Open cup cupboard
# Get cup out
# Open tea cupboard
# Open the teabag box
# Get teabag out
# Put the teabag in the cup
# Close the teabag box
# Return teabags to cupboard
# Close the cupboard
# Drape the teabag strong over the cup's edge
# Open the spoon drawer
# Grab the teaspoon
# Close the spoon drawer
# Open the sugar cupboard
# Grab the sugar
# Open the sugar jar
# Scoop teaspoon of sugar no.1
# Put the sugar in the cup
# Scoop teaspoon of sugar no.2
# Put the sugar in the cup
# close sugar jar
# Return sugar to cupboard
# Close the cupboard
# Pick up the kettle
# Pour the water out of the kettle and into the cup
# Put the kettle down
# Stir the tea
# Open the fridge
# Grab the milk
# Unscrew the cap
# Pour into the cup
# Screw the cap back on
# Return milk to fridge
# Close fridge door
# Stir cup again
# Put the teaspoon into the sink
# Pick Up the cup of fresh tea
# Blow tea to cool
# begin drinking the tea
# Enjoy the tea
# Finish the tea
# Say "Aaah, I needed that"
# Put the empty cup into the sink

def say_hello():
    print ("Hello!")

say_hello()
# This is an example of a simple function and calling it.

def cash_withdrawal(amount, accnum):
    print ("Withdrawing {} from account {}".format(amount, accnum))

cash_withdrawal(300, 50449921)
# An example of a more complex function

def say_something(something):
    print ("{}".format(something))

say_something("Hello!")
say_something("Goodbye.")
# An example of a function producing different outcomes thanks to using different parameters.

w_amount = 100
account_num = 12345678

def cash_withdrawal(amount, accnum):
    print (f"Withdrawing {amount} from account {accnum}")

cash_withdrawal(w_amount, account_num)
# An example of using global variables within a function.

def add_up(num1, num2):
    return num1 + num2

add_up(7,3)
print(add_up(2,5))
# Assigning the parameters outside of the function the moment you call it.

def multiply_by_nine_fifths(celsius):
    return celsius * (9/5)

def get_fahrenheit(celsius):
    returned_val = multiply_by_nine_fifths(celsius)     # Assigns the returned value to a variable.
    print ("The returned value is:", returned_val) 
    return returned_val + 32                            # Adds 32 to the original value, and returns the new value to print.
print (get_fahrenheit(50))