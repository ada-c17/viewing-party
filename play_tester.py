# import source code
from this import d
from viewing_party.party import *

# import test data
from tests.test_constants import *

# import "pretty-print" library
import pprint
pp = pprint.PrettyPrinter(indent=4)

# play testing section
# print("\n-----Wave 01 test data-----")
# pp.pprint(HORROR_1)
# pp.pprint(FANTASY_1)
# pp.pprint(FANTASY_2)

################################################

# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())

### graveyard ###


## WAVE 1 ##
## Create a function that will create a movie function
# with title, genre, and rating into a dictiionary
# If there is no title, genre, or rating, return None
# If any of the three variables is missing, return None

# from decimal import DivisionByZero
# from tests.test_constants import USER_DATA_2

## Create a function to track when movies are watched
## use the new_movie list to generate how the function works
## user_data is what has been "watched:"
## updated_data = add_to_watched(user_data, movie)
## Create a function to track a watch list for the user
## user_data = {"watchlist"}
## updated_data = add_to_watchlist(user_data, movie)


## def a function that will call upon the watched and watchlist functions
##  adjust the values of watched and watchlist into sets
## use set functions to create a set that compares the similarities
## return a set or dictionary that outputs the difference 
## Return an error message if the movie is on neither list
#####################
####WAVE 2 ##########
## Create a function that will check the average rating of movies watched
## if average is Zero, return error message

# '''
# input: a dictionary called 'user_data' with a 'watched' list of
# movie dictionaries (movies that user has watched)
# -- Calculate average rating of all movies user has watched
# -- An empty watch list has an average rating of 0.0
# output: the average rating
# # {   'watched': [   {   'genre': 'Fantasy',
# #                        'rating': 4.8,
# #                        'title': 'The Lord of the Functions: The Fellowship of '
# #                                 'the Function'},
# #                    {   'genre': 'Fantasy',
# #                        'rating': 4.0,
# #                        'title': 'The Lord of the Functions: The Two '
# #                                 'Parameters'},
# #                    {   'genre': 'Fantasy',
# #                        'rating': 4.0,
# #                        'title': 'The Lord of the Functions: The Return of the '
# #                                 'Value'},
# #                    {   'genre': 'Action',
# #                        'rating': 2.2,
# #                        'title': 'The JavaScript and the React'},
# #                    {'genre': 'Intrigue', 'rating': 2.0, 'title': 'Recursion'},
# #                    {   'genre': 'Intrigue',
# #                        'rating': 4.5,
# #                        'title': 'Instructor Student TA Manager'}]}
# '''

## def function to track most watched genre
## COUNT of times genre appears
## If there is no amount, return error message
# '''
# input: take in the parameter 'user_data' : a nested dictionary 
# with a VALUE 'watched' list of movie dictionaries
# each movie has the KEY "genre"
# >> this VALUE represents user's list of watched movies
# >> each watched movie contains a genre
# >>>> the VALUES of  KEY "genre" is a string
# create a COUNTER to count which "genre" occurs most often
# If the value of "watched" is empty, return None

# output: The string of the genre that is most frequently watched,
# if value of watched is an empty list could try ... else none

# '''

# def get_watched_avg_rating(user_data):
#     watched_movies = user_data["watched"] ## array of dictionaries
#     total_rating = []
#     counter = 0 
#     pp.pprint(watched_movies)

#     for movie_data in watched_movies:
#         v = movie_data["rating"]
#         total_rating.append(v)
#     if len(total_rating) == 0:
#         return None
#     average = sum(total_rating) / len(total_rating)
#     return average

#             if rating is not None:
#                 v = movie_data["rating"]
#                 total_rating.append(v)
#                 average = sum(total_rating) / len(total_rating)
#             else:
#                 return 0.0
        # return average

# def get_watched_avg_rating(user_data):
#     watched_movies = user_data["watched"] ## array of dictionaries
#     total_rating = []
#     counter = 0 
# ## for a dictionary in the list of movies
#     for movie_data in watched_movies:
#         v = movie_data["rating"]
#         total_rating.append(v)
#     if len(total_rating) == 0:
#         return 0.0
#     average = sum(total_rating) / len(total_rating)
#     return average

# get_watched_avg_rating(clean_wave_2_data())

