# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------
def create_movie(movie_title, genre, rating):
    if not movie_title or not genre or not rating:
        return None 
    new_movie = {

        "title" : movie_title,
        "genre" : genre,
        "rating" : rating}

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    
    for movie_to_watch in user_data["watchlist"]:
        if movie_to_watch["title"] == title:
            user_data["watchlist"].remove(movie_to_watch)
            user_data["watched"].append(movie_to_watch)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating = 0
    if not user_data["watched"]:
        return 0
    watched_movie = user_data["watched"]
    for movie in watched_movie:
        rating +=float(movie["rating"])
    movie_len = len(user_data["watched"])
    avg_rating = rating / movie_len
    return avg_rating
'''
def get_most_watched_genre(user_data):
    most_watched = []
    count = 0
    # watched_movie = user_data["watched"]
    if len(user_data["watched"]) == 0:
        return None


    for movie in user_data["watched"]:
        most_watched.append(movie["genre"])
    
    for genre in most_watched:
        current_frequency = most_watched.count(genre)
        if current_frequency > count:
            count = current_frequency
            top_genre = genre
        return top_genre
    # print(current_frequency)
'''
def get_most_watched_genre(user_data):
    count = {}
    if len(user_data["watched"]) == 0:
        return None

    for movie in user_data["watched"]:
        if movie["genre"] not in count:
            count[movie["genre"]] = 1
        else:
            count[movie["genre"]] += 1

    top_watched = max(count, key=count.get)
    return top_watched
     


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):

    unique_movies = []
    user_movies = get_what_user_watched(user_data)
    friends_movies = get_friends_watched(user_data)
    for movie in user_movies:
        if movie not in friends_movies:
            unique_movies.append(movie)

    return unique_movies


def get_what_user_watched(user_data):
    return user_data["watched"]
    
    # user_movies = []
    # user_watched_lists = user_data["watched"]
    # for movies in user_watched_lists:
    #     user_movies.append(movies)
    # return user_movies

def get_friends_watched(user_data):
    friends_movies = []
    for friend_lists in user_data["friends"]:
        for movie in friend_lists["watched"]:
            friends_movies.append(movie)
    return friends_movies

def get_friends_unique_watched(user_data):
    only_friends_movies = []
    user_movies = get_what_user_watched(user_data)
    friends_movies = get_friends_watched(user_data)
    for movie in friends_movies:
        if movie not in user_movies and movie not in only_friends_movies:      
            only_friends_movies.append(movie)
            # if only_friends_movies.count(movie) > 1:
            #     only_friends_movies.remove(movie)
    return only_friends_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    #user_not_watched list
    # friends_watched list
    # user has subscription 
    #   "hulu", "netflix"
    user_recs = []

    for movie in get_friends_unique_watched(user_data):
        if movie["host"] in user_data["subscriptions"]:
            user_recs.append(movie)
            
    return user_recs
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    frequently_watched_rec = []
    for movie in get_friends_unique_watched(user_data):
        if movie["genre"] == get_most_watched_genre(user_data):
            frequently_watched_rec.append(movie)
    return frequently_watched_rec
def get_rec_from_favorites(user_data):
    favorites = []

    for movie in user_data["favorites"]:
        if movie not in get_friends_watched(user_data):
            favorites.append(movie)
    return favorites
