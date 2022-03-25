
# ------------- WAVE 1 --------------------
# Creates a dictionary that holds movies with title, genre, and rating
def create_movie(title, genre, rating):
    new_movie = {"title": title,
                 "genre": genre,
                 "rating": rating}
    if title == None or genre == None or rating == None:
        return None
    else:
        return new_movie

# Creates a dictionary for watched movies


def add_to_watched(user_data, movie):
    watched_move_list = {"watched": [movie]}
    return watched_move_list

# Creates a dictionary for movies in watchlist


def add_to_watchlist(user_data, movie):
    watchlist_list = {"watchlist": [movie]}
    return watchlist_list

# Removing watched movie from watchlist to watched within a dictionary


def watch_movie(user_data, movie):
    user_updated_data = user_data
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == movie:
            remove_movie = user_updated_data["watchlist"].pop(i)
            user_updated_data["watched"] += [remove_movie]
    return user_updated_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# Calculates average rating for watched movies
def get_watched_avg_rating(user_data):
    counter = 0.0
    for key, value in user_data.items():
        for information in value:
            counter += information["rating"]

    length_of_movies = len(user_data["watched"])
    print(length_of_movies)
    if length_of_movies == 0:
        return counter
    else:
        average = counter / length_of_movies
        return average

# Finds most watche genre in user's watched within dictionary


def get_most_watched_genre(user_data):
    most_watched_genre = {}
    for movies in user_data["watched"]:
        for values in movies:
            if movies["genre"] not in most_watched_genre:
                most_watched_genre[movies["genre"]] = 1
            else:
                most_watched_genre[movies["genre"]] += 1
    length_of_movies = len(user_data["watched"])
    if length_of_movies == 0:
        return None
    else:
        most_watched_genre = max(
            most_watched_genre, key=most_watched_genre.get)
        return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    user_unique_watched = []
    user_watched = []
    friends_watched = []

    for movies in user_data["watched"]:
        user_watched.append(movies)

    for movies in user_data["friends"]:
        for details in movies["watched"]:
            friends_watched.append(details)

    user_unique_watched = [i for i in user_watched if i not in friends_watched]

    if len(user_unique_watched) == []:
        return 0
    else:
        return user_unique_watched


def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    user_watched = []
    friends_watched = []

    for movies in user_data["watched"]:
        user_watched.append(movies)

    for movies in user_data["friends"]:
        for details in movies["watched"]:
            friends_watched.append(details)

    friends_unique_watched = [
        i for i in friends_watched if i not in user_watched]

    no_duplicates_movie_list = []
    for i in friends_unique_watched:
        if i not in no_duplicates_movie_list:
            no_duplicates_movie_list.append(i)

    if len(friends_unique_watched) == []:
        return 0
    else:
        return no_duplicates_movie_list


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommend_list = []
    combined_list = []
    subscriptions = []
    for movies in user_data["subscriptions"]:
        subscriptions.append(movies)

    friends_list = get_friends_unique_watched(user_data)
    users_list = get_unique_watched(user_data)
    combined_list = friends_list + users_list

    for item in friends_list:
        for details in item:
            if item["host"] in subscriptions:
                recommend_list.append(item)

    newlist = []
    for i in recommend_list:
        if i not in newlist:
            newlist.append(i)

    if len(newlist) == []:
        return 0
    else:
        return newlist

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    new_rec_genre = []
    friends_list = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    for movie in friends_list:
        if movie["genre"] == most_watched_genre:
            new_rec_genre.append(movie)
    if len(new_rec_genre) == []:
        return 0
    else:
        return new_rec_genre


def get_rec_from_favorites(user_data):
    recommend_list = []
    user_favorite = []
    user_unique_list = get_unique_watched(user_data)

    for movie in user_data["favorites"]:
        user_favorite. append(movie)

    for movie in user_unique_list:
        if movie in user_favorite:
            recommend_list.append(movie)
    return recommend_list
