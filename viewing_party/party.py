from statistics import mean

# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
    for value in movie_dict.values():
        if value == None:
            return None
    return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == movie:
            add_to_watched(user_data, movie)
            del user_data["watchlist"][i]
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = []
    average_rating = 0
    for i in range(len(user_data["watched"])):
        ratings.append(user_data["watched"][i]['rating'])
    if len(ratings) > 0:
        average_rating = sum(ratings)/len(ratings)
    else:
        average_rating = sum(ratings)
    return average_rating

def get_most_watched_genre(user_data):
    genres = []
    for i in range(len(user_data["watched"])):
        genres.append(user_data["watched"][i]['genre'])
    if len(genres) == 0:
        return None
    else:
        popular_genre = max(set(genres), key = genres.count)
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

