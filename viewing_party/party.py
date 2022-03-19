"""
Project1: viewing party
3/19/2022
Goal: Being able to read tests to understand what is expected of our program is 
a skill that needs to be developed.
 """
 
# ------------- WAVE 1 --------------------
#1
def create_movie(title, genre, rating):
    movie_dict = {}
    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else:
        return None
#2  {"watched":[{},{}...]}   
def add_to_watched(user_data, movie):
    for movie_value in user_data.values():
        movie_value.append(movie)
        return user_data
    
#3  {"watched":[{},{}...], "watchlist":[{},{}]}      
def add_to_watchlist(user_data, movie):
    for value in user_data.values():
        value.append(movie)
        return user_data
    
#4  {"watched":[{},{}...], "watchlist":[{},{}]}    
# user_data = {'watched': ['It Came from the Stack Trace'], 'watchlist': []}, 
# title = 'It Came from the Stack Trace'
def watch_movie(user_data, title):
    for key, value in user_data.items():
        for i in range(len(value)):
            if title == value[i]["title"]:
                del value[i]
                user_data["watched"].append(title)
                return user_data
            
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
#user_data is a dictionary with a "watched" list of movie dictionaries
#{"watched":[{},{},{}]
#is there a better way to find lengh of value
def get_watched_avg_rating(user_data):
    #try:
        total = 0
        count = 0
        
        for key, value in user_data.items():
            for i in range(len(value)):
                total += value[i]["rating"]
                count += 1
        if count != 0:
            return total / count
        else:
            return 0.0
        #option: try, except ZeroDivisionError:
        #print("List is empty, the rating can't divide by 0!")
        
def get_most_watched_genre(user_data):
    len_watched = 0
    genre_frequency = {}
    most_freq, genre_result = 0, ""
    for value in user_data.values():
        len_watched = len(value)
        if len_watched == 0:
            return None
        else:
            for i in range(len(value)):
                genre = value[i]["genre"]
                #if genre not in genre_frequency:
                genre_frequency[genre] = genre_frequency.get(genre, 0) +1
                #genre_frequency[genre] += 1 KeyError
                if genre_frequency[genre] >= most_freq:
                    most_freq, genre_result = genre_frequency[genre], genre
    
        return genre_result
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
#the value of user_data will be a dictionary with a "watched" list of movie dictionaries, and a "friends"
#This represents that the user has a list of watched movies and a list of friends
#{"watched":[{},{},{}], "friends": [{"watched":[{},{},{}]}, "watched":[{},{}]}
#Consider the movies that the user has watched, and consider the movies that their friends have watched. 
#Determine which movies the user has watched, but none of their friends have watched.
def get_unique_watched(user_data):
    user, friends = {}, []
    user, friends =  get_unique_helper(user_data)
    unique_movies_from_user = []
    for value in user.values():
        if value not in friends:
            unique_movies_from_user.append(value)
    return unique_movies_from_user    

#Consider the movies that the user has watched, and consider the movies that their friends have watched. 
#Determine which movies at least one of the user's friends have watched, but the user has not watched.
def get_friends_unique_watched(user_data):
    user, friends = {}, []
    user, friends =  get_unique_helper(user_data)
    unique_movies_from_friends = []
    list_of_user_watched = []
    
    for value in user.values():
        list_of_user_watched.append(value)
        
    for dict in range(len(friends)):
        if friends[dict] not in list_of_user_watched:
            unique_movies_from_friends.append(friends[dict])
    return unique_movies_from_friends            

#helper function
def get_unique_helper(user_data):
    user_movies_dict = {}
    friends_movies_dict = {}
    friends_list = []
    result_dict = {}
    for value in user_data.values():
        if value == user_data["watched"]:
            for i in range(len(user_data["watched"])):
                user_movies_dict[i] = value[i]
        elif value == user_data["friends"]:
            for watched_key in value:#["watched":[{},{}], "watched":[{},{}]]
                #print(watched_key)
                for movie_values_list in watched_key["watched"]:
                        if movie_values_list not in friends_list:
                            friends_list.append(movie_values_list)
            
    return user_movies_dict, friends_list


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
    for dict in friends_unique:
        for list_of_host in user_data["subscriptions"]:
            if dict["host"] in list_of_host:
                recommended_list.append(dict)
    return recommended_list            
          
    
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
""" 
Consider the user's most frequently watched genre. Then, determine a list of recommended movies. 
return a list of recommended movies by genre:
1. The user has not watched it
2. At least one of the user's friends has watched
3. The "genre" of the movie is the same as the user's most frequent genre
"""
def get_new_rec_by_genre(user_data):
    recommended_genre_list = []
    genre_dict = {}
    genre_dict = get_most_watched_genre(user_data)
    #print(genre_dict)
    
    list_from_friends = get_friends_unique_watched(user_data)
    #print(list_from_friends)
    if len(list_from_friends) == 0:
        return []
    else:
        for dict in list_from_friends:
            if genre_dict is not None:
                if genre_dict in dict["genre"]:
            #print(genre_dict)
                    recommended_genre_list.append(dict)
            else:
                return []
    return recommended_genre_list

