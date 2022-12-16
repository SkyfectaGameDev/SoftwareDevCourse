from time import sleep

blind_gargoyles = False

def tower_title():
    print("                                                   o                    ")
    print("                                               _---|         _ _ _ _ _ ")
    print("                                            o   ---|     o   ]-I-I-I-[ ")
    print("                           _ _ _ _ _ _  _---|      | _---|    \ ` ' / ")
    print("                           ]-I-I-I-I-[   ---|      |  ---|    |.   | ")
    print("                            \ `   '_/       |     / \    |    | /^\| ")
    print("                             [*]  __|       ^    / ^ \   ^    | |*|| ")
    print("                             |__   ,|      / \  /    `\ / \   | ===| ")
    print("                          ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|")
    print("                          I_I__I_I__I_I  (====(_________)___|_|____|____")
    print("                          \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_| ")
    print("                           |[]      '|   | []  |`__  . [  \-\--|-|--/-/  ")
    print("                           |.   | |' |___|_____I___|___I___|---------| ")
    print("                          / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] | ")
    print("                         <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \  ")
    print("                         ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===> ")
    print("                         ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [ ")
    print("                         <===>     ' ||||| |   |   | ||||.||  []   <===>")
    print("                          \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/ ")
    print("                           |      . _||||| |   |   | ||||.|| |     | |")
    print("                        ../|' v . | .|||||/____|____\|||| /|. . | . ./")
    print("                        .|//\............/...........\........../../\\\ ")
    print("_______________________________________________________________________________________________________")
    print("   ______                                                                                               ")
    print("    /       /                                           /                                              ")
    print("---/-------/__-----__---------__-----__----__---_/_----/-----__-------_/_-----__-------------__----)__-")
    print("  /       /   )  /___)      /   '  /   )  (_ `  /     /    /___)      /     /   ) | /| /   /___)  /   )")
    print("_/_______/___/__(___ ______(___ __(___(__(__)__(_ ___/____(___ ______(_ ___(___/__|/_|/___(___ __/_____")

tower_title()

def what_do():
    print("[1]Examine tapestry")
    print("[2]Examine throne")
    print("[3]Examine gargoyles")

def gargoyle_choice():
    print("[10]Tie bow")
    print("[9]Give scarf")
    print("[8]Cover eyes")

def tower_dialogue_1():
    print("Name decides to search for the Heir's crown.")
    print("")
    print("\033[1;33m'It is located in the central tower. But there's no way to access it... You will have to search the throne room while the Heir is away.'\033[0m")
    print("...")
    print("\033[1;33m'Luckily for us they are out of town today- royal duties to attend. Should give us plenty of time.'\033[0m")
    print("...")
    print("\033[1;33m'Let us proceed with caution... No doubt the crown will be heaviy guarded. We must keep our wits about us.'\033[0m")
    print("")
    print("And with that, Name makes their way to the throne room. It feels eerily quiet...")
    print("")
    print("\033[1;33m'The castle used to be bustling with life. Yet over the years members of the staff have slowly disappeared one by one, and gargoyles startred to appear.'\033[0m")
    print("")
    print("\033[1;33m'I was powerless to assist until you came of age. When you were swapped the demon put a seal on me which prevented me from making myself known...'\033[0m")
    print("")
    print("\033[1;33m'But my power is your power. Now that you're older, and your father is in danger, you have given me the strength to overcome the seal and help you cleanse the evil that plagues this realm.'\033")
    print("...")
    print("\033[1;33m'Your father had me bound to your soul before you were even born. He must have known someone was out to get him, and wanted to protect you.'\033[0m")
    print("...")
    print("\033[1;33m'Anyway, I've rambled long enough. Let's find that crown.'\033[0m")
    print("")
    print("Name looks around the throne room, examining it's structure. ")
    print("")
    print("The throne sits proudly on elevated steps, the whole room making way for it's presence. ")
    print("")
    print("Behind it hangs a tapestry depicting an angel losing in battle to a basilisk. It used to depict his triumph, but now it feels as though it's there to mock your efforts.")
    print("")
    print("There are also four gargoyles positioned against the walls flanking the throne, with stained glass windows in-between that fill the room with glowing imprints of many frightening creatures.")
    print("")
    what_do()
    decision = int(input("What will you do ? "))
    if decision == 1:
        examine_tapestry()
    elif decision == 2:
        examine_throne()
    elif decision == 3:
        examine_gargoyles()
    
