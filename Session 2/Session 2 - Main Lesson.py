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