print ()
print ("################################################################################")
print ("#                                   GUARDIAN                                   #")  # Title
print ("################################################################################")
print ()

name = input ("Please enter your character's name: ")

#region ----- Gendered Language -----
gendered_lang = ("", "", "", "", "", "")

gender = input (f"Does {name} use masculine, feminine or neutral pronouns? (M/F/N): ")
print ()

if gender.upper() == "M":
    gendered_lang = ("He",    "Him",   "His",    "His",     "Prince",    "is")
elif gender.upper() == "F":
    gendered_lang = ("She",   "Her",   "Her",    "Hers",    "Princess",  "is")
elif gender.upper() == "N":
    gendered_lang = ("They",  "Them",  "Their",  "Theirs",  "Heir",      "are")
else:
    print ("Input not recognised.")

print (f"Welcome, {name}.")
print (f"This is an example of how to refer to the character. {gendered_lang[0]} {gendered_lang[5]} the {gendered_lang[4]}. This is {gendered_lang[2]} story.")

print ()
#endregion

#region ----- Health Bar Mechanics -----
health = 12

def show_health():
    health_bar = (("\033[1;33m█" * health * 2), ("▒" * (15 - health) * 2))          # This is a string that stores the health bar itself and a colour value.

    print (f"{name}'s Health: [", *health_bar, f"\033[0m] {health}/15", sep="")     # This is a string that stores the health bar itself and a colour value.
    print ()

show_health()
#endregion
