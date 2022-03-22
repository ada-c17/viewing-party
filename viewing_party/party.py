# ------------- WAVE 1 --------------------

from hashlib import new


def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        movie = None
    else:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    return movie

def add_to_watched(user_data, movie):
    updated_list = []
    for film in user_data["watched"]:
        updated_list.append(film)
    updated_list.append(movie)
    user_data["watched"] = updated_list    
    return user_data

def add_to_watchlist(user_data, movie):
    updated_list = []
    for film in user_data["watchlist"]:
        updated_list.append(film)
    updated_list.append(movie)
    user_data["watchlist"] = updated_list    
    return user_data

def watch_movie(user_data, title):
    move_film = False
    for film in range(len(user_data["watchlist"])):
        if user_data["watchlist"][film]["title"] == title:
            move_film = user_data["watchlist"][film]
            del user_data["watchlist"][film]
    if not move_film:
        return user_data
    user_data["watched"].append(move_film)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        average = 0.0
        return average
    rating_list = []
    for dict in range (len(user_data["watched"])):
        rating_list.append(user_data["watched"][dict]["rating"])
    average = sum(rating_list)/len(rating_list)
    return average

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    genre_dict = {}
    for dict in range (len(user_data["watched"])):
        genre = user_data["watched"][dict]["genre"]
        if genre not in genre_dict:
            genre_dict[genre] = 1
        else:
            genre_dict[genre] += 1
    return max(genre_dict, key=genre_dict.get)
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friend_watched = []
    unique_user_watched = []
    for friend in user_data["friends"]:
        for key, value in friend.items():
            if key == 'watched':
                for movie in value:
                    friend_watched.append(movie)
    for movie in user_data["watched"]:
        if movie not in friend_watched:
            unique_user_watched.append(movie)
    return unique_user_watched

def get_friends_unique_watched(user_data):

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_hosts = user_data["subscriptions"]


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

