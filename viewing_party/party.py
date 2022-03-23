# ------------- WAVE 1 --------------------

from statistics import mean


def create_movie(title, genre, rating):
    if None in (title,genre,rating,):
        return None
    else:
        new_movie = {
            "title":title,
            "genre":genre,
            "rating":rating
        }
        return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    try: 
        filter_ratings = []
        for movie in user_data["watched"]:
            filter_ratings.append(movie["rating"])
        average_rating = mean(filter_ratings)
        return average_rating
    except:
        return 0.0

def get_most_watched_genre(user_data):
    genre_count = {}
    genre_counter = 0
    top_genre = None
    for movie in user_data["watched"]:
        if movie["genre"] in genre_count:
            genre_count[movie["genre"]] += 1
        else: 
            genre_count[movie["genre"]] = 1
        if genre_count[movie["genre"]] > genre_counter:
            top_genre = movie["genre"]
            genre_counter = genre_count[movie["genre"]]
    return top_genre 


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    pass

def get_friends_unique_watched(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    pass

def get_rec_from_favorites(user_data):
    pass