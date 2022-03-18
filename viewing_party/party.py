# ------------- WAVE 1 --------------------

user_data = {}

def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        new_movie = {
            "title": movie_title,
            "genre": genre,
            "rating": rating
        }
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"]= [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"]= [movie]
    return user_data

def watch_movie(user_data, movie):
    # already_watched_list = user_data["watched"]
    # to_watch_list = user_data["watchlist"]
    for value in user_data["watchlist"]:
        if value["title"] == movie:
            movie_watched = value
            user_data["watched"].append(movie_watched)
            user_data["watchlist"].remove(movie_watched)
    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_list = []
    for value in user_data["watched"]:
        rating_list.append(value["rating"])
    if rating_list != []:
        average = sum(rating_list)/len(user_data["watched"])
    else:
        average = 0.0
    return average


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

