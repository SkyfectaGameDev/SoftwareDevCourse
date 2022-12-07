
# --- Activity 1 ---
name        = input ("Please input your name: ")
age         = input ("Please input your age: ")
fav_food    = input ("Please input your favourite food: ")

print (f"Hello, {name}. You are {age} years old and your favourite food is {fav_food}.")

# --- Activity 2 ---
def cash_machine(pin_number, amount):
    pin_number = int(input("Please enter your pin number: "))

    if pin_number == 1234:
        amount = int(input("Account Balance: £350. Please enter the amount you wish to withdraw: "))

        if amount <= 350 :
            print (f"You have successfully withdrawn £{amount}. You have £{350 - amount} remaining in your bank account.")
        else: 
            print ("Insufficient funds.")
    else:
        print ("Incorrect pin number.")
cash_machine(0, 0)






# Create a maths test in a function, Name, Age, 5 questions, score. 5 Students, rank them.