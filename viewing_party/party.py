# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    
    movie = {}
    movie['title'] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, movie_title):
    watched_movie = {}
    #find movie_title in user_data["watchlist"]
    for movie in user_data["watchlist"]:
        # movie is a dict
        if movie['title'] == movie_title:
            # add movieto user_data["watched"]
            user_data["watched"].append(movie)
            # remove movie_title in user_data["watchlist"]
            user_data["watchlist"].remove(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"]
    count = len(watched_movies)
    total_ratings = 0

    if count == 0:
        return 0

    for wacthed_movie in watched_movies:
        total_ratings += float(wacthed_movie["rating"])
    avg = total_ratings / count
    
    return avg

def get_most_watched_genre(user_data):
    watched_movies = user_data["watched"]
    genres = {}

    if len(watched_movies) == 0:
        return None

    for watched_movie in watched_movies:
        genre = watched_movie["genre"]
        if genre not in genres:
            genres[genre] = 1
        else:
            genres[genre] += 1

    most_watched_times = 1
    most_watched_genre = ""

    for genre, watched_times in genres.items():
        if watched_times > most_watched_times:
            most_watched_times = watched_times
            most_watched_genre = genre
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# -----------------------------------------
# ----------- HELPER FUNCTIONS ------------
def get_watched_movies_list(user_data):
    watched_movies = user_data["watched"]
    return watched_movies

def get_friends_watched_movies_list(user_data):
    friends = user_data["friends"]
    friends_watched_movies = []
    # friend = user_data["friends"]["watched"][i]
    for friend in friends:
        friend_watched_movies = friend["watched"]
        for friend_watched_movie in friend_watched_movies:
            friends_watched_movies.append(friend_watched_movie)

    return friends_watched_movies


# ----------- HELPER FUNCTIONS ------------
# -----------------------------------------

def get_unique_watched(user_data):
    # get list of watched movie dictionaries 
    watched_movies = get_watched_movies_list(user_data)

    # get friends' list of watched movie dictionaries
    friends_watched_movies = get_friends_watched_movies_list(user_data)

    unique_watched_list = []

    for watched_movie in watched_movies:
        if watched_movie not in friends_watched_movies:
            unique_watched_list.append(watched_movie)
    
    return unique_watched_list


def get_friends_unique_watched(user_data):
    # get list of watched movie dictionaries 
    watched_movies = get_watched_movies_list(user_data)

    # get friends' list of watched movie dictionaries
    friends_watched_movies = get_friends_watched_movies_list(user_data)

    unique_friends_watched_list = []

    for friends_watched_movie in friends_watched_movies:
        if friends_watched_movie not in watched_movies and friends_watched_movie not in unique_friends_watched_list:
            unique_friends_watched_list.append(friends_watched_movie)
    
    return unique_friends_watched_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    not_watched_movies = get_friends_unique_watched(user_data)   
    subscribed = user_data['subscriptions']
    recommendations = []

    for not_watched_movie in not_watched_movies:
        if not_watched_movie["host"] in subscribed:
            recommendations.append(not_watched_movie)

    return recommendations





# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

