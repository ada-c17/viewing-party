# ------------- WAVE 1 --------------------
from tests.test_constants import MOVIE_TITLE_1, RATING_1

#make a dictioary with three parameters if three of them are truthy
#if any of them are none function returns none
def create_movie(title, genre, rating):
    

    new_movie=dict([("title",title),("genre", genre),("rating",rating)])
  
    
    if title is None:
        return None
    if genre is None:
        return None
    if rating is None:
        return None
    return new_movie

#This function needs to add movie to the watched list inside the user_data
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
#This function needs to add movie to the watchlist inside the user_data
def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data
#If title in watchlist remove and add to watched. Else return user data as is.
def watch_movie(user_data,title):
    for i in user_data["watchlist"]:
        if i["title"]==title:
            user_data["watched"].append(i)
            user_data["watchlist"].remove(i)
    return user_data
    # 
# ----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
#calculate the average rating of user watched list. if watched is empty return 0.
def get_watched_avg_rating(user_data):
    test_list=user_data["watched"]
    ress =  [i["rating"] for i in test_list]
    if len(ress)==0:
        return 0
    else:
        return sum(ress)/len(ress)

#  Determine which genre is most frequently occurring in the watched list. Return that. if watched is empty return None.
def get_most_watched_genre(user_data):
    User_watched_movies=user_data["watched"]
    Users_watched_genre =  [i["genre"] for i in User_watched_movies]
    frequency={}
    if len(User_watched_movies)>0:

        for item in Users_watched_genre:
            if item in frequency:
                frequency[item] += 1
            else:
                frequency[item] = 1
        fav_genre = max(frequency, key=frequency.get)
        return fav_genre
    else:
        return None
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

#what title you can see in user's watched list that cant see in friends watched list
# add them to a new list of movie dictionaries 

def get_unique_watched(user_data):
    user_movie = user_data["watched"]
    

    all_friends_movies = []
    for friends_list in user_data['friends']:
        all_friends_movies+=friends_list['watched']

    not_common = []
    for elements in user_movie:
        if elements not in all_friends_movies:
            not_common.append(elements)

    return not_common
#look at friends watched and users watched. detrmi what movies friends watched but user didnt watch and add them to alist.

def get_friends_unique_watched(user_data):
    user_movie = user_data["watched"]

    all_friends_movies = []
    for friends_list in user_data['friends']:
        all_friends_movies+=friends_list['watched']

    not_common = []
    for elements in all_friends_movies:
        if elements not in user_movie:
            if elements not in not_common:#??????????????????
                not_common.append(elements)

    return not_common
    

# ------------- WAVE 4 --------------------
# -----------------------------------------
#We want a list of movies that user hasnt watched
#at least one of the friends have watched
#if the streaming company is in the list of subscribtions
#add that movies to a new list


def get_available_recs(user_data):
    uniq_friends= get_friends_unique_watched(user_data)
    host=user_data["subscriptions"]
    available_recs=[]
    for i in uniq_friends:
       if i['host'] in host:
        #    if i not in available_recs:
            available_recs.append(i)
    return available_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

#a a movie should be added to recommended list if user hasnt watched but friends have watched(uniq_friends).This time genre is the same as users favorite genre
def get_new_rec_by_genre(user_data):
    recommended_list=[]
    fav_genre = get_most_watched_genre(user_data)
    uniq_friends= get_friends_unique_watched(user_data)
    for i in uniq_friends:
        if i["genre"] == fav_genre:
            recommended_list.append(i)
    return recommended_list


#a list dictionary of movies of the list favorites in user's data that are uniq to the user 
def get_rec_from_favorites(user_data):
    user_recom=[]
    users_uniq= get_unique_watched(user_data)
    for i in user_data["favorites"]:
        if i in users_uniq:
            user_recom.append(i)
    return user_recom



