# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {
        "title":title,
        "genre":genre,
        "rating":rating
    }

    for val in movie_dict.values():
        if not val:
            return None

    return movie_dict

def add_to_watched(user, movie):

    for key in user:
        user[key].append(movie)
    
    return user

def add_to_watchlist(user, movie):

    for key in user:
        user[key].append(movie)
    
    return user

def watch_movie(user_data, movie):
    
    filtered_user_data = dict(user_data)

    for elem in user_data["watchlist"]:
        watched_movie = elem["title"]
        if movie == watched_movie:
            filtered_user_data["watched"].append(elem)
            filtered_user_data["watchlist"].remove(elem)

    return filtered_user_data

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

