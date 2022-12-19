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
num = 1001
num_string = str(num)
num_reverse = num_string[::-1]
if num_string == num_reverse:
    print(f"The number {num} is a palindrome!")
else:
    print(f"The number {num} is NOT a palindrome!")

# Activity 8
def coffee_order(size, drink_type):
    print (f"You have ordered a {size} {drink_type}.")

coffee_order("Large", "Chai Latté")
coffee_order("Small", "Mocha")
coffee_order("Medium", "Cappuccino")

# ---------------------------------------- Part 2 ----------------------------------------

# Activity 1
order_count = 1
def take_order(topping1, topping2, topping3):
    global order_count
    print (f"Order number {order_count} is a pizza with {topping1}, {topping2} and {topping3} on it.")
    order_count += 1

take_order("Pepperoni", "Chicken", "Sausage")
take_order("Peppers", "Onion", "Sweetcorn")
take_order("Ham", "Mushroom", "Beef")

# Activity 2
def cash_machine(pin_number, amount):
    if pin_number != 1234:
        print ("Incorrect pin number.")
    elif pin_number == 1234 and amount <= 350 :
        print (f"You have successfully withdrawn £{amount}. You have £{350 - amount} remaining in your bank account.")
    else:
        print ("You lack the sufficent funds for this withdrawal.")
    
cash_machine (4321, 250)
cash_machine (1234, 250)
cash_machine (1234, 400)