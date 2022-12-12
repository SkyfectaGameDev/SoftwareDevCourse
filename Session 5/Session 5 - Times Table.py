print ()
print ("Times Tables: ")
print ()

multiply = 1

while multiply < 13:
    for i in range(1, 13):
        print (f"{multiply} x {i} = {multiply * i}")
    multiply +=1
    print ()