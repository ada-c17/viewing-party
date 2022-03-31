# ------------- WAVE 1 --------------------
MOVIE_TITLE_1 = "It Came from the Stack Trace"
GENRE_1 = "Horror"
RATING_1 = 3.5

def create_movie(title, genre, rating):
    movie_dict= {}
    if title == None: 
        return None
    elif genre == None: 
        return None
    elif rating == None: 
        return None 
    else:  
        movie_dict["title"]= title
        movie_dict["genre"]= genre
        movie_dict["rating"] = rating
        return movie_dict
    
# print(create_movie(MOVIE_TITLE_1, GENRE_1, RATING_1))
# watched= {watchlist:[[{"title":"Up"},{"title": "dookey"},{"title"= "Air Bud"}], watched[{"title":" Alice in wonderland" }]}
def add_to_watched(user_data, movie):
    if movie: 
        user_data['watched'].append(movie)
        return user_data
    return None

# print(add_to_watched(user_data, movie))


def add_to_watchlist(user_data, movie):
        if movie : 
            user_data["watchlist"].append(movie)
            return user_data
        return None


# watched= {watchlist:[[{"title":"Up"},{"title": "dookey"},{"title"= "Air Bud"}], watched[{"title":" Alice in wonderland" }]}

def watch_movie(user_data, title):
    if title: 
        if user_data['watchlist']:
            watchlist_data = user_data['watchlist']
            for item in watchlist_data: 
                if item['title'] == title: 
                    watchlist_data.remove(item)
                    watched_data = user_data["watched"]
                    watched_data.append(item)
        return user_data
    return None


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_data = user_data['watched']
    average_rating = []
    total_rating = 0 
    if watched_data == []:
        return 0.0
    elif watched_data:
        for movie in watched_data: 
            average_rating.append(movie['rating'])
        for rating in average_rating:
            total_rating += rating 
        average = float(total_rating/ len(average_rating))
        return average



    # Psudo code
    # takes in user_data
    # user_data_structure: {watched:[{movie:title, genre:type, rating:number}{}{}]}
    # if watch list is empty --> return 0.0 
    # go into watched list and get movie ratings
    # Append values to list
    # In loop add all ratings 
    # len list to get denom for average
    # return average rating


import statistics 
from statistics import mode
def get_most_watched_genre(user_data):
# psudo
# access watched
# count how many of each genre in dictrionary 
# return most frequently watched 
# if emtpy return none 


    watched_data = user_data["watched"]
    genre_list= []
    if watched_data == []:
        return None
    for movie in watched_data:
        if movie['genre']: 
            genre_list.append(movie['genre'])
        most_watched_genre = mode(genre_list)
        return most_watched_genre
        




# -----------------------------------------
# ------------- WAVE 3 --------------------

# 1. The first two tests are about a `get_unique_watched()` function.

# In `party.py`, there should be a function named `get_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
# - Return a list of dictionaries, that represents a list of movies


# -----------------------------------------
def get_unique_watched(user_data):
    # Psudo
    # user_data = {watched: [{movie}{movie}], friends:[{watched:[{movie}]}[watched:{movie}][{watched:{movie}}]]}
    # access watched and friends watched
    # compare dictionaries--> if they have the title that is not in the other list
    # append list with  movies if True
    # titles in users watched to titles friends have not watched
    # user_watched = user_data['watched']
    # print(user_data)


    user_watched = user_data['watched']
    list_friends = user_data['friends']
    user_unique = []

    for movie in user_watched:
        if is_movie_unique(movie,list_friends):
            user_unique.append(movie)
    return(user_unique)

def is_movie_unique(movie, list_of_friends):
    for friend in list_of_friends:
        if movie in friend["watched"]:
            return False
    return True
    
        



# 2. The next three tests are about a `get_friends_unique_watched()` function.

# In `party.py`, there should be a function named `get_friends_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
# - Return a list of dictionaries, that represents a list of movies
def get_friends_unique_watched(user_data):

    user_watched = user_data['watched']
    list_friends = user_data['friends']
    friends_unique = []
 

    for friend in list_friends: 
        for movie in friend['watched']:
            if is_friends_movie_unique(movie, user_watched) and movie not in friends_unique:
                friends_unique.append(movie)
    return(friends_unique)

def is_friends_movie_unique(movie, user_watched_list):
    if movie in user_watched_list:
        return False
    else:
        return True




 

# -----------------------------------------
# ------------- WAVE 4 --------------------
# 1. There are four tests about a `get_available_recs` function

# Create a function named `get_available_recs`

# - takes one parameter: `user_data`
#   - `user_data` will have a field `"subscriptions"`. The value of `"subscriptions"` is a list of strings
#     - This represents the names of streaming services that the user has access to
#     - Each friend in `"friends"` has a watched list. Each movie in the watched list has a `"host"`, which is a string that says what streaming service it's hosted on
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
# - Return the list of recommended movies
# -----------------------------------------
def get_available_recs(user_data):
    
    subs = user_data["subscriptions"]
    avail_recs = []
    no_recs = []
    if get_friends_unique_watched == []:
        return no_recs
    else:
        for streaming_services in subs:
            for unique_movie in get_friends_unique_watched(user_data):
                if streaming_services == unique_movie['host']:
                    avail_recs.append(unique_movie)
        return avail_recs

    



# -----------------------------------------
# ------------- WAVE 5 --------------------
# 1. There are four tests about a `get_new_rec_by_genre` function

# Create a function named `get_new_rec_by_genre`

# - takes one parameter: `user_data`
# - Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"genre"` of the movie is the same as the user's most frequent genre
# - Return the list of recommended movies

# -----------------------------------------


def get_new_rec_by_genre(user_data):
    # find users most watched genre
    # add movies to watch list if user hasnt watched it , a friend has watched it, genre matches most watched
    # return list of movies 
    rec_by_genre = []
    no_recs= []
    genre = get_most_watched_genre(user_data)
    movie_list = get_friends_unique_watched(user_data)
    if movie_list == []:
        return no_recs 
    else: 
        for movie in movie_list:
            if genre == movie['genre']:
                rec_by_genre.append(movie)
            return rec_by_genre

# 2. There are also two tests about a `get_rec_from_favorites` function

# Create a function named `get_rec_from_favorites`

# - takes one parameter: `user_data`
#   - `user_data` will have a field `"favorites"`. The value of `"favorites"` is a list of movie dictionaries
#     - This represents the user's favorite movies
# - Then, determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The movie is in the user's `"favorites"`
#   - None of the user's friends have watched it
# - Return the list of recommended movies
def get_rec_from_favorites(user_data):
    favorite_recs = []
    user_unique = get_unique_watched(user_data)
    user_faves= user_data["favorites"]
    no_recs = []

    for movies in user_faves:
        if user_unique == []:
            return no_recs
        elif movies in user_unique:
            favorite_recs.append(movies)
    return favorite_recs




    