"""
structure: {"watched":[{}], "friends":["watched":[{},{}], "watched":[{"host":"" ...},{}] ..., "subscription":["","",..]], "favorates":[{},{}]}
return a list of recommendate movies:
1. The movie is in the user's "favorites"
2. None of the user's friends have watched it
"""
def get_rec_from_favorites(user_data):
    recommended_favorites = []
    unique_list_from_user = []
    unique_list_from_user = get_unique_watched(user_data)
    for list in user_data["favorites"]:
        if list is not None:
            for movie in unique_list_from_user:
                if movie  == list:
                    recommended_favorites.append(list)
    return recommended_favorites

            
#Below comment is for my own referrence and record of wave03 functions
#misundersting of return value caused wrong approach and code 
#set(dictionary) causes KeyError, set is immutable
#get_unique_watched(user_data)          
# def get_unique_watched(user_data):
#     user_movies = set()
#     friend_movies = set()
#     list_of_dictionary_user = []
#     list_of_dictionary_friends = []
#     for value in user_data.values(): 
#         if value == user_data["watched"]: #6 movies user watched
#             #print(value)
#             len_my_watched = len(value)
#             #print(len_my_watched) 
#             if len_my_watched > 0:
#                 for i in range(len_my_watched):
#                     #user_movies.add(value[i]["title"])
#                     #print(user_movies)
#                     print(value[i])
#                     list_of_dictionary_user.append(value[i])
#             else:
#                 return list_of_dictionary_friends
#         else:
#             #have friends' list of movie dict [{"watched":[{},{},{}]}, "watched":[{},{}]}]
#             #print(value)
#             for dict in value:
#                 watched_each_in_list = dict["watched"] 
#                 len_movie = len(watched_each_in_list)
#                 #print(len_movie) #4 movies in each friend's watched list
#                 if len_movie > 0:
#                     for index in range(len_movie):
#                         #friend_movies.add(watched_each_in_list[index]["title"]) #7 unique movies in set now
#                         #print(friend_movies)
#                         #print(watched_each_in_list[index])
#                         list_of_dictionary_friends.append(watched_each_in_list[index])
                        
#                 else:
#                     return list_of_dictionary_user
#     #Return a list of dictionaries, that represents a list of movies
#     #print(list_of_dictionary_user  - list_of_dictionary_friends)
#     return (set(list_of_dictionary_user) - set(list_of_dictionary_friends)) ####didn't print the whole {} but title TypeError: unhashable type: 'dict'

# #Consider the movies that the user has watched, and consider the movies that their friends have watched. 
# # Determine which movies at least one of the user's friends have watched, but the user has not watched.
# def get_friends_unique_watched(user_data):
#     user_movies = set()
#     friend_movies = set()
#     list_of_dictionary_user = []
#     list_of_dictionary_friends = []
#     for value in user_data.values(): 
#         if value == user_data["watched"]: #6 movies user watched
#             #print(value)
#             len_my_watched = len(value)
#             #print(len_my_watched) 
#             if len_my_watched > 0:
#                 for i in range(len_my_watched):
#                     user_movies.add(value[i]["title"])
#                     #print(user_movies)
#                     list_of_dictionary_user.append(value[i])
#             else:
#                 return list(friend_movies)
#         else:
#             #have friends' list of movie dict [{"watched":[{},{},{}]}, "watched":[{},{}]}]
#             #print(value)
#             for dict in value:
#                 watched_each_in_list = dict["watched"] 
#                 len_movie = len(watched_each_in_list)
#                 #print(len_movie) #4 movies in each friend's watched list
#                 if len_movie > 0:
#                     for index in range(len_movie):
#                         friend_movies.add(watched_each_in_list[index]["title"]) #7 unique movies in set now
#                         #print(friend_movies)
#                         list_of_dictionary_friends.append(watched_each_in_list[index])
                        
#                 else:
#                     return list(user_movies)
#     #Return a list of dictionaries, that represents a list of movies
#     #no unique movies from friends:
#     if friend_movies.issubset(user_movies):
#         return []
#     else:
#         return friend_movies-user_movies
