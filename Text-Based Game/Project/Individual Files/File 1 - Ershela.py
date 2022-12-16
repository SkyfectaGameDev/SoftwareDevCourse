print()

def guardian_title():
                          
    print("                                  _)\.-.")
    print("                 .-.__,___,_.-=-. )\`  a`\_")
    print("             .-.__\__,__,__.-=-. `/  \     `\  ")
    print("             {~,-~-,-~.-~,-,;;;;\ |   '--;`)/")
    print("              \-,~_-~_-,~-,(_(_(;\/   ,;/")
    print("               ',-.~_,-~,-~,)_)_)'.  ;;(")
    print("                 `~-,_-~,-~(_(_(_(_\  `;\  ")
    print("           ,          `'~~--,)_)_)_)\_   \ ")
    print("           |\              (_(_/_(_,   \  ;")
    print("           \ '-.       _.--'  /_/_/_)   | |")
    print("            '--.\    .'          /_/    | |")
    print("                ))  /       \      |   /.'")
    print("               //  /,        | __.'|  ||")
    print("              //   ||        /`    (  ||")
    print("             ||    ||      .'       \ \\")
    print("             ||    ||    .'_         \ \\")
    print("              \\   //   / _ `\        \ \\__")
    print("               \'-'/(   _  `\,;        \ '--:,")
    print("                `'`  `'` `-,,;         `'',,;")
    print(" ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ ██╗ █████╗ ███╗   ██╗")
    print("██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗██║██╔══██╗████╗  ██║")
    print("██║  ███╗██║   ██║███████║██████╔╝██║  ██║██║███████║██╔██╗ ██║")
    print("██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║██║██╔══██║██║╚██╗██║")
    print("╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝██║██║  ██║██║ ╚████║")
    print(" ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝")
    print()

guardian_title()

# task 1 (feed the dogs morning)
print (f"TASK 1\nIt's 7AM, time for breakfast!\nWould you like to feed the dogs and throw a toy for them to play, while you are preparing their food? YES\nWould you like to feed the dogs normally? NO")
task1 = input ()
if task1 == "yes":
    print("Dogs are playing with the toy while the bowl is filled ")
if task1 == "no":
    print ("You feed the dogs normally and now they are all happy")
input("Press enter to continue")


#task 2 (clean the chimney)
bond_points = 0
print (f"TASK 2\nClean chimney: wet wood. Yes/No")
task1 = input ()
if task1 == "yes":
    print("Fire doesnt light so we are all good, you got an extra BP  ")
    game_points = + 1
    print (f"+ {game_points} BP")
if task1 == "no":
    print ("someone strarts a fire")
input("Press enter to continue")


# task 3 (sort the library)
print (f"TASK 3\nSort out the library!")
task1 = input ()
if task1 == "yes":
    print("Exellent, now learn about carn plants ")
    game_points = + 1
    print (f"+ {game_points} BP")
if task1 == "no":
    print ("you didn't learn anything")
input("Press enter to continue")

# task 4 (feed the dogs evening)
bond_points = 0
print (f"TASK 4\nIt's dinner time!\nWould you like to feed the dogs and throw a toy at them? Yes/No")
task1 = input ()
if task1 == "yes":
    print("Great news, you got an extra BP & dogs destroy toy -- human knows not to approach ")
    game_points = + 1
    print (f"+ {game_points} BP")
if task1 == "no":
    print ("Dogs are attacking")