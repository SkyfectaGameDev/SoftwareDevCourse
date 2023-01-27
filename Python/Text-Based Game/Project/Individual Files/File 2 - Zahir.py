# Health bar
# Judy
#name = ""
#    global name
#    name = input ("What is your name? ")
#    print(f"Hello {name}")
#10:22
#player_health_bar = (("\033[1;33m█" * player_health * 2), ("▒" * (20 - player_health) * 2))
#        print (f"{name}'s Health: [", *player_health_bar, f"\033[0m] {player_health}/20", sep="")





import os
import time

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
consume_main_course()









