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
    ratings_data = []
    watched_movies = user_data["watched"] # An array of dictionaries 
    average = 0.0
    for movie in watched_movies:    # For each dictionary/movie in this array 
        ratings_data.append(movie["rating"])
    
        ratings_total = sum(ratings_data)
        average = ratings_total / len(ratings_data)

    return average

def get_most_watched_genre(user_data):
    #The aim appears to be a frequency map
    popular_genre_dict = {}
    watched_movies = user_data["watched"] 
    if len(watched_movies) == 0:
        return None

    for movies in watched_movies:
    # for genre, frequency in popular_genre.items():
        genre = movies["genre"]
        if genre in popular_genre_dict:
            frequency = popular_genre_dict[genre] + 1 
            print(f"*********This is the value of: {frequency=}")
        else:
            frequency = 1
            # popular_genre = {str(genre): frequency}
        popular_genre_dict.update({genre: frequency})
        print(f"*********This is the value of: {popular_genre_dict=}")
    popular_genre = None
    highest_frequency = 0
    for genre, frequency in popular_genre_dict.items():
        if frequency > highest_frequency:
            highest_frequency = frequency
            popular_genre = genre
        # highest_frequency = max(popular_genre_dict.values)
        # popular_genre = max(popular_genre_dict, genre = popular_genre_dict.get) 
        
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
            
    #Movie title variable? For each movie in movie ditionary in watched movies
    print(f"HERE IS THE LIST*************** {friends_unique_watched_list}")       
    return friends_unique_watched_list
    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommendations = []    
    watched_movies = user_data["watched"]  
    friends_unique_watched = get_friends_unique_watched(user_data)
    subscriptions = user_data["subscriptions"] # This represents the names of streaming services that the user has access to

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
# Consider the user's most frequently watched genre. 
    user_fave_genre = get_most_watched_genre(user_data)
# Then, determine a list of recommended movies. 
    watched_movies = user_data["watched"]  

    recs_by_genre = []
    recommendations = get_available_recs(user_data)  
    # friends_unique_watched = get_friends_unique_watched(user_data)
    # for movie in friends_unique_watched:
    #     if movie not in watched_movies:
    #         for genre in friends_unique_watched["genre"]: 
    #             if genre in user_fave_genre:
    #                 recs_by_genre = recs_by_genre.append(movie)
    for movie in recommendations:
        if movie not in watched_movies:
            for genre in movie:
                if genre == user_fave_genre:
                    recs_by_genre = recs_by_genre.append(movie)

    return recs_by_genre    

        

# A movie should be added to this list if and only if:

# The user has not watched it
# At least one of the user's friends has watched
# The "genre" of the movie is the same as the user's most frequent genre
# Return the list of recommended movies
# There are also two tests about a get_rec_from_favorites function
# Create a function named get_rec_from_favorites

# takes one parameter: user_data
# user_data will have a field "favorites". The value of "favorites" is a list of movie dictionaries
# This represents the user's favorite movies
# Then, determine a list of recommended movies. A movie should be added to this list if and only if:
# The movie is in the user's "favorites"
# None of the user's friends have watched it
# Return the list of recommended movies

def new_genre_rec_from_empty_watched():
    user_data["watched"] = []   #Due to test arrange section
    pass
# user_data = {
#     "watchlist": [{
#         "title": MOVIE_TITLE_1,
#         "genre": GENRE_1,
#         "rating": RATING_1
#     }],
#     "watched":  [{
#         "title": MOVIE_TITLE_1,
#         "genre": GENRE_1,
#         "rating": RATING_1
#     }]
# }
