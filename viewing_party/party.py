# ------------- WAVE 1 --------------------

# this is a test change

from audioop import avg


def create_movie(title, genre, rating):
    if (title == None) or (genre == None) or (rating == None):
       return None
    else:
        created_movie_dict = {}
        created_movie_dict["title"] = title
        created_movie_dict["genre"] = genre
        created_movie_dict["rating"] = rating
        return created_movie_dict
    
    
def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    user_data["watchlist"][0]["title"] = movie["title"]
    return user_data

# In `party.py`, there should be a function named `watch_movie`. This function should...

# - take two parameters: `user_data`, `title`
#   - the value of `user_data` will be a dictionary with a `"watchlist"` and a `"watched"`
#     - This represents that the user has a watchlist and a list of watched movies
#   - the value of `title` will be a string
#     - This represents the title of the movie the user has watched
# - If the title is in a movie in the user's watchlist:
#   - remove that movie from the watchlist
#   - add that movie to watched
#   - return the `user_data`
# - If the title is not a movie in the user's watchlist:
#   - return the `user_data`

def watch_movie(user_data, title):
    if user_data["watchlist"][0]["title"] == title:
        user_data["watchlist"].remove(user_data["watchlist"][0])
        user_data["watched"].append(title)
        return user_data
    else:
        return user_data

# def watch_movie(user_data, title):
#     if user_data["watchlist"][0]["title"] == title:
#         specific_title = user_data["watchlist"][0]["title"]
#         user_data["watchlist"].remove(specific_title)
#         user_data["watched"].append(user_data["watchlist"])
#     else:
#         return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    rating_sum = 0
    for key in user_data:
        if len(user_data["watched"]) == 0:
            return 0
        for index in range(len(user_data["watched"])):
            if user_data["watched"] == []:
                return 0
            else:
                rating_sum +=  user_data["watched"][index]["rating"]
        avg_rating = rating_sum/(len(user_data["watched"]))
    return avg_rating
            
            
'''
- take one parameter: `user_data`
- the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries. 
    Each movie dictionary has a key `"genre"`.
    - This represents that the user has a list of watched movies. Each watched movie has a genre.
    - The values of `"genre"` is a string.
- Determine which genre is most frequently occurring in the watched list
- return the genre that is the most frequently watched
- If the value of "watched" is an empty list, `get_most_watched_genre` should return `None`.
'''

def get_most_watched_genre(user_data):
    genres_dict = {}
    for key in user_data:
        if user_data["watched"] == []:
            return None
        for index in range(len(user_data["watched"])):
            # if "genre" in user_data["watched"][index]:
            if user_data["watched"][index]["genre"] not in genres_dict:
                genres_dict[user_data["watched"][index]["genre"]] = 1   
            else:
                genres_dict[user_data["watched"][index]["genre"]] += 1
    max_genre = max(genres_dict, key=genres_dict.get)
    return max_genre
    
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
'''
- the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
    - This represents that the user has a list of watched movies and a list of friends
    - The value of `"friends"` is a list
    - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
    - Each movie dictionary has a `"title"`.
- Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
- Return a list of dictionaries, that represents a list of movies
'''

def get_unique_watched(user_data):
    friends_movie_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movie_list:
                friends_movie_list.append(movie)
    watched_list = []
    for movie in user_data["watched"]:
        if movie not in friends_movie_list:
            watched_list.append(movie)
    return watched_list
                
        
def get_friends_unique_watched(user_data):
    friends_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_list:
                friends_list.append(movie)
    only_friends_list = []
    for movie in friends_list:
        if movie not in user_data["watched"]:
            only_friends_list.append(movie)
    
    return only_friends_list


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    movies_friends_watched = get_friends_unique_watched(user_data)
    for movie in range(len(movies_friends_watched)):
        if movies_friends_watched[movie]["host"] in user_data["subscriptions"]:
            recommended_movies.append(movies_friends_watched[movie])
    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    list_by_genre = []
    friends_movies = get_friends_unique_watched(user_data)
    for movie in range(len(friends_movies)):
        if friends_movies[movie]["genre"] == get_most_watched_genre(user_data):
            list_by_genre.append(friends_movies[movie])
    return list_by_genre
