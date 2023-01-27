from random import random, randint, uniform
# This imports the methods random, randint and uniform from the random library. You can put only "import random" to use the full library.

print ("hello world")
# This code prints the string "hello world".

print ("Character Number"[5])
print ("uppercase".upper())
print ("lowercase".lower())
print ("   Strip".strip())

print ("capitalize".capitalize())
print ("hello".count("l"))
print ("hello".find("e"))
print ("hello".replace("hello","goodbye"))

print (random())
#print (random.random())
# Prints a random float - the method "random" returns a floating point between 0 and 1.

print (uniform(1, 10))
#print (random.uniform(1, 10))
# Prints a random float between 1 and 10 - the method "uniform" returns a floating point between two parameters.

print (randint(1, 10))
#print (random.randint(1, 10))
# Prints a random integer between 1 and 10 - the method "randint" returns a integer between two parameters.

print ("   |   |   \n   |   |   \n   |   |   \n-----------\n   |   |   \n   |   |   \n   |   |   \n-----------\n   |   |   \n   |   |   \n   |   |   ")
# Including "\n" within the quotation marks of a string will create a new line within the text.

print ("All Around the World"[7].upper())
# Finding the 8th character and making it uppercase.

my_name = "Alisha"
my_age  = 21
student = True
fav_drink = "Iced Tea"
# Always use Snake Case in Python.

print ("My name is", my_name, "and I am", my_age, "years old.")
# You can combine multiple data types in print and construct a sentance that way.

print ("{}'s favourite drink is {}".format(my_name, fav_drink))
print (f"{my_name}'s favourite drink is {fav_drink}")
# There are different ways to format text.

print ('{}\'s favourite drink is {}'.format(my_name, fav_drink))
# A backslash will prevent the string from ending when using the same quotation marks as the ones holding the string.

print ("Addition:",         5 + 5)
print ("Subtraction:",      8 - 5)
print ("Multiplication:",   3 * 4)
print ("To the Power:",      3 ** 3)
print ("Division:",         9 / 3)
print ("Remainder:",        17 % 2)

value = 10
print ("New Value:", value)
value += 3
print ("Plus Three:", value)
value *= 2
print ("Multiplied by Two:", value)
value /= 3
print ("Divided by Three:", value)
value -= 5
print ("Minus Five:", value)
print ()