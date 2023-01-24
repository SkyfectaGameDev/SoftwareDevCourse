import random
print ()

# An example of a While Loop.
num = 0

while num < 10:
    num += 1
    print (num)

print ()

# An example of a more advanced While Loop.
rand_num = random.randint(0, 50)
my_num = 50
total_searches = 0

while rand_num != my_num:
    total_searches += 1
    print (rand_num)
    rand_num = random.randint(0, 50)

print (f"After {total_searches} searches, you've found {my_num}!")
print ()