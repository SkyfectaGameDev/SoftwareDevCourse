import os
import time
import random

#region -------------------------------------------------------------------------------- SECTION 1 - BEGINNING --------------------------------------------------------------------------------
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

bond_points = 0
name = input ("What is your name? ")

# task 1 (feed the dogs morning)
def task1():
    print (f"TASK 1\nIt's 7AM, time for breakfast!\nWould you like to feed the dogs and throw a toy for them to play, while you are preparing their food? YES\nWould you like to feed the dogs normally? NO")
    task1 = input ()
    if task1.lower() == "yes":
        print("Dogs are playing with the toy while the bowl is filled ")
    if task1.lower() == "no":
        print ("You feed the dogs normally and now they are all happy")
    input("Press enter to continue")


#task 2 (clean the chimney)
def task2():
    print (f"TASK 2\nClean chimney: wet wood. Yes/No")
    task1 = input ()
    if task1.lower() == "yes":
        print("Fire doesnt light so we are all good, you got an extra BP  ")
        game_points = + 1
        print (f"+ {game_points} BP")
    if task1.lower() == "no":
        print ("Someone starts a fire, engulfing you in flames - ending your journey before it could even begin.")
        death_choice = input ("Would you like to try again? (Yes/No)")
        if death_choice.lower() == "yes":
            task2()
        else:
            print()
            print("Your fate is sealed, never to return to this world.")
            quit()

    input("Press enter to continue")


# task 3 (sort the library)
def task3():
    print (f"TASK 3\nSort out the library! (Yes/No)")
    task1 = input ()
    if task1.lower() == "yes":
        print("Exellent, now learn about carn plants ")
        game_points = + 1
        print (f"+ {game_points} BP")
    if task1.lower() == "no":
        print ("you didn't learn anything")
    input("Press enter to continue")

# task 4 (feed the dogs evening)
def task4():
    print (f"TASK 4\nIt's dinner time!\nWould you like to feed the dogs and throw a toy at them? Yes/No")
    task1 = input ()
    if task1.lower() == "yes":
        print("Great news, you got an extra BP & dogs destroy toy -- human knows not to approach ")
        game_points = + 1
        print (f"+ {game_points} BP")
    if task1.lower() == "no":
        print ("Dogs are attacking")

task1()
task2()
task3()
task4()

#endregion


#region -------------------------------------------------------------------------------- SECTION 2 - THE CELLAR --------------------------------------------------------------------------------

# define directions
dir_none = 0
dir_north = 8
dir_west = 4
dir_east = 2
dir_south = 1


# defineof walls (8=north/4=west/2=east/1=south/0=none)
wall_north = 8
wall_west = 4
wall_east = 2
wall_south = 1
wall_none = 0
#walls = [wall_north, wall_west, wall_east, wall_south, wall_none]


# map tiles
tile1 = 1           #south
tile2 = 2           #east
tile3 = 3
tile4 = 4           #west
tile5 = 5
tile6 = 6
tile7 = 7
tile8 = 8           #north
tile9 = 9
tile10 = 10
tile11 = 11
tile12 = 12
tile13 = 13
tile14 = 14
tile15 = 15


# map sizing
map_sizex = 5
map_sizey = 5


# cell size
cell_sizex = 5
cell_sizey = 3


# player position
plyr_posx = 0
plyr_posy = 4
target_posx = 4
target_posy = 0


# define 1 x 5  roooms
group0 = [12, 9, 9, 9, 10]
group1 = [5, 8, 9, 9, 10]
group2 = [12, 1, 9, 10, 6]
group3 = [6, 13, 10, 6, 6]
group4 = [5, 11, 5, 1, 3]


# define 5 x 5  maze
cellar = []


# define menu
menu = {}
menu_text_length = 0
game_started = False
winner = False


def initialise_cellar():
    # Debug
    #print("\n[Function: initialise_cellar()]")
    global group0
    global group1
    global group2
    global group3
    global group4
    global celler
    # Process - Joins 5 separate 1x5 rooms arrays into a 5x5 maze
    cellar.extend(group0)
    cellar.extend(group1)
    cellar.extend(group2)
    cellar.extend(group3)
    cellar.extend(group4)
    #print(f"Group0: {group0}")
    #print(f"Group1: {group1}")
    #print(f"Group2: {group2}")
    #print(f"Group3: {group3}")
    #print(f"Group4: {group4}")
    #print(f"Cellar: {cellar}")
