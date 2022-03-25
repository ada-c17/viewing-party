# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating: 
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title in movie.values():
            user_data["watchlist"].remove(movie)
            user_data = add_to_watched(user_data, movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0
    movie_count = len(user_data["watched"])
    if user_data["watched"]:
        for movie in user_data["watched"]:
            sum += movie["rating"]
        return sum/movie_count
    else:
        return sum

def get_most_watched_genre(user_data):
    genres = []
    if user_data["watched"]:
        for movie in user_data["watched"]:
            genres.append(movie["genre"])
        # will return the genre with the highest count in the list
        return max(genres, key = genres.count)
    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies = []
    friend_count = len(user_data["friends"])
    # Use friend_watched count to keep track of all the friends, to be sure that the movie
    # is not in either friends watched list 
    for movie in user_data["watched"]:
        friend_watched = 0
        for friend in user_data["friends"]:
            if movie not in friend["watched"]:
                friend_watched += 1
        if friend_watched == friend_count:
            unique_movies.append(movie)

    return unique_movies


def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)
    return friends_unique_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    reccomendations = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            reccomendations.append(movie)
    return reccomendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    reccomendations = []
    genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)
    for movie in friends_unique_watched:
        if movie["genre"] == genre:
            reccomendations.append(movie)
    return reccomendations


def get_rec_from_favorites(user_data):
    reccomendations = []
    unique_movies = get_unique_watched(user_data)
    for movie in user_data["favorites"]:
        if movie in unique_movies:
                reccomendations.append(movie)
    return reccomendations