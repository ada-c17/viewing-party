# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    if not (title and genre and rating):
        return None
    else:
        new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
        
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)          
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data 

def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:    
        if movie_title in movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"] # An array of dictionaries 
    ratings = 0
    if len(watched_movies) == 0:
        return 0.0
    for movie in watched_movies:    # For each dictionary/movie in this array 
        ratings += movie["rating"]

    average = ratings/ len(watched_movies)

    return average

def get_most_watched_genre(user_data):
    #The aim appears to be a frequency map
    popular_genre_dict = {}
    watched_movies = user_data["watched"] 
    if len(watched_movies) == 0:
        return None

    for movies in watched_movies:
        genre = movies["genre"]
        if genre in popular_genre_dict:
            frequency = popular_genre_dict[genre] + 1 
            print(f"*********This is the value of: {frequency=}")
        else:
            frequency = 1

        popular_genre_dict.update({genre: frequency})
        print(f"*********This is the value of: {popular_genre_dict=}")
    popular_genre = None
    highest_frequency = 0
    for genre, frequency in popular_genre_dict.items():
        if frequency > highest_frequency:
            highest_frequency = frequency
            popular_genre = genre
        
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_friends_watched_movies(user_data):
    friends = user_data["friends"]   
    friends_watched_list = []
    for friend in friends:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)
        
    return friends_watched_list

def get_unique_watched(user_data):
    unique_watched_list = []
    watched_movies = user_data["watched"]   
    friends_watched_list = get_friends_watched_movies(user_data)
    for movie in watched_movies:
        if movie not in friends_watched_list:
            unique_watched_list.append(movie)
    
    return unique_watched_list

def get_friends_unique_watched(user_data):
    friends_unique_watched_list = []
    watched_movies = user_data["watched"] 
    friends_watched_list = get_friends_watched_movies(user_data)

    for movie in friends_watched_list:
        if len(friends_watched_list) == 0:
            return None
        elif movie in friends_unique_watched_list:
            continue 
        elif movie not in watched_movies:
            friends_unique_watched_list.append(movie)
            
    print(f"HERE IS THE LIST*************** {friends_unique_watched_list}")       
    return friends_unique_watched_list
    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommendations = []    
    watched_movies = user_data["watched"]  
    friends_unique_watched = get_friends_unique_watched(user_data)
    subscriptions = user_data["subscriptions"] # User's streaming services

    for movie in friends_unique_watched:
        if movie not in watched_movies:
            host = movie["host"]
            if host in subscriptions:
                recommendations.append(movie)
            
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    user_fave_genre = get_most_watched_genre(user_data) # This is a string
    recs_by_genre = []  
    friends_unique_watched = get_friends_unique_watched(user_data)
    for movie in friends_unique_watched:
        if movie["genre"] == user_fave_genre:
            recs_by_genre.append(movie)

    return recs_by_genre    


def get_rec_from_favorites(user_data):
    favorites = user_data["favorites"]   # A list of movie dictionaries
    recs_by_favorites = []
    friends_watched_list = get_friends_watched_movies(user_data)
    for movie in favorites:
        if movie in favorites and movie not in friends_watched_list:
            recs_by_favorites.append(movie)

    return recs_by_favorites