#end of function def


def show_intro_message():
    global menu
    global menu_text_length
    os.system("cls")
    print("\n\nThe Cellar.")
    print("============")
    print("As soon as you step into the cellar, you find that your fear's were true, and the cellar is really a labrynth of many rooms.\n")
    print("You realise that to finish your quest, you must negoiate the labrynth.\n")
    print("So you stiffen your resolve and get down to the business of negoitaing the maze of rooms.\n\n")
    print("Labrynth Instructions.")
    print("=======================")
    print("You will be presented with a maze puzzle.")
    print("Your locationa is indicated by an '@' symbol.")
    print("The exit is marked with an 'X' symbol.")
    print("Negotiate the labrynth of rooms to continue on your quest...\n\n")
    print("Decision.")
    print("=======================")
    print("Choose whether you wish to go on or quit before you even started!!!\n")
    
    # clear menu
    menu.clear()
    #room_value = room_type
    menu_text_length = 0

    # Enter
    menu_text = "Enter the maze - I mean how difficut can it be? right?"
    text_length = len(menu_text)
    if text_length > menu_text_length:
        menu_text_length = text_length
    #end of if
    menu_add("E", menu_text)

    # Exit
    menu_text = "I don't know if I can do it or not, so I won't risk it..."
    text_length = len(menu_text)
    if text_length > menu_text_length:
        menu_text_length = text_length
    #end of if
    menu_add("X", menu_text)
#end of function def


def roomtype_for(style, tilenum):
    global plyr_posx
    global plyr_posy
    global map_sizey
    global cellar
    room_type = 0
    if style == "MapSquare":
        room_type = cellar[tilenum]
    elif style == "PlayerPos":
        posz = (plyr_posy * map_sizey) + plyr_posx 
        room_type = cellar[posz]
    #end of if 
    return room_type
#end of function def


def display_cell_layer(mapx, mapy, layer):
    global plyr_posx
    global plyr_posy
    global map_sizey
    
    posz = (mapy * map_sizey) + mapx 
    room_type = roomtype_for("MapSquare", posz)
    #print (f"[SqId: {posz}][RoomType: {room_type}]")

    # Are we here yet?
    u_are_here = False
    if (layer == 1) and (mapx == plyr_posx) and (mapy == plyr_posy):
        u_are_here = True
        #end of if
    #end of if 
    # Render room slice
    string = get_room_layer_string(room_type, layer, u_are_here, mapx, mapy)
    return string
#end of function def


def display_map():
    global map_sizey
    global map_sizex
    global cell_sizey

    # Process
    for tiley in range(map_sizey):
        if (tiley >= 0) and (tiley <= 2):
            for layer in range(0, 2):
                string = ""
                for tilex in range(map_sizex):
                    #print(f"[MapY: {tiley}][MapX: {tilex}][Layer: {layer}]")
                    string = string + display_cell_layer(tilex, tiley, layer)
                #end of for
                #print(string)
                print(string)
            #end of for
        elif tiley == 3:
            for layer in range(cell_sizey):
                string = ""
                for tilex in range(map_sizex):
                    #print(f"[MapY: {tiley}][MapX: {tilex}][Layer: {layer}]")
                    string = string + display_cell_layer(tilex, tiley, layer)
                #end of for
                #print(string)
                print(string)
            #end of for
        elif tiley == 4:
            for layer in range(1, 3):
                string = ""
                for tilex in range(map_sizex):
                    #print(f"[MapY: {tiley}][MapX: {tilex}][Layer: {layer}]")
                    string = string + display_cell_layer(tilex, tiley, layer)
                #end of for
                #print(string)
                print(string)
            #end of for
        #end of if
    #end of for

    # WORKING CODE BUT MESSY MAP
    #for tiley in range(map_sizey):
    #    for layer in range(cell_sizey):
    #        string = ""
    #        for tilex in range(map_sizex):
    #            #print(f"[MapY: {tiley}][MapX: {tilex}][Layer: {layer}]")
    #            string = string + display_cell_layer(tilex, tiley, layer)
    #        #end of for
    #        #print(string)
    #        print(string)
    #    #end of for
    #end of for
