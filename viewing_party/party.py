# ------------- WAVE 1 --------------------
#adding a comment in the code to commit :)
def create_movie(title, genre, rating):
    
    user_data = {
        "watched": [],
        "watchlist": []
        }

    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    if None in new_movie.values():
        return None

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist_length = len(user_data['watchlist'])

    """compare the title argument to value of title in
    each movie dictionary in the user's watchlist
    if the titles are the same then append the movie dictionary
    to the user's watched list and delete the dictionary
    from the user's watchlist"""

    for i in range(watchlist_length):
        if user_data['watchlist'][i]['title'] == title:  
            user_data['watched'].append(user_data['watchlist'][i])
            del user_data['watchlist'][i]
    
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    sum_rating = 0
    watched_length = len(user_data['watched'])

    #exit function if user's watched list is empty
    if watched_length < 1:
        return avg_rating
    
    for movie in user_data['watched']:
        sum_rating += movie["rating"]

    avg_rating = sum_rating/watched_length
    
    return avg_rating

def get_most_watched_genre(user_data):
    popular_genre = None
    genre_list = []
    popular_count = 0
    watched_length = len(user_data['watched'])
    
    for i in range(watched_length):
        genre_list.append(user_data['watched'][i]['genre'])

    #could use Counter module but stuck to naive approach
    for genre in genre_list:
        if genre_list.count(genre) > popular_count:
            popular_count = genre_list.count(genre)
            popular_genre = genre
    
    return popular_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):

    user_watched_titles = []
    friends_movies = []
    unique_movies = []
    
    #generate a list of title values that user watched
    for movie in user_data['watched']:
        user_watched_titles.append(movie['title'])
    
    #generate a list of title values that friends watched
    for i in range(len(user_data['friends'])):
        for movie in user_data['friends'][i]['watched']:
            friends_movies.append(movie['title'])

    #convert to set to get unique titles via difference method
    user_watched_set = set(user_watched_titles)
    friends_movies_set = set(friends_movies)
    unique_watched = user_watched_set - friends_movies_set
    
    #generate list of unique movie dictionaries
    for movie in user_data['watched']:
        if movie['title'] in unique_watched:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):

    user_watched_titles = []
    friends_movies = []
    friends_unique_movies = []
    
    for movie in user_data['watched']:
        user_watched_titles.append(movie['title'])
    
    for i in range(len(user_data['friends'])):
        for movie in user_data['friends'][i]['watched']:
            friends_movies.append(movie['title'])

    user_watched_set = set(user_watched_titles)
    friends_movies_set = set(friends_movies)
    unique_watched = friends_movies_set - user_watched_set
    
    #avoiding duplicate movies by not adding movie that 
    #is already in friends_unique_movies list
    
    for i in range(len(user_data['friends'])):
        for movie in user_data['friends'][i]['watched']:
            if movie['title'] in unique_watched and movie not in friends_unique_movies:
                 friends_unique_movies.append(movie)
    
    return friends_unique_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

