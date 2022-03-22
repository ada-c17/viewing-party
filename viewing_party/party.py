# Q: how to use test_constants??
# from viewing_party.tests import test_constants
# ------------- WAVE 1 --------------------
import statistics
user_data = {}

def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        new_movie = {
            "title": movie_title,
            "genre": genre,
            "rating": rating
        }
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"]= [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"]= [movie]
    return user_data

def watch_movie(user_data, movie):
    # already_watched_list = user_data["watched"]
    # to_watch_list = user_data["watchlist"]
    for value in user_data["watchlist"]:
        if value["title"] == movie:
            movie_watched = value
            user_data["watched"].append(movie_watched)
            user_data["watchlist"].remove(movie_watched)
    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_list = []
    for value in user_data["watched"]:
        rating_list.append(value["rating"])
    if rating_list != []:
        average = sum(rating_list)/len(user_data["watched"])
    else:
        average = 0.0
    return average

def get_most_watched_genre(user_data):
    genre_list = []
    for value in user_data["watched"]:
        genre_list.append(value["genre"])
    if genre_list != []:
        popular_genre = statistics.mode(genre_list)
        return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# ----------------------------------------

def get_unique_watched(user_data):
# lists of movies watched by user, and by friends 
    movies_user_watched = []
    movies_friends_watched = []

    # add movie titles to the lists
    for i in range(len(user_data["watched"])):
        movie_title = user_data["watched"][i]['title']
        movies_user_watched.append(movie_title)

    for i in range(len(user_data["friends"])):
        list_of_dicts = user_data["friends"][i]['watched']
        for i in range(len(list_of_dicts)):
            movies_friends_watched.append(list_of_dicts[i]['title'])
    
    # use set to compare the lists, taking the difference between the user's set from the friends set.
    # new_set = set_a - set_b
    unique_user_set = set(movies_user_watched) - set(movies_friends_watched)

    # set of movie titles --> list of dictionaries of those movies
    unique_list_of_dicts = []
    for movie in unique_user_set:
        for i in range(len(user_data["watched"])):
            if movie == user_data["watched"][i]['title']:
                unique_list_of_dicts.append(user_data["watched"][i])

    return unique_list_of_dicts

def get_friends_unique_watched(user_data):
    # lists of movies watched by user, and by friends 
    movies_user_watched = []
    movies_friends_watched = []

    # add movie titles to the lists
    for i in range(len(user_data["watched"])):
        movie_title = user_data["watched"][i]['title']
        movies_user_watched.append(movie_title)

    for i in range(len(user_data["friends"])):
        list_of_dicts = user_data["friends"][i]['watched']
        for i in range(len(list_of_dicts)):
            movies_friends_watched.append(list_of_dicts[i]['title'])

    # difference between sets to find movies ONLY in friends lists
    unique_friends_set = set(movies_friends_watched) - set(movies_user_watched)

    # set of movie titles  --> list of dictionaries of those movies
    unique_list_of_dicts = []
    for list in user_data['friends']:
        for movie in list['watched']:
            if movie['title'] in unique_friends_set and movie not in unique_list_of_dicts:
                unique_list_of_dicts.append(movie)

    return unique_list_of_dicts

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    list_of_recommendations = []
    # find list of movies that friends have watched and user has not
    movies_friends_watched = get_friends_unique_watched(user_data)
        # check if 'host' is in the user's 'subscrptions' list
    for movie in movies_friends_watched:
        if movie['host'] in user_data['subscriptions']:
            list_of_recommendations.append(movie)
    return list_of_recommendations
        
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    fav_genre_rec_list =[]
    # find list of movies that friends have watched and user has not (this is a list of dictionaries)
    movies_friends_watched = get_friends_unique_watched(user_data)
    # most watched genre (this is a string)
    favorite_genre = get_most_watched_genre(user_data)

    for movie in movies_friends_watched:
        if movie['genre'] == favorite_genre:
            fav_genre_rec_list.append(movie)
    return fav_genre_rec_list

def get_rec_from_favorites(user_data):
    # This func returns a list of movie dictionaries. The movie is in the user's "favorites" and
    #  none of the user's friends have watched them
    recommended_list = []

    # make a list of movies watched by friends
    movies_friends_watched = []
    for i in range(len(user_data["friends"])):
        list_of_dicts = user_data["friends"][i]['watched']
        for i in range(len(list_of_dicts)):
            movies_friends_watched.append(list_of_dicts[i])
            
    # if the movies are in the user's fav list and NOT in the friends watched list, add to recommendations
    for movie in user_data['favorites']:
        if movie not in movies_friends_watched:
            recommended_list.append(movie)
    return recommended_list