def examine_throne():

        print("You examine the throne...")
        print("...")
        print("Upon closer inspection, you see a message ingraved into the back of the throne which reads:")
        print("")
        print(                           "Eight eyes confirm my fate")
        print(                         "A battle lost, I turn to stone")
        print(                        "If they don't see my fate to be:")
        print(                          "I reclaim my rightful throne")
        print("")
        print("'A clue...'")
        what_do()
        decision = int(input("What will you do ? "))
        if decision == 1:
                examine_tapestry()
        elif decision == 2:
                examine_throne()
        elif decision == 3:
                examine_gargoyles()

def examine_gargoyles():
        global blind_gargoyles  
        print("You take a closer look at each of the gargoyles...")
        print("...")
        print("You notice that each one holds a strip of fabric in it's maw.")
        print ("What will you do ? ")
        gargoyle_choice()
        decision = int(input("What will you do ? "))
        if decision == 8:
            blind_gargoyles = True
            print("You cover the eyes of each gargoyle using the fabric from its maw. A rumbling sound can be heard from behind the throne.")
            what_do()
            decision = int(input("What will you do ? "))
            if decision == 1:
                examine_tapestry()
            elif decision == 2:
                examine_throne()
            elif decision == 3:
                examine_gargoyles()
        elif decision == 9:
            print("You take the fabric from between the gargoyle's teeth and wrap it around the gargoyles neck in a scarf-like fashion. If it weren't a gargoyle you could almost say it looks cute. ")
            print("")
            print("'I don't think that's gonna work.'")
            what_do()
            decision = int(input("What will you do ? "))
            if decision == 1:
                examine_tapestry()
            elif decision == 2:
                examine_throne()
            elif decision == 3:
                examine_gargoyles()
        elif decision == 10:
            print("You take the fabric and tie it into a cute bow o the gargoyles head. It looks much less scary now.")
            print("")
            print("'Very cute, but I don't think that's gonna work.'")
            what_do()
            decision = int(input("What will you do ? "))
            if decision == 1:
                examine_tapestry()
            elif decision == 2:
                examine_throne()
            elif decision == 3:
                examine_gargoyles()
        else:
            print("Please input a valid option.")
            what_do()
            decision = int(input("What will you do ? "))
            if decision == 1:
                examine_tapestry()
            elif decision == 2:
                examine_throne()
            elif decision == 3:
                examine_gargoyles()

def enter_tower():
    print("")

def examine_tapestry():
    #check_tapestry = "Examine Tapestry ? yes/no "
    if  blind_gargoyles == True:
            print("You examine the tapestry...")
            print("...")
            print("You can see that it is extremely detailed. No doubt the heir had it specially made along with the stained glass windows to strike fear into those who dare oppose their rule. It depicts angel losing in battle against a basilisk.")
            print("...")
            print("You peek behind the tapestry.")
            print("...")
            print("And find that the wall has sunken into the ground, revealing a spiralling stairway leading up to where the crown is held: the previously inaccessible central tower.")
            print("FUNCTION TO PROCEED")

    elif blind_gargoyles == False:
         print("You examine the tapestry...")
         print("...")
         print("You can see that it is extremely detailed. No doubt the heir had it specially made along with the stained glass windows to strike fear into those who dare oppose their rule.")
         print("...")
         print("You peek behind the tapestry.")
         print("...")
         print("But it's just an empty wall.")
    else:
        print("Please input a valid response.")



tower_dialogue_1()






  


            
    
