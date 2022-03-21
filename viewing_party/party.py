# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {"title": title, "genre":
        genre, "rating": rating
        }
    if title is None or genre is None or rating is None:
        return None
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data



def watch_movie(user_data, title):
    
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(title)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    #data_dict = user_data["watched"]
    rating_list = []
    user_data_average = 0
    for movie in user_data["watched"]:
        if movie["rating"] == None:
            user_data_average = 0.0
        else:
            rating_list.append(movie["rating"])
        user_data_average = sum(rating_list) / len(rating_list)
    return user_data_average


def get_most_watched_genre(user_data):
    watched_genre = []
    most_watched_genre = None
    for movie in user_data["watched"]:
        if movie["genre"] == None:
            return most_watched_genre
        else:
            watched_genre.append(movie["genre"])
        most_watched_genre = max(set(watched_genre), key = watched_genre.count)
    return most_watched_genre        


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data): 
    unique_watched = []
    unique_watched += user_data["watched"]
    for data in user_data["friends"]:
        for movie in data["watched"]:
            if movie in unique_watched:
                unique_watched.remove(movie)
            
    return unique_watched

def get_friends_unique_watched(user_data):
    not_watched = []
    
    for data in user_data["friends"]:
        for movie in data["watched"]:
            if movie not in user_data["watched"] and movie not in not_watched:
                not_watched.append(movie)
                
    return not_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    streaming_services = user_data["subscriptions"]
    
    for data in user_data["friends"]:
        for movie in data["watched"]:
            if movie not in user_data["watched"] and movie not in recommended_movies:
                if movie["host"] in streaming_services:
                    recommended_movies.append(movie)
    return recommended_movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------