##~~~!!!!RUNS!!!!~~~##

# def get_most_watched(user_data):
#     watched_movies = user_data["watched"]
#     counter = []
#     for movie_data in watched_movies:
#         g = movie_data["genre"]
#         if g:
#             counter += 1
#         elif:
#             counter == 0
#             return None

# def get_most_watched_genre(user_data):
#     watched_movies = user_data["watched"]
#     counter = 0
#     for movie_data in watched_movies:
#         g = movie_data["genre"]
#         while g is True:
#             counter += 1
#             ## return most popular here
#         else:
#             return None


# def get_most_watched_genre(user_data):
#     watched_movies = user_data["watched"]
#     # counter = 0
#     popular_genre = ""
#     for movie_data in watched_movies:
#         g = movie_data["genre"]
#         # if g is True: 
#         #     # counter += 1
#         #     popular_genre.append(g) 
#         #     num = popular_genre.count(g) 
#         #     return num
#         # else:
#             # return None
#         g = False
#         print(g)
#     return popular_genre(g)
## removed counter, iterating through amount in list

# def get_most_watched_genre(user_data):
#     watched_movies = user_data["watched"]
#     popular_genre = []
#     for movie_data in watched_movies: 

        # print(movie_data, "//////")
        # print(movie_data["genre"], "*******")
#         for genre in movie_data["genre"]:
#             print(genre)
#             popular_genre.append(genre)
#         #     popular_genre += movie_data["genre"]
#         #     popular_genre.append(genre)
#             print(popular_genre)
#         else: watched_movies == 0
#         return None


# def get_most_watched_genre(user_data):
#     watched_movies = user_data["watched"]
#     popular_genre = []
#     count = 0
#     if watched_movies is False:
#         return None
#     for movie_data in watched_movies: ## key, value ?
#         popular_genre.append(movie_data["genre"])
#     for movie_data in watched_movies: ## key, value ?
#         if count < popular_genre.count(movie_data["genre"]):
#             count = popular_genre.count(movie_data["genre"])
#     # print(popular_genre[0])
#     # print(count)
#     return popular_genre[0]
#     ## return value for count 
##~~~!!!!RUNS!!!!~~~##
# get_most_watched_genre(clean_wave_2_data())



################################################
################################################
#     user_movie_title = set()

# '''
# input: user_data (dictionary with key "watched" with value of a
# list of dictionaries and "friends" key, with a list value)
# > watched list of movies and list of friends
# > "friends" key: has a list value, each element in the list
# is a dictionary
# >> this dictionary contains a key of watched and a list of
# movie dictionaries
# >>>> each movie dictionary has a list of movie dictionaries
# >>>> with "title" key

# consider the movies that the user has watched
# consider the moves that the friends have watched
# determine which moives at least one friend has watched, but user
# HAS NOT watched
# -> return a list of dictionaries that reresent a list of movies

# output: a list of dictionaries that display the movies friends
# have watched that user has not watched
# '''
# def get_friends_unique_watched(user_data):
#     watched_movies = user_data["watched"]
#     friends_list = user_data["friends"]
#     friends_watched = user_data["friends"]["watched"]
#     only_friends_watched = []
# ## consider sets and set functionality here
# ## if friends_watched NOT in watched_movies,
# ## then append "title" to only_friends_watched list
#     pass

# def get_unique_watched(user_data):
#     watched_movies = user_data["watched"]
#     friends_list = user_data["friends"]
# #     friends_watched = user_data["friends"][]["watched"]
#     user_watched = []
#     dictionary_friend_movies = []
#     unique_user_movies = [] #[{}]

#     for movie_watched in friends_list:
#         for movie in movie_watched["watched"]:
#         #     for title in movie["title"]:
#             dictionary_friend_movies.append(movie)
#     for movie in watched_movies:
#         user_watched.append(movie)
#         if movie not in dictionary_friend_movies:
#             unique_user_movies.append(movie)
#     ## if title is in watched_movies AND NOT in friends_watched
#     ## 
#     return unique_user_movies

