import datetime

# Activity 1
password = "PasswordIsABadPassword"

print ("Password Length:", len(password))
if len(password) < 8:
    print ("Password is too short.")
else:
    print (password)

# Activity 2
num = 9
print (f"Your number is {num}.")

if num %3 == 0 or num %5 == 0:
    print ("This number is divisible by either 3 or 5.")

# Activity 3
num = 21
print (f"Your new number is {num}.")

if num %3 == 0 and num %7 == 0:
    print ("Fizz Buzz")
elif num %7 == 0:
    print ("Buzz")
elif num %3 == 0:
    print ("Fizz")
else:
    print ("Not divisible by 7")

# Activity 4
word = "Window"
word_length = len(word)
print (f"Your word is {word}.")
print (f"Your word is {word_length} characters long.")

if word.upper()[0] == word.upper()[word_length - 1]:
    print (f"The last letter of {word} is the same as the first.")

# Activity 5
time = datetime.time(8)
place_of_work = datetime.time(9)
town_of_home = datetime.time(7)

if time <= town_of_home:
    print (f"The time is {time}, which means that you will be at home.")
elif time >= place_of_work:
    print (f"The time is {time}, which means that you will be at work.")
else:
    print (f"The time is {time}, which means that you will be commuting to work.")

# Activity 6
num1 = 12
num2 = 17
result = num1 + num2

if result %2 == 0:
    print (f"You have added {num1} and {num2} together. Your result is {result}, which is an even number.")
else:
    print (f"You have added {num1} and {num2} together. Your result is {result}, which is an odd number.")

# Activity 7