# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
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


def watch_movie(user_data, MOVIE_TITLE_1):
    for movies in user_data.values():
        for movie in movies:
            if movie["title"] == MOVIE_TITLE_1:
                add_movie = movies.pop(movies.index(movie))
                user_data["watched"].append(add_movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    try:
        total = 0
        num_movies = 0

        for movies in user_data.values():
            for movie in movies:
                num_movies += 1
                total += movie['rating']
        average = total / num_movies
    except ZeroDivisionError:
        average = 0.0

    return average


def get_most_watched_genre(user_data):
    if user_data["watched"]:
        most_popular_genre = []
        for movies in user_data.values():
            for movie in movies:
                most_popular_genre.append(movie['genre'])
        user_data = max(set(most_popular_genre), key = most_popular_genre.count)
    else:
        user_data = None

    return user_data

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_watched = []
    friend_1_watched_movies = user_data["friends"][0]["watched"]
    friend_2_watched_movies = user_data["friends"][1]["watched"]

    for movie in user_data["watched"]:
        if movie in friend_1_watched_movies or movie in friend_2_watched_movies:
            continue
        else:
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

    friend_1_watched_movies = user_data["friends"][0]["watched"]
    friend_2_watched_movies = user_data["friends"][1]["watched"]
    movies_friends_watched = tuple(friend_1_watched_movies + friend_2_watched_movies)
    
    for movie in movies_friends_watched:
        if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
            movie_recs.append(movie)
        else:
            continue

    return movie_recs    


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    # user_movie_genres = {}
    # for movie in user_data["watched"]:
    #     if movie["genre"] in movie:
    #         user_movie_genres.append(movie['genre'])

    # try:
    #     user_most_watched_genre = max(set(user_movie_genres), key = user_movie_genres.count)
    # except ValueError:
    #     user_most_watched_genre = []

    # friend_1_watched_movies = user_data["friends"][0]["watched"]
    # friend_2_watched_movies = user_data["friends"][1]["watched"]
    # movies_friends_watched = tuple(friend_1_watched_movies + friend_2_watched_movies)
    
    # movie_recs = []
    # for movie in movies_friends_watched:
    #     if movie not in user_data["watched"] and movie["genre"] == user_most_watched_genre:
    #         movie_recs.append(movie)
    #     else:
    #         continue
    # return movie_recs
    pass


def get_rec_from_favorites(users_data):
    pass