"""
Project1: viewing party
3/19/2022
Goal: 1. Use Test-Driven-Development approach to implement movie recommendation program. 
      2. Practice data structures like (nested)dictionary, list, set, and control flow and manipulating given data
      3. Reuse function code and write helper function
      4. Debug, pytest, refactor code
 """
 
# ------------- WAVE 1 --------------------
#1
from collections import Counter
from curses.panel import top_panel


def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None 
    else:
        return {"title": title, "genre": genre, "rating": rating}
        
#2  {"watched":[{},{}...]}   
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    
#3  {"watched":[{},{}...], "watchlist":[{},{}]}      
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
    
#4  {"watched":[{},{}...], "watchlist":[{},{}]}    
# user_data = {'watched': ['It Came from the Stack Trace'], 'watchlist': []}, 
# title = 'It Came from the Stack Trace'
def watch_movie(user_data, title):  
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
#user_data is a dictionary with a "watched" list of movie dictionaries
#{"watched":[{},{},{}]
def get_watched_avg_rating(user_data):
    rating_list = []
    for movie in user_data["watched"]:
        rating_list.append(movie["rating"])
    total = sum(rating_list) #use sum() vs accumulate myself?
    
    if len(rating_list) != 0:
        return total / len(rating_list)
    else:
        return 0.0
    #try/catch option wors too
     
#{"watched": [{},{},{}...]}
def get_most_watched_genre(user_data):
    genre_fq, max_genre = 0, None
    genre = []
    for movie in user_data["watched"]:
        genre.append(movie["genre"])
    
    genre_dict = Counter(genre)    
    
    for key, value in genre_dict.items():
        if value > genre_fq:
            genre_fq = value
            max_genre = key
    return max_genre
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------\
    
#user data: {"watched": [{},{},...], "friends":[{"watched":[{},{},...]}, {"watched":[{},{},...]}]}
#returna list of dicitonary that user has watched, but not that their friends have watched. 
def get_unique_watched(user_data):
    all_friends_watched = set()
    unique_result = []
    for f_movies in user_data["friends"]: #list of dict
        for i in range(len(f_movies["watched"])):
            all_friends_watched.add(f_movies["watched"][i]["title"])
    #print(all_friends_watched)
    
    for my_movies in user_data["watched"]:
        if my_movies["title"] not in all_friends_watched:
            unique_result.append(my_movies)
    return unique_result   

#return list of dict that friends watched, but the user hasn't watched
def get_friends_unique_watched(user_data):
    all_f_list, f_unique_list = [], []

    for list_add_list in user_data["friends"]:
        all_f_list += (list_add_list["watched"]) #add all friends movies together
        
    for f_movie in all_f_list:
        if f_movie not in user_data["watched"] and f_movie not in f_unique_list:
            f_unique_list.append(f_movie)
        
    return f_unique_list    


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
"""
structure: {"watched":[{}], "friends":["watched":[{},{}], "watched":[{"host":"" ...},{}] ..., "subscription":["","",..]]}
return a list of recommended movies:
1. The user has not watched it
2. At least one of the user's friends has watched
3. The "host" of the movie is a service that is in the user's "subscriptions"
INTRIGUE_3b["host"] = "disney+"
USER_DATA_4["subscriptions"] = ["netflix", "hulu"] 
"""
def get_available_recs(user_data):
    recommended_list = []
    friends_unique = get_friends_unique_watched(user_data)
    #print(friends_unique)
    for movie_dict in friends_unique:
        if movie_dict["host"] in user_data["subscriptions"]:
            recommended_list.append(movie_dict)
    return recommended_list            
          
    
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
""" 
return a list of recommended movies by genre:
1. The user has not watched it
2. At least one of the user's friends has watched
3. The "genre" of the movie is the same as the user's most frequent genre
"""
def get_new_rec_by_genre(user_data):
    recommended_genre_list, genre_dict = [], {}
    genre_dict = get_most_watched_genre(user_data)
    f_recs = get_friends_unique_watched(user_data)  #refactored to O(n)
    for movie in f_recs:
        if movie["genre"] == genre_dict:
            recommended_genre_list.append(movie)
        
    return recommended_genre_list

"""
structure: {"watched":[{}], "friends":["watched":[{},{}], "watched":[{"host":"" ...},{}] ..., "subscription":["","",..]], "favorates":[{},{}]}
return a list of recommendate movies:
1. The movie is in the user's "favorites"
2. None of the user's friends have watched it
"""
def get_rec_from_favorites(user_data):
    recommended_result, friends_watched = [], []
    #user_data["favorites"] == {movie} in [{movie},{movie}]
    for i in range(len(user_data["friends"])): 
        #print(user_data["friends"][i])
        friends_watched = user_data["friends"][i]["watched"]
    
    #movie in favorate movies [{},{},{}]
    for movie in user_data["favorites"]:
        if movie not in friends_watched:
            recommended_result.append(movie)
    print(recommended_result)
    return recommended_result
