# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie = {"title": title, "genre": genre, "rating": rating}
    return movie

def add_to_watched(user_data, movie):
    watched = user_data["watched"]
    watched.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    user_watchlist = user_data["watchlist"]
    user_watched = user_data["watched"]
    print(type(user_watchlist))
    watching_index = None
    for index in range(len(user_watchlist)):
        print(index)
        movie = user_watchlist[index]
        if movie["title"] == movie_title:
            watching_index = index
    user_watched.append(user_watchlist[watching_index])
    user_watchlist.pop(watching_index)

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

