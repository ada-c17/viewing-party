# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_table = {}
    if title and genre and rating:
        movie_table["title"] = title
        movie_table["genre"] = genre
        movie_table["rating"] = rating
        return movie_table
def add_to_watched(user_data,movie):
        if not all((user_data,movie)):
            return None   
        watched = user_data["watched"]
        watched.append(movie)
        print(user_data) 
        return user_data
        # return updated_datas
def add_to_watchlist(user_data,movie):
        if not all((user_data,movie)):
            return None
        watchlist = user_data["watchlist"]
        watchlist.append(movie)
        return user_data
def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    new_watchlist = []
    watched = user_data["watched"]
    
    for item in range(len(list(watchlist))):
        if watchlist[item]["title"] != title:
            new_watchlist.append(watchlist[item])
        else:
            watched.append(title)
    user_data["watchlist"] = new_watchlist

    return user_data


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

