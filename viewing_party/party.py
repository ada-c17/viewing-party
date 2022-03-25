from doctest import ELLIPSIS
from pickle import NONE

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if title and genre and rating:
        new_movie = {"title" : title, "genre" : genre, "rating":rating }
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for num_movies in range(len(user_data["watchlist"])):
        if user_data["watchlist"][num_movies]["title"] == title: 
            movie = user_data["watchlist"].pop(num_movies)
            user_data["watched"].append(movie)
            break        
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    addition = 0
    if len(user_data["watched"])>=1: 
        for num_movies in range(0,len(user_data["watched"])):
            addition += user_data["watched"][num_movies]["rating"]
        average = addition/ len(user_data["watched"])
    else:
        average = 0.0
    return average


def get_most_watched_genre(user_data):
    genre_dict = {}
    
    
    for movie in user_data["watched"]:
        genre_var = movie["genre"]
        if genre_var in genre_dict:
            genre_dict[genre_var] +=1
        else:
            genre_dict[genre_var] = 1   

    popular_genre = None
    counter_genre = 0
    for genre in genre_dict:
        if genre_dict[genre] > counter_genre:
            popular_genre = genre
            counter_genre = genre_dict[genre] 
            

    return popular_genre 

        


    


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
   
    # index_movies = 0
    # unique_set = set()
    # user_set = set(user_data["watched"])
    # for friend in range (len(user_data["friends"])):
    #     unique_set = set(user_data["frieds"][friend]["watched"]) | unique_set
    # return user_set - unique_set


    # create a dictionary with all movies and use title as a key.
    # Keys(titles) will be used as elements/items for create two sets. 
    # One is for Amanda and the other one for the rest of their friends.
    # return amanda_set - friend_set 
    # Create a list with all movies from the remaining  set

    
    movie_dict = {} #Complete library of movies
    user_set = set() #Set of Amanda (user) has watched.
    friend_set = set() #Sets of users friends has watched.
    unique_list =[] # a list of the difference of users watched and friends watched.
    
    for movie in user_data["watched"]:
        movie_dict[movie["title"]] = movie
        user_set.add(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            movie_dict[movie["title"]] = movie
            friend_set.add(movie["title"])

    unique_set = user_set - friend_set
    friends_unique_set = friend_set - user_set

    for movies in unique_set :
        unique_list.append (movie_dict[movies])
    
    return unique_list 

def get_friends_unique_watched(user_data):
    
    movie_dict = {} #Complete library of movies
    user_set = set() #Set of Amanda (user) has watched.
    friend_set = set() #Sets of users friends has watched.
    unique_list =[] # a list of the difference of users watched and friends watched.
    
    for movie in user_data["watched"]:
        movie_dict[movie["title"]] = movie
        user_set.add(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            movie_dict[movie["title"]] = movie
            friend_set.add(movie["title"])  
    
    friends_unique_set = friend_set - user_set

    for movies in friends_unique_set :
        unique_list.append (movie_dict[movies])
    
    return unique_list 
    


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    
    movie_dict = {} #Complete library of movies
    user_set = set() #Set of Amanda (user) has watched.
    friend_set = set() #Sets of users friends has watched.
    unique_list =[] # a list of the difference of users watched and friends watched.
    
    for movie in user_data["watched"]:
        movie_dict[movie["title"]] = movie
        user_set.add(movie["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            movie_dict[movie["title"]] = movie
            friend_set.add(movie["title"])  
    
    friends_unique_set = friend_set - user_set


    for movies in friends_unique_set :
        if movie_dict[movies]["host"] in user_data["subscriptions"]:
            unique_list.append(movie_dict[movies])
    
    return unique_list 



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

