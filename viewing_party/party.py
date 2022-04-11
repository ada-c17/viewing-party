# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    new_movie = {
        "genre" : genre, 
        "rating": rating,
        "title" : title,
    }
    return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"].copy()
    for movies in watchlist:
        if movies["title"] == title: 
            user_data["watchlist"].remove(movies)
            user_data["watched"].append(movies)

            break
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"] ## array of dictionaries
    total_rating = []

    for movie_data in watched_movies:
        rating = movie_data["rating"]
        total_rating.append(rating)
    if not total_rating:
        return 0.0
    average = sum(total_rating) / len(total_rating)
    return average


def get_most_watched_genre(user_data):
    watched_movies = user_data["watched"]
    most_popular_genre = ""
    popular_genre = []
    count = 0

    if not watched_movies:
        return None
    for movie_data in watched_movies: 
        popular_genre.append(movie_data["genre"])
        genre_count = popular_genre.count(movie_data["genre"])
        if count < genre_count:
            count = genre_count
            most_popular_genre = movie_data["genre"]
    return most_popular_genre



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    watched_movies = user_data["watched"]
    friends_list = user_data["friends"]
    friend_movies = []
    unique_user_movies = [] 

    for movie_watched in friends_list:
        for movie in movie_watched["watched"]:
            friend_movies.append(movie)
    for movie in watched_movies:
        if movie not in friend_movies:
            unique_user_movies.append(movie)
    return unique_user_movies



def get_friends_unique_watched(user_data):
    watched_movies = user_data["watched"]
    friends_list = user_data["friends"]
    unique_friend_movies = [] 
    unique_unique = []

    for movie_watched in friends_list: # {} in [{}]
        for movie in movie_watched["watched"]: 
            if movie not in unique_friend_movies:
                unique_friend_movies.append(movie)
                if movie in unique_friend_movies and movie not in watched_movies:
                    unique_unique.append(movie)
    return unique_unique



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    movie_rec = []
    watched_movies = user_data["watched"]
    unique_movie_friends = get_friends_unique_watched(user_data)
    user_subscriptions = user_data["subscriptions"]

    for movie in unique_movie_friends:
        if movie["host"] in user_subscriptions and movie not in watched_movies:
            movie_rec.append(movie)
    return movie_rec



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    popular_genre = get_most_watched_genre(user_data)
    unique_movie_friends = get_friends_unique_watched(user_data)
    rec_by_genre = []

    for movie in unique_movie_friends:
        if movie["genre"] == popular_genre:
            rec_by_genre.append(movie)
    return rec_by_genre


def get_rec_from_favorites(user_data):
    user_favorites = user_data["favorites"]
    friends_list = user_data["friends"]
    friend_watched = []
    rec_by_fave = []

    for movie in friends_list:
        for watched_movie in movie["watched"]:
           friend_watched.append(watched_movie)

    for movie in user_favorites:
        if movie in user_favorites and movie not in friend_watched:
            rec_by_fave.append(movie)
    return rec_by_fave