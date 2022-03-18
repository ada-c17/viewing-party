#my first commit

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    dict_of_movies = {}
    if title == None or genre  == None or rating == None:
        return None
    dict_of_movies["title"] = title
    dict_of_movies["genre"] = genre
    dict_of_movies["rating"] = rating
    return dict_of_movies

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def  add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(janes_data, MOVIE_TITLE_1):
    for movie in janes_data["watchlist"]:
        if movie["title"]==MOVIE_TITLE_1:
            watched_movie=movie
            janes_data["watched"].append(watched_movie)
            janes_data["watchlist"].remove(movie)
            break
    return (janes_data)
        

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

