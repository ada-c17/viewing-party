# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if title and genre and rating:
    
        movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
            }
        return movie
    
    else:
        return None
    
def add_to_watched(user_data, movie):
    
    watched = []

    user_data = {"watched": watched}

    #for item in movie.items():
    for value in user_data:
        watched.append(movie)
        print(watched)
        #len_watched += 1
        #return len_watched

    # for key, value in user_data["watched", ]:
    # for value in watched:
    #     watched.append(movie)
    #     len_watched += 1
    #     return len_watched
    
    #print(len_watched)
                
    return user_data


def add_to_watchlist(user_data, movie):

    watchlist = []
    len_watchlist = 0
    user_data = {"watchlist", watchlist}

    for key, value in user_data.items():
        len_watchlist = len(value)
        if len(value) > 0:
            watchlist.append(movie)
            len_watchlist =+ 1
            return len_watchlist

    return user_data

#def watch_movie():



#the value of user_data will be a dictionary with a key "watched", and a value which is a list of dictionaries representing the movies the user has watched
#An empty list represents that the user has no movies in their watched list
#the value of movie will be a dictionary in this format:




#If those three attributes are truthy, then return a dictionary. This dictionary should...
# Have three key-value pairs, with specific keys
# The three keys should be "title", "genre", and "rating"
# The values of these key-value pairs should be appropriate values
# If title is falsy, genre is falsy, or rating is falsy, this function should return None


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