#end of fuunction def


def get_room_layer_string(room_type, layer, is_here, mapx, mapy):
    # Debug
    #print("\n[Function: build_room_slice_array()]")
    #print(f"RoomType: {room_type}")
    #print(f"Layer: {layer}")

    # Globals
    global map_sizex
    global cell_sizex
    global target_posx
    global target_posy
   
    # Process
    data = ""

    #print(mid_point) 
    if (room_type == 15):
        if (layer == 0) or (layer == 2):
            data = "#####"
        elif (layer == 1):
            if is_here:
                data = "# @ #"
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "# X #"
            else:
                data = "#   #"
            #end of if
        else:
            data = "....."
        #end of if

    elif (room_type == 14):
        if (layer == 0):
            data = "#####"
        elif (layer == 1):
            if is_here:
                data = "# @ #"
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "# X #"
            else:
                data = "#   #"
            #end of if
        elif (layer == 2):
            data = "#   #"
        else:
            data = "....."
        #end of if

    elif (room_type == 13):
        if (layer == 0) or (layer == 2):
            data = "#####"
        elif (layer == 1):
            if is_here:
                data = "# @  "
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "# X  "
            else:
                data = "#    "
            #end of if
        else:
            data = "....."
        #end of if

    elif (room_type == 12):
        if (layer == 0):
            data = "#####"
        elif (layer == 1):
            if is_here:
                data = "# @  "
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "# X  "
            else:
                data = "#    "
            #end of if
        elif (layer == 2):
            data = "#    "
        else:
            data = "....."
        #end of if

    elif (room_type == 11):
        if (layer == 0) or (layer == 2):
            data = "#####"
        elif (layer == 1):
            if is_here:
                data = "  @ #"
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "  X #"
            else:
                data = "    #"
            #end of if
        else:
            data = "....."
        #end of if

    elif (room_type == 10):
        if (layer == 0):
            data = "#####"
        elif (layer == 1):
            if is_here:
                data = "  @ #"
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "  X #"
            else:
                data = "    #"
            #end of if
        elif (layer == 2):
            data = "    #"
        else:
            data = "....."
        #end of if

    elif (room_type == 9):
        if (layer == 0) or (layer == 2):
            data = "#####"
        elif (layer == 1):
            if is_here:
                data = "  @  "
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "  X  "
            else:
                data = "     "
            #end of if
        else:
            data = "....."
        #end of if

    elif (room_type == 8):
        if (layer == 0):
            data = "#####"
        elif (layer == 1):
            if is_here:
                data = "  @  "
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "  X  "
            else:
                data = "     "
            #end of if
        elif (layer == 2):
            data = "     "
        else:
            data = "....."
        #end of if

    elif (room_type == 7):
        if (layer == 0):
            data = "#   #"
        elif (layer == 1):
            if is_here:
                data = "# @ #"
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "  X  "
            else:
                date = "#   #"
            #end of if
        elif (layer == 2):
            data = "#####"
        else:
            data = "....."
        #end of if

    elif (room_type == 6):
        if (layer == 0) or (layer == 2):
            data = "#   #"
        elif (layer == 1):
            if is_here:
                data = "# @ #"
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "# X #"
            else:
                data = "#   #"
            #end of if
        else:
            data = "....."
        #end of if

    elif (room_type == 5):
        if (layer == 0):
            data = "#    "
        elif (layer == 1):
            if is_here:
                data = "# @  "
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "# X  "
            else:
                data = "#    "
            #end of if
        elif (layer == 2):
            data = "#####"
        else:
            data = "....."
        #end of if

    elif (room_type == 4):
        if (layer == 0) or (layer == 2):
            data = "#    "
        elif (layer == 1):
            if is_here:
                data = "# @  "
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "# X  "
            else:
                data = "#    "
            #end of if
        else:
            data = "....."
        #end of if

    elif (room_type == 3):
        if (layer == 0):
            data = "    #"
        elif (layer == 1):
            if is_here:
                data = "  @ #"
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "  X #"
            else:
                data = "    #"
            #end of if
        elif (layer == 2):
            data = "#####"
        else:
            data = "....."
        #end of if

    elif (room_type == 2):
        if (layer == 0) or (layer == 2):
            data = "    #"
        elif (layer == 1):
            if is_here:
                data = "  @ #"
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "  X #"
            else:
                data = "    #"
        #end of if
        else:
            data = "....."
        #end of if

    elif (room_type == 1):
        if (layer == 0):
            data = "     "
        elif (layer == 1):
            if is_here:
                data = "  @  "
            elif (mapx == target_posx) and (mapy == target_posy):
                data = "  X  "
            else:
                data = "     "
            #end of if
        elif (layer == 2):
            data = "#####"
        else:
            data = "....."
        #end of if

    elif (room_type == 0):
            data = "....."
    #end of if
    return data
