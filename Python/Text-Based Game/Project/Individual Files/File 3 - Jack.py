from time import sleep



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


def which_path_grdn():
    psn_grdn_path = input("Which path will you take ? ")
    print(psn_grdn_path)
    if psn_grdn_path == "left": 
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
        
    elif psn_grdn_path == "right":
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
    if riddle_solution == "mistletoe":
        print("You wait")
        print("...And the overgrowth sealing the door deteriorates, allowing the old stone  doors to part,")
        print("revealing one of the heir's artifacts: A flower frozen in time by the Heir's glamour spell.")
        print("'A flower for beauty. You must destroy it.")
        print("With a determined nod, your human takes the flower in their hands, which activates their Holy Blessing, and causes the flower to wilt as the Heir's magic is released.. ")
        print("")
    else:
        print("You wait")
        print("...But nothing happens.")
    
    


poison_garden_title()

grdn_dialogue_1()

which_path_grdn()
