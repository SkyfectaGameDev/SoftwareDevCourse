
coffee_is_grinding = False

def press_grind_beans():
    global coffee_is_grinding
    if coffee_is_grinding:
        print("Stopping the grind.")
        coffee_is_grinding = False
    else:
        print ("Starting the grind.")
        coffee_is_grinding = True

press_grind_beans() # The coffee is not grinding
press_grind_beans() # The coffee isgrinding