#end of function def


def menu_add(menu_key, menu_text):
    global menu_text_length
    # existss?
    old_value = menu.get(menu_key, "")
    if (old_value != ""):
        menu.pop(menu_key)
    #end of if
    text_length = len(menu_text)
    if text_length > menu_text_length:
        menu_text_length = text_length
    #end of if
    menu.update({menu_key : menu_text})
#end of function def


def set_room_doors_menu(room_type):
    global menu
    global plyr_posx
    global plyr_posy
    global dir_north
    global dir_west
    global dir_east
    global dir_south
    global menu_text_length

    # clear menu
    menu.clear()
    #room_value = room_type
    menu_text_length = 0

    # north
    if room_type >= 8:
        # has_north_door = False
        room_type = room_type - dir_north
    else:
        if plyr_posy > 0:
            menu_text = "Walk through the North wall doorway"
            text_length = len(menu_text)
            if text_length > menu_text_length:
                menu_text_length = text_length
            #end of if
            menu_add("N", menu_text)
        else:
            print("You are at the edge of the labrynth and cannot go in that direction (North).")
        #end of if
    #end of if

    # West
    if room_type >= 4:
        # has_west_door = False
        room_type = room_type - dir_west
    else:
        if plyr_posx > 0:
            menu_text = "Walk through the West wall doorway"
            text_length = len(menu_text)
            if text_length > menu_text_length:
                menu_text_length = text_length
            #end of if
            menu_add("W", menu_text)
        else:
            print("You are at the edge of the labrynth and cannot go in that direction (West).")
        #end of if
    #end of if

    # East
    if room_type >= 2:
        # has_east_door = False
        room_type = room_type - dir_east
    else:
        if plyr_posx < 4:
            menu_text = "Walk through the East wall doorway"
            text_length = len(menu_text)
            if text_length > menu_text_length:
                menu_text_length = text_length
            #end of if
            menu_add("E", menu_text)
        else:
            print("You are at the edge of the labrynth and cannot go in that direction (East).")
        #end of if
    #end of if

    # south
    if room_type  >= 1:
        # has_south_door = False
        room_type = room_type - dir_south
    else:
        if plyr_posy < 4:
            menu_text = "Walk through the South wall doorway"
            text_length = len(menu_text)
            if text_length > menu_text_length:
                menu_text_length = text_length
            #end of if
            menu_add("S", menu_text)
        else:
            if game_started == True:
                print("You are at the edge of the labrynth and cannot go in that direction (South).")
            #end of if
        #end of if
    #end of if

    # exit
    menu_text = "I'm bored now and want to quit."
    text_length = len(menu_text)
    if text_length > menu_text_length:
        menu_text_length = text_length
    #end of if
    menu_add("X", menu_text)
    #end of if
#end of function def


def show_menu():
    #menu_title = "[>      ====    Options Menu      ====    <]"
    #print(f"{menu_tite}\n")
    if (len(menu)) > 0:
        keys = list((menu.keys()))
        #print(f"Keys: {keys}")
        for i in range(len(menu)):
            print (f"[ {keys[i]} ] - {menu.get(keys[i])}\n")
        #end of for
    else:
        print("Menu is empty!")
    #end of if
#end of function def


def move_player(direction):
    global plyr_posx
    global plyr_posy
    global target_posx
    global target_posy
    global winner
    winner = False
    if direction == "N":
        plyr_posy = plyr_posy - 1
    elif direction == "W":
        plyr_posx = plyr_posx - 1
    elif direction == "E":
        plyr_posx = plyr_posx + 1
    elif direction == "S":
        plyr_posy = plyr_posy + 1
    #end of if
    #reached destination check
    if plyr_posx == target_posx and plyr_posy == target_posy:
        winner = True
    #end of if
