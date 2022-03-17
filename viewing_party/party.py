# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not (title and genre and rating):
        return None
    return {"title":title, "genre":genre,"rating":rating}

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    updated_watchlist = []
    for movie in user_data["watchlist"]:
        if movie_title != movie["title"]:
            updated_watchlist.append(movie)
        else:
            user_data["watched"].append(movie)
    user_data["watchlist"] = updated_watchlist
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0

    rating_sum = 0
    for movie in user_data["watched"]:
        rating_sum += movie["rating"]
    return rating_sum / len(user_data["watched"])

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    watched_genre_frequencies = {}
    
    for movie in user_data["watched"]:
        if movie["genre"] in watched_genre_frequencies.keys():
            watched_genre_frequencies[movie["genre"]] += 1
        else:
            watched_genre_frequencies[movie["genre"]] = 1
    
    current_top = ["",0]
    for genre, count in watched_genre_frequencies.items():
        if count > current_top[1]:
            current_top = [genre, count]
    return current_top[0]


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

