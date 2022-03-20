# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    for value in movie_dict.values():
        if value == None:
            return None

    return movie_dict

def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data      
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum_rating = 0.0
    if len(user_data["watched"]) == 0:
        avg_rating = 0.0
    for movie in user_data["watched"]:
        sum_rating += movie["rating"]
        avg_rating = sum_rating/len(user_data["watched"])
    return avg_rating

def get_most_watched_genre(user_data):
    popular_genre = ""
    genres = []
    if len(user_data["watched"]) == 0:
        popular_genre = None
    for movie in user_data["watched"]:
        genres.append(movie["genre"])
        popular_genre = max(set(genres), key=genres.count)
    return popular_genre 
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

