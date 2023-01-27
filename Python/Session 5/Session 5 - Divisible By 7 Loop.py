import random
print ()

num_generator   = 0
div_check       = 0

print ("Generating six numbers...")
while num_generator < 6:
    num_generator += 1
    div_check = random.randint(0, 30)
    if div_check %7 == 0:
        print (f"{div_check} is dividible by 7!")
    else:
        print (f"{div_check} is not dividible by 7.")