#end of function def


def get_room_exits(roomtype):
    if roomtype == 0:
        tmp = ["N","W","E","S"]
    elif roomtype == 1:
        tmp = ["N","W","E"]
    elif roomtype == 2:
        tmp = ["N","W","S"]
    elif roomtype == 3:
        tmp = ["N","W"]
    elif roomtype == 4:
        tmp = ["N","E","S"]
    elif roomtype == 5:
        tmp = ["N","E"]
    elif roomtype == 6:
        tmp = ["N","S"]
    elif roomtype == 7:
        tmp = ["N"]
    elif roomtype == 8:
        tmp = ["W","E","S"]
    elif roomtype == 9:
        tmp = ["W","E"]
    elif roomtype == 10:
        tmp = ["W","S"]
    elif roomtype == 11:
        tmp = ["W"]
    elif roomtype == 12:
        tmp = ["E","S"]
    elif roomtype == 13:
        tmp = ["E"]
    elif roomtype == 14:
        tmp = ["S"]
    else:
        tmp = []
    #end of if 
    return tmp
#end of function def


def heading_out(direction):
    global plyr_posx
    global plyr_posy
    global map_sizex
    global map_sizey
    # assess direction taken
    test = False
    if direction == "N" and plyr_posy == 0:
        return True
    elif direction == "W" and plyr_posx == 0:
        return True
    elif direction == "E" and plyr_posx == map_sizex:
        return True
    elif direction == "S" and plyr_posy == map_sizey:
        return True
    #end of if
#end of function def


def negotiate_room(room_type, direction):

    # get room exits list based on type of room
    exits = get_room_exits(room_type)

    # lets continue
    if direction == "X":
        print ("You chose to rest and the evil shodows slowly extend their deathly tendrils towards you...")
        print ("You fall asleep while resting and the evil shodows moxious gases slowly cover you completely and you die sleeping.")
        time.sleep(7)
        return False
    else:
        messing_about = heading_out(direction)
        # process direction
        if messing_about:
            print("The direction you chose may NOT have been one of the available options!")
            print("You head that anyway, thinking your Indian Jones, and bash your nose on a wall!")
            time.sleep(4)
            return False
        elif (exits.count(direction) > 0):
            # show direction taken
            if direction == "N":
                print ("You walk North into the next room in the labrynth...")
            elif direction == "W":
                print ("You walk West into the next room in the labrynth...")
            elif direction == "E":
                print ("You walk East into the next room in the labrynth...")
            elif direction == "S":
                print ("You walk South into the next room in the labrynth...")
            #end of if
            move_player(direction)
            time.sleep(2.5)
            if winner:
                return False
            else:
                return True
            #end of if
        else:
            print("The direction you chose may NOT have been one of the available options!")
            print("You head that anyway, thinking your Indian Jones, and bash your nose on a wall!")
            time.sleep(4)
            return False
        #end of if
    #end of if
#end of function def 


def consume_main_course():
    # globals
    global game_started
    # set up maze / cellar
    Test = False
    initialise_cellar()
    user_input = ""

    # show intro
    while (user_input.upper() != "X") and (user_input.upper() != "E"):
        show_intro_message()
        show_menu()
        user_input = input("\nPlease choose an option\n")
    #end of while
    os.system("cls")

    # main loop
    if user_input.upper() == "E":
        roomid = 0
        while (user_input.upper() != "X"):
            os.system("cls")
            display_map()
            roomid = roomtype_for("PlayerPos", 0)
            set_room_doors_menu(roomid)
            print(f"\n[> ROOM: {roomid} <]")
            print("\nUpon entering the room you review your surroundings,")
            print(f"You see the floor is tiled in such away that it spells out 'ROOM #{roomid}'.")
            print("and you are pesented with the following choices:\n")
            show_menu()
            user_input = input("\nWhich path will you choose?\n")
            Test = negotiate_room(roomid, user_input.upper())
            # process response
            if winner:
                os.system("cls")
                print("You make it out of the labrynth, and it empowers you even more, to complete your quest.")
                user_input = "X"
            elif Test:
                user_input = ""
            #end of if
        #end of while
        print ("\n\n\nThank for trying the maze/labrynth.")
    else:
        print ("\nYou have left the maze/labrynth.")
    #end of while
