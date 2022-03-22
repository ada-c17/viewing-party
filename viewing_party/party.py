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

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if 'title' in movie and movie['title'] == title:
            user_data["watchlist"].remove(movie)
            add_to_watched(user_data, movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = []
    average_rating = 0
    for movie in user_data['watched']:
        ratings.append(movie['rating'])
    if len(ratings) > 0:
        average_rating = sum(ratings)/len(ratings)
    else:
        average_rating = sum(ratings)
    return average_rating

def get_most_watched_genre(user_data):
    genres = []
    # add all user's genres to a list
    for movie in user_data["watched"]:
        if 'genre' in movie:
            genres.append(movie['genre'])
    
    if len(genres) == 0:
        return None
    else:
        popular_genre = max(set(genres), key = genres.count)
    return popular_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friend_movies = []
    unique_user_movies = []
    # generate friend watched movies list
    for friend_data in user_data["friends"]:
        if 'watched' in friend_data:
            for movie in friend_data['watched']:
                if movie not in friend_movies:
                    friend_movies.append(movie)
    # find users unique movies
    for movie in user_data["watched"]:
        if movie not in friend_movies and movie not in unique_user_movies:
            unique_user_movies.append(movie)
    return unique_user_movies

def get_friends_unique_watched(user_data):
    user_movies = user_data["watched"]
    unique_friend_movies = []
    for dict in user_data["friends"]:
        if 'watched' in dict:
            for movie in dict['watched']:
                if movie not in user_movies and movie not in unique_friend_movies:
                    unique_friend_movies.append(movie)
    return unique_friend_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    unique_friend_movies = get_friends_unique_watched(user_data)
    user_subscriptions = user_data['subscriptions']
    return [movie for movie in unique_friend_movies if movie['host'] in user_subscriptions]

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    unique_friend_movies = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    return [movie for movie in unique_friend_movies if movie['genre'] == most_watched_genre]

def get_rec_from_favorites(user_data):
    user_favorite_movies = user_data["favorites"]
    user_unique_watched = get_unique_watched(user_data)
    return [movie for movie in user_unique_watched if movie in user_favorite_movies]