## Compare user data to to generate unique movies watched
## Return results if there are no unique movies on the list
'''
take in user_data
> the value of user_data will be a dictionary with a "watched" key of value movie dict
> there is also "friends" key which has a value of friends names
>> each value in "friends" is a list of dictionaries
>> each item in "friends" has a key "watched" with a value of movie dictionaries
>> each movie dictionary has a "title" key

- consider user watched moves, consider which movies their friend has watched
- which movies the user has watched but friends have not
## if user_data["watched"] and friends_data["title"] unique

output a list of dictionaries, list of movies 
'''
# ## Get user unique data
# def get_unique_watched(user_data):
#     watched_movies = user_data["watched"]
#     friends_list = user_data["friends"]
#     friends_watched = user_data["friends"]["watched"]
#     only_user_watched = []
#     ## if title is in watched_movies AND NOT in friends_watched
#     ## return list of dictionary of only_user_watched
#     pass

#     print("friends:")
#     pp.pprint(dictionary_friend_movies)
#     print("!!!!!!!!!!!!!!!USER!!!!!!!!!!!!!!!!")
#     pp.pprint(only_user_watched)
#     pp.pprint(unique_user_movies)

# def get_friends_unique_watched(user_data):
#     watched_movies = user_data["watched"]
#     friends_list = user_data["friends"]
#     user_watched = []
#     dictionary_friend_movies = []
#     unique_friend_movies = [] 

#     for movie_watched in friends_list:
#         for movie in movie_watched["watched"]:
#             dictionary_friend_movies.append(movie)
#         if movie not in dictionary_friend_movies:
#             unique_friend_movies.append(movie)
#     for movie in watched_movies:
#         user_watched.append(movie)
#     return unique_friend_movies


# def get_friends_unique_watched(user_data):
#     watched_movies = user_data["watched"]
#     friends_list = user_data["friends"]
#     dictionary_friend_movies = []
#     unique_friend_movies = [] 
#     unique_unique = []

#     for movie_watched in friends_list:
#         for movie in movie_watched["watched"]:
#             dictionary_friend_movies.append(movie)
#             if movie not in unique_friend_movies:
#                 unique_friend_movies.append(movie)
#             if movie in unique_friend_movies and movie not in watched_movies:
#                 unique_unique.append(movie)
#     return unique_unique



# ## movie in unique_friend_movies and
# def get_friends_unique_watched(user_data):
#     watched_movies = user_data["watched"]
#     friends_list = user_data["friends"]
#     dictionary_friend_movies = []
#     unique_friend_movies = [] 
#     unique_unique = []

#     for movie_watched in friends_list: # {} in [{}]
#         # pp.pprint(movie_watched)
#         for movie in movie_watched["watched"]: 
#         #     dictionary_friend_movies.append(movie)
#         #     pp.pprint(movie)
#             if movie not in unique_friend_movies:
#                 unique_friend_movies.append(movie)
#                 if movie in unique_friend_movies and movie not in watched_movies:
#                     unique_unique.append(movie)
#             pp.pprint(unique_unique)
#             print(len(unique_unique))
# #     return unique_unique

#         # pp.pprint(unique_unique)
#         # print(len(unique_unique))
#         # print("!!!!!!dictionary_friend_movies!!!!!!!!")
#         # pp.pprint(dictionary_friend_movies)


# get_friends_unique_watched(clean_wave_3_data())
####end graveyard####

# print("\n-----Wave 03 user_data-----")
pp.pprint(clean_wave_3_data())



################################################
################################################

############ graveyard ############
'''
input: takes in user_data, nested dictionary
> field "subscriptions" is a list of strings
> represents the names of streaming services that
user has access to
> each friend in "friends" has a watched list
>each movie in watched list has a "host" 
>> "host" key holds a string that says the streaming service it is
hosted on
> determine list of reccommended movies and add to list
IF AND ONLY IF (try ... except?)
>>>> user has NOT watched  (not on "watched" list)
>>>> at least ONE friend has it on their "watched" list
** think, this is a unique movie from friends list
>>>> the "host" of that "title" is in a service that the user has
in their "subscriptions"
output: list of recommended movies

'''
# def get_available_recs(user_data):
#     movie_rec = []
#     unique_movie_function = get_friends_unique_watched()
    
# # create empty rec movie list
# # call upon unique movie function, name it
# # call friends unique movie function, name it
# # if NOT in user unique movies and in friend unique movie,
# # check if "title" "host" ==  user_data "subscriptions" 
# #  if true, append "title" to empty rec movie list

