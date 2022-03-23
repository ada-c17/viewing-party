# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        print("hello")
        dict = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return dict

    return None

def add_to_watched(user_data, movie):
    user_data_copy = user_data.copy()

    # if movie:
    user_data_copy["watched"].append(movie)

    return user_data_copy

def add_to_watchlist(user_data, movie):
    user_data_copy = user_data.copy()

    user_data_copy["watchlist"].append(movie)

    return user_data_copy

def watch_movie(user_data, title):
    # user_data_copy = user_data.copy()
    for movie_entry in user_data["watchlist"]:
        if movie_entry["title"] == title:
            user_data["watched"].append(movie_entry)
            user_data["watchlist"].remove(movie_entry)

    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum = 0
    # edge case
    if len(user_data["watched"]) == 0:
        return 0.0

    for movie in user_data["watched"]:
        sum += movie["rating"]

    return sum / len(user_data["watched"])

def get_most_watched_genre(user_data):
    # edge case
    if len(user_data["watched"]) == 0:
        return None

    genre_frequency = {}

    # iterate over the list of watched movies
        # if genre key not in dict
            # new_dict[key] = 1
        # else
            # +1
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_frequency:
            genre_frequency[movie["genre"]] = 1
        else:
            genre_frequency[movie["genre"]] += 1

    # print(genre_frequency)
    # return key that has max value in genre frequency
    return max(genre_frequency, key=genre_frequency.get)



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    unique_watched = []
    friend_titles_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            # if movie["title"] in unique_watched:
            #     unique_watched.pop(movie["title"])
            friend_titles_watched.append(movie["title"])

    for movie in user_data["watched"]:
        if movie["title"] not in friend_titles_watched:
            unique_watched.append(movie)

    return unique_watched

def get_friends_unique_watched(user_data):
    friends_watched = []
    friends_unique_watched = []
    user_titles = set()

    # iterate through user list
       # append title to user_watched
    for movie in user_data["watched"]:
        user_titles.add(movie["title"])

    # iterate through user_data of friends
       # if movie["title"] is not in user_titles
           # append movie to friends_unique_watched
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_titles:
                friends_watched.append(movie)

    for i in range(len(friends_watched)):
        if friends_watched[i] not in friends_watched[i+1:]:
            friends_unique_watched.append(friends_watched[i])

    return friends_unique_watched



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    friends_watched = get_friends_unique_watched(user_data)

    # loop through friends unique watched
    for movie in friends_watched:
        # if the movie is in subscriptions list
        if movie["host"] in user_data["subscriptions"]:
            # add it to the output list
            recommended_movies.append(movie)

    return recommended_movies



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

'''
There are four tests about a get_new_rec_by_genre function
Create a function named get_new_rec_by_genre

takes one parameter: user_data
Consider the user's most frequently watched genre. Then, determine a list of recommended movies.
A movie should be added to this list if and only if:
The user has not watched it
At least one of the user's friends has watched
The "genre" of the movie is the same as the user's most frequent genre
Return the list of recommended movies

'''

'''
There are also two tests about a get_rec_from_favorites function
Create a function named get_rec_from_favorites

takes one parameter: user_data
user_data will have a field "favorites". The value of "favorites" is a list of movie dictionaries
This represents the user's favorite movies
Then, determine a list of recommended movies. A movie should be added to this list if and only if:
The movie is in the user's "favorites"
None of the user's friends have watched it
Return the list of recommended movies
'''


def get_new_rec_by_genre(user_data):
    recommended_movies = []
    friends_watched = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)

    for movie in friends_watched:
        if movie["genre"] == most_watched_genre:
            recommended_movies.append(movie)

    return recommended_movies

def get_rec_from_favorites(user_data):
    recommended_movies = []
    friend_titles_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_titles_watched.append(movie["title"])

    for movie in user_data["favorites"]:
        if movie["title"] not in friend_titles_watched:
            recommended_movies.append(movie)

    return recommended_movies