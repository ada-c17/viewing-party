# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        movie_data = None

    else:
        movie_data = {
            'title': title,
            'genre': genre,
            'rating': rating
            }

    return movie_data


def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data


def watch_movie(user_data, movie_title):
    
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            break

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    try:
        total = 0
        for movie in user_data["watchlist"]:
            total += movie['rating']
            average = total / len(user_data["watchlist"])

    except ZeroDivisionError:
        average = 0.0

    return average


def get_most_watched_genre(user_data):
    if user_data["watched"]:
        genre_list = []
        for movie in user_data["watched"]:
            most_popular_genre.append(movie['genre'])
        most_popular_genre = max(genre_list, key = genre_list.count)
    else:
        most_popular_genre = None

    return most_popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_watched_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_movies.append(movie)

    unique_watched = []
    for movie in user_data["watched"]:
        if movie not in friends_watched_movies:
            unique_watched.append(movie)

    return unique_watched
    

def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    
    friend_1_watched_movies = user_data["friends"][0]["watched"]
    friend_2_watched_movies = user_data["friends"][1]["watched"]
    movies_friends_watched = tuple(friend_1_watched_movies + friend_2_watched_movies)

    for movie in movies_friends_watched:
        if movie in user_data["watched"]:
            continue
        else:
            if movie in friends_unique_watched:
                continue
            else:
                friends_unique_watched.append(movie)

    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    movie_recs = []

    # friend_1_watched_movies = user_data["friends"][0]["watched"]
    # friend_2_watched_movies = user_data["friends"][1]["watched"]
    # movies_friends_watched = tuple(friend_1_watched_movies + friend_2_watched_movies)
    
    # for movie in movies_friends_watched:
    #     if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
    #         movie_recs.append(movie)
    #     else:
    #         continue

    return movie_recs    


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    pass


def get_rec_from_favorites(users_data):
    pass