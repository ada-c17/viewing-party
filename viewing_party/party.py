# ------------- WAVE 1 --------------------

from tests.test_constants import MOVIE_TITLE_1


def create_movie(title, genre, rating):
    movie_dict = {}
    if not title:
        return None
    elif not genre:
        return None
    elif not rating:
        return None
    else:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict

def add_to_watched(user_data, movie):
    movie_list = user_data["watched"]
    movie_list.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watch_list= user_data["watchlist"]
    watch_list.append(movie)
    return user_data

def watch_movie(user_data, title):
    user_data_list = user_data["watchlist"]
    user_data_watched = user_data["watched"]
    for movie_details in user_data["watchlist"]:
        if movie_details["title"] == title:
            user_data_list.remove(movie_details)
            user_data_watched.append(movie_details)
            return user_data
        else:
            continue
    return user_data

        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0
    watched_dict = user_data["watched"]
    if len(watched_dict) == 0:
        return 0.0
    else:
        for movie_dict in watched_dict:
            sum += movie_dict["rating"]
        avg = float(sum / (len(watched_dict)))
        return avg

def get_most_watched_genre(user_data):
    watched_dict = user_data["watched"]
    genre_dict = {"Fantasy" : 0, "Action": 0, "Intrigue": 0, "Horror": 0}
    if len(watched_dict) == 0:
        return None
    else:
        for movie_dict in watched_dict:
            for genre in movie_dict.values():
                if genre == "Fantasy":
                    genre_dict["Fantasy"] += 1
                elif genre == "Action":
                    genre_dict["Action"] += 1
                elif genre == " Intrigue":
                    genre_dict["Intrigue"] += 1
                elif genre == "Horror":
                    genre_dict["Horror"] += 1
    genre_max = max(genre_dict, key=genre_dict.get)
    return genre_max



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friend_movie_list = []
    my_movie_list = []
    for friend in user_data["friends"]:
        friend_value = friend["watched"]
        for i in friend_value:  
            friend_movie_list.append(i)
    watched_list = user_data["watched"]
    for movie in watched_list:
        my_movie_list.append(movie)
    unique_list = []
    for movie in my_movie_list:
        if movie not in friend_movie_list:
            unique_list.append(movie)
    return unique_list

def get_friends_unique_watched(user_data):
    

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

