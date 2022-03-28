from tests.test_constants import *

# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
  
   keys = ["title", "genre", "rating"]
   values = [movie_title, genre, rating]
   new_movie = {}
    
   if movie_title == None:
       return None
   if genre == None:
       return None
   if rating == None:
       return None
   for index in  range(len(values)):
       new_movie [keys[index]] = values[index]
   return new_movie   

def add_to_watched(user_data, movie):
    user_data = {
        "watched": [] 
     }
    new_list = [ ]
    new_list.append(movie)
    
    user_data["watched"]= new_list
    return user_data


def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": []
    }
    new_list = [ ]
    new_list.append(movie)

    user_data["watchlist"]= new_list
    return user_data

def watch_movie(user_data, MOVIE_TITLE_1):
    user_data = {
        "watchlist": [{
            "title": MOVIE_TITLE_1,
            "genre": "GENRE_1",
            "rating": "RATING_1"
        }],
        "watched": []
    }

    watched_movie = []

    
    
    for i in range(len("watchlist")): 
        if MOVIE_TITLE_1 == user_data["watchlist"][i]["title"]:
            watched_movie.append(user_data["watchlist"][i])
            user_data["watched"]= watched_movie
            del user_data["watchlist"][0]
            return user_data

    else:
        return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    if user_data["watched"] == []:
         average = 0.0
         return average
    else:
        for  value in user_data.values():   
            ratings =[]
            rate_list= value[0]
            ratings.append(rate_list["rating"])
            rate_list= value[1]
            ratings.append(rate_list["rating"])
            rate_list= value[2]
            ratings.append(rate_list["rating"])
            rate_list= value[3]
            ratings.append(rate_list["rating"])
            rate_list= value[4]
            ratings.append(rate_list["rating"])
            rate_list= value[5]
            ratings.append(rate_list["rating"])
            average = sum(ratings)/ len(ratings)
            return average

def get_most_watched_genre(user_data):
    genre_count = {}
    if user_data["watched"] == []:
        most_watched = None
        return most_watched
        
    else:
        for movie in user_data["watched"]:
            if movie["genre"] not in genre_count.keys():
                genre_count[movie["genre"]] = 1
            elif movie["genre"] in genre_count.keys():
                genre_count[movie["genre"]] += 1
        most_watched = max(genre_count, key=genre_count.get)
        return most_watched



 

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

user_watched= [FANTASY_1,
                FANTASY_2,
                FANTASY_3,
                ACTION_1,
                INTRIGUE_1,
                INTRIGUE_2,
]

first_friend_watched_data = [
                FANTASY_1,
                FANTASY_3,
                FANTASY_4,
                HORROR_1
               
            ]
second_friend_watched_data = [ FANTASY_1,
                ACTION_1,
                INTRIGUE_1,
                INTRIGUE_3,
                ]
def get_unique_watched(user_data):
    unique_list = [] 
    comparison_1 =[]
    comparison_2 =[]
    for movie in user_data["watched"]:
        if movie not in first_friend_watched_data:
            comparison_1.append(movie)
    for movie in user_data["watched"]:
        if movie  not in second_friend_watched_data:
            comparison_2.append(movie)
    for movie in comparison_2:
        if movie in comparison_1 and comparison_2:
           unique_list.append(movie)
    return unique_list
    

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"]:
                friends_unique_movies.append(movie)
    
    return friends_unique_movies 
  
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


user_watched = []
friends_watched = []
comparison_list =[]
recommendations = []
def get_available_recs(user_data):
    if user_data["watched"] == []:
        return recommendations
    else:

        for i in range(len(user_data["watched"])):
            # user_watched = user_data["watched"][i]
            user_watched.append(user_data["watched"][i])
        for i in range(len(user_data["friends"])):
            for j in range(len(user_data["friends"][i]["watched"])):
                friends_watched.append(user_data["friends"][i]["watched"][j])
            # user_watched.append(user_data["watched"][i])
        for movie in friends_watched:
            if movie not in user_watched:
                comparison_list.append(movie)
        for movie in comparison_list:
            if movie["host"] in user_data["subscriptions"]:
                recommendations.append(movie)
        # print(f"friends watched: {friends_watched}")
        return recommendations
    


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

new_list= []
recommendations_list = []
def get_new_rec_by_genre(USER_DATA_5):
    for friend in USER_DATA_5["friends"]:
        for movie in friend["watched"]:
            if movie not in USER_DATA_5["watched"] and movie not in new_list:
                new_list.append(movie)
        for movie in new_list:
            if movie["genre"]== "Fantasy":
                recommendations_list.append(movie)
    return recommendations_list

def get_rec_from_favorites(user_data):
    favorites_rec = []
    user_watched_list = get_unique_watched(user_data)
    for movie in user_watched_list:
        if movie in user_data["favorites"]:
            favorites_rec.append(movie)
    return favorites_rec