
coffee_is_grinding = False

def press_grind_beans():
    global coffee_is_grinding           # This reads the value of "coffee_is_grinding", which starts in the False state (off).
    if coffee_is_grinding:              
        print("Stopping the grind.")
        coffee_is_grinding = False      # If the "coffee_is_grinding" is True (on), then it turns to False (off).   
    else:
        print ("Starting the grind.")   # If the "coffee_is_grinding" is False (off), then it turns to True (on).   
        coffee_is_grinding = True       

press_grind_beans()                     # The coffee is not grinding.
press_grind_beans()                     # The coffee is grinding.