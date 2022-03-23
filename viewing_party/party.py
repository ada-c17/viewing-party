# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    for value in movie_dict.values():
        if value == None:
            return None

    return movie_dict

def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data      
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum_rating = 0.0
    if len(user_data["watched"]) == 0:
        avg_rating = 0.0
    for movie in user_data["watched"]:
        sum_rating += movie["rating"]
        avg_rating = sum_rating/len(user_data["watched"])
    return avg_rating

def get_most_watched_genre(user_data):
    popular_genre = ""
    genres = []
    if len(user_data["watched"]) == 0:
        popular_genre = None
    for movie in user_data["watched"]:
        genres.append(movie["genre"])
        popular_genre = max(set(genres), key=genres.count)
    return popular_genre 
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_watched = []
    friend_watched = []
    user_watched = []
    if len(user_data["watched"]) == 0:
        return unique_watched
    for watched_movie in user_data["watched"]:
        user_watched.append(watched_movie)
    for friend_watched_dict in user_data["friends"]:
        for friend_watched_movie in friend_watched_dict["watched"]:
            friend_watched.append(friend_watched_movie)
    for movie in user_watched:
        if movie not in friend_watched:
            unique_watched.append(movie) 
    return unique_watched
        
def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    friend_watched = []
    user_watched = []
    movies_set = set()
    for watched_movie in user_data["watched"]:
        user_watched.append(watched_movie)
    for friend_watched_dict in user_data["friends"]:
        for friend_watched_movie in friend_watched_dict["watched"]:
            friend_watched.append(friend_watched_movie)
    for movie in friend_watched:
        if movie not in user_watched:
            friends_unique_movies.append(movie)
    final_friends_unique_movies = []
    for movie in friends_unique_movies:
        each_movie = tuple(movie.items())
        if each_movie not in movies_set:
            movies_set.add(each_movie)
            final_friends_unique_movies.append(movie)
    return final_friends_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    rec_movies = []
    friend_watched = get_friends_unique_watched(user_data)
    user_watched = []
    total_movies = []
    for movie in user_data["watched"]:
        user_watched.append(movie)
        total_movies.append(movie)
    for movie in friend_watched:
        total_movies.append(movie)
    for movie in total_movies:
        if movie not in user_watched and movie in friend_watched \
            and movie["host"] in user_data["subscriptions"]:
            rec_movies.append(movie)
    return rec_movies



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    rec_movies_by_genre = []
    most_watched_genre = get_most_watched_genre(user_data)
    friend_watched = get_friends_unique_watched(user_data)
    user_watched = []
    total_movies = []
    for movie in user_data["watched"]:
        user_watched.append(movie)
        total_movies.append(movie)
    for movie in friend_watched:
        total_movies.append(movie)
    for movie in total_movies:
        if movie not in user_watched and movie in friend_watched \
            and movie["genre"]==most_watched_genre:
            rec_movies_by_genre.append(movie)
    return rec_movies_by_genre

def get_rec_from_favorites(user_data):
    rec_movies = []
    friend_watched = []
    for movie_dict in user_data["friends"]:
        for movie in movie_dict["watched"]:
            friend_watched.append(movie)
    for movie in user_data["favorites"]:
        if movie not in friend_watched:
            rec_movies.append(movie)
    return rec_movies


