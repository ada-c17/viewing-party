
# I was inspired by Joan's idea of making a helper function instead of copy-pasting
def create_friend_watched_list(user_data):
    friend_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched.append(movie)
    return friend_watched

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
        return 0.0
    rating_list = []
    for dict in range (len(user_data["watched"])):
        rating_list.append(user_data["watched"][dict]["rating"])
    return sum(rating_list)/len(rating_list)

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
    friend_watched = create_friend_watched_list(user_data)
    unique_user_watched = []
    for movie in user_data["watched"]:
        if movie not in friend_watched:
            unique_user_watched.append(movie)
    return unique_user_watched

def get_friends_unique_watched(user_data):
    friend_watched = create_friend_watched_list(user_data)
    unique_friend_watched = []
    for movie in friend_watched:
        if movie not in user_data["watched"] and movie not in unique_friend_watched:
            unique_friend_watched.append(movie)
    return unique_friend_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friend_watched = create_friend_watched_list(user_data)
    return [movie for movie in friend_watched if movie["host"] in user_data["subscriptions"] and movie not in user_data["watched"]]

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)
    return [movie for movie in friends_unique_watched if movie["genre"] == genre and movie not in user_data["watched"]]

def get_rec_from_favorites(user_data):
    friend_watched = create_friend_watched_list(user_data)
    return [movie for movie in user_data["favorites"] if movie not in friend_watched]