#end of function def
    

# START HERE =======================================
#consume_main_course()

#endregion


#region -------------------------------------------------------------------------------- SECTION 3 - THE POISON GARDEN --------------------------------------------------------------------------------



print()
def poison_garden_title():
    print("            wWWWw               wWWWw")
    print("       vVVVv(___) wWWWw         (___)  vVVVv")
    print ("      (___) ~Y~  (___)  vVVVv   ~Y~   (___) ")
    print("       ~Y~   \|    ~Y~   (___)    |/    ~Y~ ")
    print("       \|   \ |/   \| /  \~Y~/   \|    \ |/")
    print("      \\|// \\|// \\|/// \\|//  \\|// \\\|///")
    print("    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print(" ____,___,  __, _, _ _, _,_, _   _, _,__,__,__,_, _")
    print(" | |_||_   |_)/ \ |(_ / \|\ |  / _/_\|_)| \|_ |\ |")
    print(" | | ||    |  \ / |, )\ /| \|  \ /| || \|_/|  | \|")
    print(" ~ ~ ~~~~  ~   ~  ~ ~  ~ ~  ~   ~ ~ ~~ ~~  ~~~~  ~")


def grdn_dialogue_1():
    print("Your human decides to search the castle garden for one of the heir's artifacts.")
    print("")
    print("Upon exiting the castle doors, the faint smell of many flowers fills the air, growing stronger as you and your human descend the castle steps.")
    print("")
    print("You follow them as they make their way through the garden, keeping a lookout for prying eyes, while your human admires the garden's many lakes and flowerbeds.")
    print("")
    print("They reach a large fountain filled with murky water and fallen petals. It is encircled by mossy statues and a ring of aged cobblestone.")
    print("")
    print("From the fountain path extends two more walkways in opposite directions.")
    print("")
    print("The path to your left is draped with vines of purple flowers. A gentle scent like sweet wine invites you to take this path.")
    print("")
    print("And to your right, clusters of large red blooms guide your way, eminating a familliar scent that you can't quite seem to place.")

    input ("Press Enter to continue.")


def which_path_grdn():
    psn_grdn_path = input("Which path will you take ? ")
    print(psn_grdn_path)
    if psn_grdn_path.lower() == "left": 
        print("Your human takes the left path, as if drunk on it's wine-like smell.")
        print("")
        print("You proceed to follow them, almost getting distracted by the sudden beauty of this path's purple flowers now that you can see them up close.")
        print("")
        print("The end of the path is in sight, yet your human's pace comes to a decided halt.")
        print("")
        print('"..."')
        print("")
        print('"Wait"')
        print("")
        print('"I think I might stay a little longer."')
        print("")
        print("You almost want to disagree, but can't help but feel drawn back to the flower-draped path surrounding you.")
        print("")
        print("Vines creep up your human's leg unnoticed.")
        print("")
        print("You are distracted by the flowers.")
        print("")
        print("Your human is entangled tightly, yet their eyes are still fixated on the blooms.")
        print("")
        print("You are distracted by the flowers.")
        print("")
        print("Your human's face turns blue. Your halo starts to dim.")
        print("")
        print("Your life force slips away. You have failed.")
        print("")
        print("GAME OVER.")

        death_choice = input ("Would you like to try again? (Yes/No)")
        if death_choice.lower() == "yes":
            which_path_grdn()
        else:
            print()
            print("Your fate is sealed, never to return to this world.")
            quit()
            
        
    elif psn_grdn_path.lower() == "right":
        print("Your human takes the path to the right. The familliar scent feels comforting.")
        print("")
        print("'Don't let your guard down, Human'")
        print("")
        print("Your human continues down the path, watchng their step as they go.")
        print("")
        print("The path unwinds through the garden for what feels like hours, oversized red blooms seem to be watching your every move.")
        print("")
        print("Your human stays well away from the path edges, not allowing themself to be drawn near.")
        print("")
        print("You and your human finally reach the end of the pathway. A large stone door hides behind vines of ivy, as if the garden itself wishes to hold the door shut.")
        print("")
        print("Through the overgrowth however, the following words can be read ingraved into the stone:")
        print("")
        print("                                             A leech in the garden is me")
        print("                                        Yet my home is neither lake nor ground")
        print("                                          love I conjure when you are neath")
        print("                                             to my home I'm forever bound")

        grdn_dialogue_2()

    else:
        print("You must choose either left or right. There is no other way to proceed.")
        print(psn_grdn_path)

        
def grdn_dialogue_2():
    riddle_solution = input("Name me: ")
    if riddle_solution.lower() == "mistletoe":
        print("You wait")
        print("...And the overgrowth sealing the door deteriorates, allowing the old stone  doors to part,")
        print("revealing one of the heir's artifacts: A flower frozen in time by the Heir's glamour spell.")
        print("'A flower for beauty. You must destroy it.")
        print("With a determined nod, your human takes the flower in their hands, which activates their Holy Blessing, and causes the flower to wilt as the Heir's magic is released.. ")
        print("")
        input ("Press Enter to continue.")
    else:
        print("You wait")
        print("...But nothing happens.")

        input ("Press Enter to continue.")
    
    


poison_garden_title()

grdn_dialogue_1()

which_path_grdn()

#endregion


#region -------------------------------------------------------------------------------- SECTION 4 - THE CASTLE TOWER --------------------------------------------------------------------------------

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
            
            input ("Press Enter to continue.")


    elif blind_gargoyles == False:
         print("You examine the tapestry...")
         print("...")
         print("You can see that it is extremely detailed. No doubt the heir had it specially made along with the stained glass windows to strike fear into those who dare oppose their rule.")
         print("...")
         print("You peek behind the tapestry.")
         print("...")
         print("But it's just an empty wall.")

         what_do()
         decision = int(input("What will you do ? "))
         if decision == 1:
            examine_tapestry()
         elif decision == 2:
            examine_throne()
         elif decision == 3:
            examine_gargoyles()

    else:
        print("Please input a valid response.")



tower_dialogue_1()

#endregion


#region -------------------------------------------------------------------------------- SECTION 5 - THE FINAL BOSS --------------------------------------------------------------------------------

bond_point = ""

def main():
    global name
    global bond_point
    bond_point = 3
    name = input ("What is your name? ")
    print(f"Hello {name}")

    isPlaying = True
    while isPlaying:      
        print("\033[1;33mYou can 'attack' or 'quit'\033[0m")
        command = input("What do you want to do? ")
        
        if(command.lower() == "quit"):
            isPlaying = False
            print("Goodbye 👋")
        elif(command.lower() == "attack"):
            hasWon = enter_combat()
            if hasWon:
                isPlaying = False
            else:
                print("You lost, attack to try again.")
        
        else:
            print("Please insert a VALID response")

def enter_combat():
    enemy_health = 30
    player_health = 20

    def print_health(colour, hp_name, current_hp, max_hp):
        enemy_health_bar = ((f"\033[1;3{colour}m█" * current_hp * 2), ("▒" * (max_hp - current_hp) * 2))
        print (f"{hp_name} Health: [", *enemy_health_bar, f"\033[0m] {current_hp}/{max_hp}", sep="") 

    def player_attack(attack):   
        if attack.lower() == "slash":
            strength = random.randint(1, 4)
            print(f"{name} slashes at the demon but it manages to jump back, only taking {strength} damage")
            return strength
        elif attack.lower() == "stab":
            strength = random.randint(5, 10)
            print(f"{name} stabs the demon, the creature lets out a pained cry as it sustains {strength} damage")
            return strength
        elif attack.lower() == "parry":
            strength = random.randint(7, 20)
            print(f"As the demon moves to slash at {name} you whip around, blocking gracefully before delivering a deep strike of your own causing {strength} damage")
            return strength
        elif attack == "kill":
            strength = 30
            return strength
        else:
            print("That is not a valid attack")

    # Making typewriter effect for text
    def list_of_speech(speech):
        for line in speech:
            for character in line:
                print(character, end= '', flush=True)
                time.sleep(0.040)
            print("")

    while (enemy_health > 0) and (player_health > 0):
        # Printing HP bars using print health function
        print_health(1, "Demon", enemy_health, 30)
        print_health(3, "Jude", player_health, 20)

        # Choosing an attack and performing an attack
        print("Attack options [slash, stab, parry]")
        attack = input("Choose attack: ")
        strength = player_attack(attack)
        enemy_health -= strength
        if attack == "die":
            player_health = 0

        # Choosing a random speech option
        villain_speech = [  
            "The demon smiles unnaturally wide... \"My turn\"",
            f"As {name} jumps back from an attack the demon lunges forward",
            f"Before {name} could strike again, the demon makes its move",
            "\"You think a shiny sword is enough to defeat me?\" the demon laughs.",
            "\"Foolish mortal!\""
        ]
        rand_speech = random.choice(villain_speech)

        # Enemy chooses an attack if they are still alive
        if enemy_health > 0:
            print(rand_speech)
            enemy_attack = ["roar", "breathe fire", "helhound attack"]
            rand_enemy_attack = random.choice(enemy_attack)
            if rand_enemy_attack == "roar":
                strength = random.randint(1,4)
                print(f"The demon roared, terrifying {name}, you take {strength} damage")
                player_health -= strength
            elif rand_enemy_attack == "breathe fire":
                strength = random.randint(4,5)
                print(f"The demon breathes fire, causing burns to {name}'s body. You take {strength} damage")
                player_health -= strength
            elif rand_enemy_attack == "helhound attack":
                strength = random.randint(5,7)
                print(f"The demon summons a dark shadowy hound which lunges at {name}. You take {strength} damage")
                player_health -= strength

        # Endings depending on the outcome of the battle and bond points
        if enemy_health <= 0:
            print("The demon roars in a mixture of disbelief and horror. It flails at it's own body as it begins to disintegrate.")
            print("\"Please... Not like this\" It begs.")
            if bond_point == 3:
                # Giving a speech
                list_of_speech([f"{name} pauses, watching the demon. They step forward, still gripping you tightly in your sword form", 
                                f"\"You have done unspeakable evil... But I will not be like you\" as they say this they plunge you into the demons heart",
                                f"Your angelic power seeps into the demon. It screams, light pouring from its pores.",
                                "Weeks later...",
                                "The king is once again well, the staff that had been turned to gargoyles return to themselves,",
                                "having no memory of the weeks they spent inprisoned",
                                f"{name} has taken their rightful place as the heir of the kingdom and are learning from their father",
                                f"You stay to watch over {name}, knowing that no matter what the forces of evil throw at you-",
                                "You will be ready"])
            elif bond_point < 3:
                # Giving a speech
                list_of_speech([f"{name} stands over the demon, panting from the exersion of battle",
                                "\"You... are a monster. You robbed me of my life, stole my face, why should I show you mercy?\"",
                                "The demons answer was lost in a pained cry and gargle as black sludge poured from its mouth",
                                f"\"Help it\" you ask {name}",
                                "But they shake their head and watch. The demons death is long and painful.",
                                f"You must have missed some chance to influance {name} towards the light.",
                                "You feel a weight on your shoulders...",
                                "Then on your feet, on your ankles, on your legs..",
                                "You look down and see chains wrapping around you",
                                "They pull and you are gone.",
                                "You see a familiar demonic face \"Seems you're on my turf now\""
                ])
        elif player_health <= 0:
            # Giving a speech
            list_of_speech([f"Despite all your efforts {name} loses the battle.",
                            f"The demon cuts {name} down with one final blow and as they lay on thr ground, bleeding",
                            f"The demon draws their blood into a symbol on the ground.",
                            f"\"A servent you were, a servant you will be\" it says, smiling mouth dripping with blood",
                            f"As it completes the symbol {name} begins to transform...",
                            f"Their limbs break and reshape as their body turns to stone,",
                            f"they scream but nothing comes out as the stone travels down their throat",
                            f"The demon smiles, its glamour returning, \"Place this thing ousdie\" it shouts to the guards outside",
                            "Now you'll always see " "\033[1;31mmy\033[0m", "kingdom"
                ])

    # Finishing the combat
    if(enemy_health <= 0):
        return True
    else:
        return False

main()

#endregion