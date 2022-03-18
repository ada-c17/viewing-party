# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        movies = None
    else:
        movies = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
    return movies

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for watched_movie in user_data["watchlist"]:
        if watched_movie["title"] == title:
            user_data["watchlist"].remove(watched_movie)
            user_data["watched"].append(watched_movie)
    return user_data

# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    rating_count = 0
    for movie in user_data["watched"]:
        rating_count += 1
        avg_rating += movie["rating"]
    if rating_count > 0:
        return avg_rating / rating_count
    else:
        return avg_rating


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

