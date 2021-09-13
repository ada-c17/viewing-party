def create_movie(title, genre, rating):
    if not all((title, genre, rating)):
        return None 
   
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    } 

    return movie

def add_to_watched(user_data, movie):
    if not all((user_data, movie)):
        return None

    watched = user_data["watched"]
    watched.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    # if not all((user_data, movie)):
    #     return None

    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    if not all((user_data, title)):
        return None

    watchlist = user_data["watchlist"]

    for movie in watchlist:
        if movie["title"] == title:
            watchlist.remove(movie)
            add_to_watched(user_data, movie)

    return user_data

def get_watched_avg_rating(user_data):
    if not user_data:
        return None
    
    watched = user_data["watched"]

    if len(watched) == 0:
        return 0

    # ratings = []
    # for movie in watched:
    #     ratings.append(movie["rating"])

    ratings = [movie["rating"] for movie in watched ]
    average = sum(ratings)/len(ratings)

    return average 

def get_most_watched_genre(user_data):
    if not user_data:
        return None

    watched = user_data["watched"]
    if len(watched) == 0:
        return None

    # genre_count = { movie["genre"] for movie in watched }
    genre_count = {}

    for movie in watched:
        if movie["genre"] not in genre_count:
            genre_count[movie["genre"]] = 1
        else:
            genre_count[movie["genre"]] += 1

    return max(genre_count, key = lambda k:genre_count[k])

def get_unique_watched(user_data):
    if not user_data:
        return None
    
    watched = user_data["watched"]
    friends = user_data["friends"]

    friends_movies = [movie for friend in friends for movie in friend["watched"]]
    
    unique_friends_movies = {
    movies['title']:movies for movies in friends_movies}.values()
    
    unique_movies = [ movie for movie in watched if movie not in unique_friends_movies]
    return unique_movies

def get_friends_unique_watched(user_data):
    if not user_data:
        return None 

    watched = user_data["watched"]
    friends = user_data["friends"]

    friends_movies = [movie for friend in friends for movie in friend["watched"]]
    
    unique_friends_movies = {
    movies['title']:movies for movies in friends_movies}.values()
    
    unique_movies = [ movie for movie in unique_friends_movies if movie not in watched]
    return unique_movies

def get_available_recs(user_data):
    if not user_data:
        return None 
