print ()

def film_check():

    for i in range(len(fav_movies)):
        print ("-", fav_movies[i])
        if fav_movies[i] == "Ghostbusters" and i == 2:
            print ("Who you gonna call?")
        else:
            print ("My disappointment is immeasurable, and my day is ruined.")
        print ()
    
fav_movies = [
    "Forrest Gump",
    "Pulp Fiction",
    "Ghostbusters",
    "Baby Driver"
]

print ("My top four favourite movies are: ")
film_check()