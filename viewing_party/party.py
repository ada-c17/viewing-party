# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}

    if title == None or genre == None or rating == None:
        return None

    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    movies = user_data["watchlist"]
    for movie in range(len(movies)):
        if movies[movie]['title'] == title:
            add_to_watched = movies[movie]
            del movies[movie]
            user_data["watched"].append(add_to_watched)
    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0 
    watched_list = user_data['watched']

    if len(watched_list) == 0:
        return 0.0 
    for movie in watched_list:
        sum += movie['rating']
    
    average = sum/(len(watched_list))
    return average


def get_most_watched_genre(user_data):
    genres_dict = {}
    counter = 0 

    watched_list = user_data['watched']
    list_length = len(watched_list)
    
    if list_length == 0:
        return None
    for movie in watched_list:
        genre = movie['genre']
        if genre not in genres_dict:
            genres_dict[genre] = 1
        else: 
            genres_dict[genre] += 1

    for key, value in genres_dict.items():
        if counter < value:
            counter += value
            most_frequent_genre = key
    return most_frequent_genre
        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_unique_movies = []
    repeated_movies = []

    user_watched_movies = user_data['watched']
    friends_data = user_data['friends']

    for friend in friends_data:
        for movie in friend['watched']:
            if movie in user_watched_movies:
                repeated_movies.append(movie)

    for unique_movie in user_watched_movies:
        if unique_movie not in repeated_movies:
            user_unique_movies.append(unique_movie)

    return user_unique_movies


def get_friends_unique_watched(user_data):
    unique_to_friends= []

    user_watched_movies = user_data['watched']
    friends_data = user_data['friends']

    for friend in friends_data:
        for movie in friend['watched']:
            if movie not in user_watched_movies:
                if movie not in unique_to_friends:
                    unique_to_friends.append(movie) 
    return unique_to_friends


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    user_watched_movies = user_data['watched']

    friends_data = user_data['friends']

    for friend in friends_data:
        for movie in friend['watched']:
            if movie not in user_watched_movies and movie['host'] in user_data['subscriptions']:
                recommended_movies.append(movie)
    return recommended_movies
        
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    user_frequent_genre = get_most_watched_genre(user_data)

    recommended_movies = []
    if user_frequent_genre is not None:
        user_watched_movies = user_data['watched']
        friends_data = user_data['friends']

        for friend in friends_data:
            if len(friend['watched']) > 0:
                for movie in friend['watched']:
                    if movie not in user_watched_movies and movie['genre'] == user_frequent_genre:
                        recommended_movies.append(movie)
    return recommended_movies


def get_rec_from_favorites(user_data):
    recommended_movies = []

    friends_data = user_data['friends']

    for movie in user_data['favorites']:
        valid_rec = True
        for friend in friends_data:
            if movie in friend['watched']:
                valid_rec = False
        if valid_rec:
            recommended_movies.append(movie)
    return recommended_movies
