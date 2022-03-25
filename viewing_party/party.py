# ------------- WAVE 1 --------------------

from itertools import count


def create_movie(title, genre, rating):
    if None in [title, genre, rating]:
        return None
        
    movie_dict = {
                "title" : title,
                "genre" : genre,
                "rating" : rating
    }
    return movie_dict


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            just_watched = user_data["watchlist"].pop(i)
            user_data["watched"].append(just_watched) 
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0.00

    if len(user_data["watched"]) == 0:
        return sum

    for movie in user_data["watched"]:
        sum += movie["rating"]
    average = sum / len(user_data["watched"])
    return average


def get_most_watched_genre(user_data):
    genre_dict = {}
    max_genre = ["", 0]

    if len(user_data["watched"]) == 0:
        return None

    for current in user_data["watched"]:
        if current["genre"] in genre_dict:
            genre_dict[current["genre"]] += 1
        else:
            genre_dict[current["genre"]] = 1
        if max_genre[1] < genre_dict[current["genre"]]: #checks for a new high score(most popular genre)
            max_genre[0] = current["genre"]
            max_genre[1] = genre_dict[current["genre"]]
    return max_genre[0]


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    movie_list = user_data["watched"].copy()
    friend_list = combine_friend_movies(user_data)
    user_only =[]

    for movie in movie_list:
        if not movie in friend_list:
            user_only.append(movie)
    return user_only


def get_friends_unique_watched(user_data):
    movie_list = user_data["watched"].copy()
    friend_list = combine_friend_movies(user_data)
    friend_only =[]

    for movie in friend_list:
        if not movie in movie_list:
            friend_only.append(movie)
    return friend_only


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friend_movies = get_friends_unique_watched(user_data)
    to_watch = []

    for movie in friend_movies:
        if movie["host"] in user_data["subscriptions"]:
            to_watch.append(movie)
    return to_watch


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    pop_genre = get_most_watched_genre(user_data)
    friend_movies = get_friends_unique_watched(user_data)
    to_watch = []

    for movie in friend_movies:
        if movie["genre"] == pop_genre:
            to_watch.append(movie)
    return to_watch


def get_rec_from_favorites(user_data):
    friend_movies = combine_friend_movies(user_data)
    to_watch = []

    for movie in user_data["favorites"]:
        if not movie in friend_movies:
            to_watch.append(movie)
    return to_watch


# -----------------------------------------
# ------------- HELPERS -------------------
# -----------------------------------------
def combine_friend_movies(user_data):
    friend_list = []

    for friends in user_data["friends"]:
        for movie in friends["watched"]:
            if not movie in friend_list:
                friend_list.append(movie)
    return friend_list