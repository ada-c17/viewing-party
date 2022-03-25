# ------------- WAVE 1 --------------------
from tests.test_constants import *
def create_movie(movie_title, genre, rating):
    if movie_title == None or genre == None or rating == None:
        return None
    else:
        new_movie = {"title":MOVIE_TITLE_1,"genre":GENRE_1,"rating":RATING_1}
        return new_movie

def add_to_watched(user_data, movie):
    user_data = {"watched":[{"title":MOVIE_TITLE_1, "genre":GENRE_1, "rating":RATING_1}]}
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {"watchlist": [{"title":MOVIE_TITLE_1,"genre":GENRE_1,"rating":RATING_1}]}
    return user_data

def watch_movie(janes_data, movie_title1):

    movie_data = {"title": movie_title1 , "genre": GENRE_1, "rating": RATING_1 }
    for i in janes_data["watchlist"]:
        if movie_data in janes_data["watchlist"]:
            janes_data["watchlist"].remove(movie_data)
            janes_data["watched"].append(movie_data)
            return janes_data
    return janes_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(janes_data):
    total_rating = 0
    counter = 0
    if janes_data["watched"] == []:
        average = 0.0
        return average
    else:
        for val in USER_DATA_2.values():
            for dict in val:
                for key in dict:
                    if key == "rating":
                        total_rating += dict[key]
                        counter+= 1
        average = total_rating/counter
        return average 

def get_most_watched_genre(janes_data):
    
    genre_dict ={}
    
    if janes_data["watched"] == []:
        popular_genre = None
        return popular_genre
    else:                  
        for watched_items in USER_DATA_2.values():
            for movie_data in watched_items:
                key = movie_data["genre"]
                if key not in genre_dict:
                    genre_dict[key]= 1 
                else:
                    genre_dict[key] +=1
    popular_genre = max(genre_dict,key=genre_dict.get)
    return popular_genre
    
        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(amandas_data):
    amandas_unique_movies =[]
    list_friends = []
    list_amandas = []

    for element in amandas_data["friends"]:
        for movie_data in element["watched"]:
            list_friends.append(movie_data)
    
    
    for element in amandas_data["watched"]:
        list_amandas.append(element)

    
    for element in list_amandas:
        if element not in list_friends:
            amandas_unique_movies.append(element)

    return amandas_unique_movies

def get_friends_unique_watched(amandas_data):
    friends_unique_movies =[]
    list_friends = []
    list_amandas = []

    for element in amandas_data["friends"]:
        for movie_data in element["watched"]:
                list_friends.append(movie_data)
    
    
    for element in amandas_data["watched"]:
            list_amandas.append(element)
  

    for element in list_friends:
        if element not in list_amandas:
            if element not in friends_unique_movies:
                friends_unique_movies.append(element)
    
    return friends_unique_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(amandas_data):

    rec_list = []
    friends_unique_movies =[]
    list_friends = []
    list_amandas = []

    for element in amandas_data["friends"]:
        for movie_data in element["watched"]:
                list_friends.append(movie_data)
    
    
    for element in amandas_data["watched"]:
            list_amandas.append(element)


    for element in list_friends:
        if element not in list_amandas:
            friends_unique_movies.append(element)

    for movie in friends_unique_movies:
        if movie["host"] in amandas_data ["subscriptions"]:
            rec_list.append(movie)
    
    return rec_list
    
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(sonyas_data):
    rec_list_genre = []
    friends_unique_movies =[]
    list_friends = []
    list_sonyas = []
    fav_genre = []

    for element in sonyas_data["friends"]:
        for movie_data in element["watched"]:
            list_friends.append(movie_data)
    
    if len (sonyas_data["watched"])== 0:
        return rec_list_genre
    for element in sonyas_data["watched"]:
        list_sonyas.append(element)

    if len(list_friends) == 0:
        return rec_list_genre
    for element in list_friends:
        if element not in list_sonyas:
            friends_unique_movies.append(element)

    for movie in sonyas_data["favorites"]:
        fav_genre.append(movie["genre"])

    
    for movie in friends_unique_movies:
        if movie["host"] in sonyas_data ["subscriptions"]:
            if movie["genre"] in fav_genre:
                rec_list_genre.append(movie)

    return rec_list_genre
    
def get_rec_from_favorites(sonyas_data):

    rec_list_fav = []
    sonyas_unique_movies =[]
    list_friends = []
    list_sonyas = []

    for element in sonyas_data["friends"]:
        for movie_data in element["watched"]:
            list_friends.append(movie_data)
    
    
    for element in sonyas_data["watched"]:
        list_sonyas.append(element)

    
    for element in list_sonyas:
        if element not in list_friends:
            sonyas_unique_movies.append(element)

    for movie in sonyas_unique_movies:
        if movie not in list_friends:
            rec_list_fav.append(movie)

    return rec_list_fav

