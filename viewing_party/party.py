# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # clarify why this doesn't work
    # if title or genre or rating is None:
    #     return None 

    new_movie = {
        "title": title, 
        "genre": genre,
        "rating": rating 
    }

    if title == None or genre == None or rating == None:
        new_movie = None 
    return new_movie


def add_to_watched(user_data, movie):
    # if movie:
    #     return user_data["watched"].append(movie)
    print(movie)
    print(user_data)

    updated_data = user_data["watched"].append(movie)
    return updated_data
    # if movie:
    # # return user_data["watched"].append(movie)
    #     return user_data["watched"].append({
    #         "title": movie["title"],
    #         "genre": movie["genre"],
    #         "rating": movie["rating"]
    #     })

def add_to_watchlist(user_data, movie):
    updated_watchlist = user_data["watchlist"].append(movie)
    # updated_watchlist = user_data["watchlist"].append({
    #         "title": movie["title"],
    #         "genre": movie["genre"],
    #         "rating": movie["rating"]
    #     })

    return updated_watchlist


def watch_movie(user_data, title):
    if title in user_data["watchlist"]:
        user_data["watchlist"].remove(title)
        user_data["watched"].append(title)
    
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