#     pass


#     unique_movies = unique_movie_friends + unique_movie_user


        # if movies["host"] not in
        #     if host not in unique_movie_user:

                #     movie_rec.remove(movies)

        # if movies["host"] not in watched_movies:
        #     movie_rec.rm(movies)

# try:
#         for movie in unique_movie_user:
#             if movie in unique_movie_friends and movie not in unique_movie_user:
#                 movie_rec.append(movie)
#     except:


#     for movie in unique_movie_user: 
#         for host in unique_movie_friends.items():
#             if host in movie:
#                 movie_rec.append(movie)
   

#     print("**************FRIENDS**************")
#     pp.pprint(unique_movie_friends) ## friend unique movie list
#     print("////////////USER/////////////////")
#     pp.pprint(unique_movie_user)

# create empty rec movie list *CHECK*
# call upon unique movie function, name it *CHECK*
# call friends unique movie function, name it *CHECK*
# if NOT in user unique movies and in friend unique movie,
# check if "title" "host" ==  user_data "subscriptions" 
#  if true, append "title" to empty rec movie list


# def get_available_recs(user_data):
#     movie_rec = []
#     watched_movies = user_data["watched"]
#     unique_movie_user = get_unique_watched(user_data)
#     unique_movie_friends = get_friends_unique_watched(user_data)
#     user_subscriptions = user_data["subscriptions"]

#     for movie in unique_movie_friends:
#         pp.pprint(movie)
#         if movie["host"] in user_subscriptions and movie not in watched_movies:
#             movie_rec.append(movie)
        
#     pp.pprint(movie_rec)
#     print(len(movie_rec))


# get_available_recs(clean_wave_4_data())


########## end graveyard ##########



# Wave 04 user data
# print("\n-----Wave 04 user_data-----")
# pp.pprint(clean_wave_4_data())



################################################
'''
input: takes in user_data, nested dictionary
> field "subscriptions" is a list of strings
> represents the names of streaming services that
user has access to
> each friend in "friends" has a watched list
>each movie in watched list has a "host" 
>> "host" key holds a string that says the streaming service it is
hosted on
> determine list of reccommended movies and add to list
IF AND ONLY IF (try ... except?)
>>>> user has NOT watched  (not on "watched" list)
>>>> at least ONE friend has it on their "watched" list
** think, this is a unique movie from friends list
>>>> the "host" of that "title" is in a service that the user has
in their "subscriptions"
output: list of recommended movies #list of dictionaries# for user

'''
################################################
################################################
############   gaveyard    ############
############ end graveyard ############


# Wave 05 user data
# print("\n-----Wave 05 user_data-----")
# pp.pprint(clean_wave_5_data())

'''
input: user_data
>>>> USE most popular genre info (hint: this function)
>>>> create a list of movies under these conditions:
>> if the user has not watched it
>> at least ONE friend HAS watched movie
the "genre" of the movie is the MOST POPULAR GENRE
'''

# def get_new_rec_by_genre(user_data):
#     popular_genre = get_most_watched_genre(user_data)
#     unique_movie_friends = get_friends_unique_watched(user_data)
#     rec_by_genre = []

#     for movie in unique_movie_friends:
#         if movie["genre"] == popular_genre:
#             rec_by_genre.append(movie)
#     return rec_by_genre

    ## empty list *CHECK*
    ## if user_data["watched"] and 
    ## if user_data["friends"]["watched"]
    ## AND popular_genre == true
    ## append ["title"] to empty list

        ## empty list *CHECK*
    ## if user_data["watched"] and 
    ## if user_data["friends"]["watched"]
    ## AND popular_genre == true
    ## append ["title"] to empty list
    
    
# def get_rec_from_favorites(user_data):
#     user_favorites = user_data["favorites"]
#     friends_list = user_data["friends"]
#     friend_watched = []
#     rec_by_fave = []

#     for movie in friends_list:
#         for watched_movie in friends_list["watched"]:
#             friend_watched.append(watched_movie)

#     for movie in user_favorites:
#         if movie in user_favorites and movie not in friend_watched:
#             rec_by_fave.append(movie)
#     return rec_by_fave