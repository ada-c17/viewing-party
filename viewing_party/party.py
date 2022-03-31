# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if not None in (title, genre, rating):
        movie_dict['title'] = title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

# helper function to remove movie from watchlist
def remove_movie_from_watchlist(user_data, movie):
    user_data['watchlist'].remove(movie)

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if title in movie['title']:
            add_to_watched(user_data, movie)
            remove_movie_from_watchlist(user_data, movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_movie_rating = 0

    # checks if the data are valid for input
    if user_data['watched'] == []:
        return 0.0

    # finds how many watched movies in user data
    total_movies = len(user_data['watched'])

    # loops to add each movie's rating
    for movie in user_data['watched']:
        total_movie_rating += float(movie['rating'])

    # calculate avg rating
    avg_rating = total_movie_rating / total_movies
    return avg_rating


def get_most_watched_genre(user_data):
    user_genre_dict = {}

    # checks if the data are valid for input
    if user_data['watched'] == []:
        return None

    # loops through user's watched
    # adds genre as key, occurances as value for user_genre_dict
    for movie in user_data['watched']:
        if movie['genre'] in user_genre_dict:
            user_genre_dict[movie['genre']] += 1
        else:
            user_genre_dict[movie['genre']] = 1
    
    # finds highest value and returns the key (genre) 
    most_watched_genre = max(user_genre_dict, key=user_genre_dict.get)

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_unique_movies = []
    user_movies = user_data['watched']
    friend_movies = get_friend_movies(user_data)

    # loops through user_movies
    # if movie not in friend_movies, adds to the user_unique_movies list
    for movie in user_movies:
        if movie not in friend_movies:
            user_unique_movies.append(movie)

    return user_unique_movies


# helper function to grab all the friend movies in a list
# also avoids adding duplicates into the list
def get_friend_movies(user_data):
    friend_movies = []
    for selection in user_data['friends']:
        for movie in selection['watched']:
            if movie not in friend_movies:
                friend_movies.append(movie)

    return friend_movies

def get_friends_unique_watched(user_data):
    friend_unique_movies = []
    user_movies = user_data['watched']
    friend_movies = get_friend_movies(user_data)
    
    # loop through to append friend movies that not are in user movies
    for movie in friend_movies:
        if movie not in user_movies:
            friend_unique_movies.append(movie)
    return friend_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies = []
    user_hosts = user_data['subscriptions']
    friend_unique_movies = get_friends_unique_watched(user_data)

    # loops through friend_unique_movies
    # if host is in user_hosts, adds to recommended_movies list
    for movie in friend_unique_movies:
        if movie['host'] in user_hosts:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_movies = []

    # initalize check to see if user_data's watched list is empty
    if user_data['watched'] == []:
        return recommended_movies
    
    # initalize check to see if user_data's friend's watched list is empty
    for friend in user_data['friends']:
        if friend['watched'] == []:
            return recommended_movies

    # calling helper function to find out most watch genre
    user_most_watched_genre = get_most_watched_genre(user_data)

    # calling helper function to find out movies friend's unique movies
    friend_unique_movies = get_friends_unique_watched(user_data)

    # loops through friend's unique movies list
    # if friend's movie matches user's genre, adds to recommended_movies list
    for movie in friend_unique_movies:
        if movie['genre'] in user_most_watched_genre:
            recommended_movies.append(movie)
    return recommended_movies


def get_rec_from_favorites(user_data):
    recommended_movies = []
    favorite_user_movies = user_data['favorites']
    friend_movies = get_friend_movies(user_data)

    # loops through favorite movies in user data
    # if movie not in friend's movies, add to recommended_movies list
    for movie in favorite_user_movies:
        if movie not in friend_movies:
            recommended_movies.append(movie)
    return recommended_movies




