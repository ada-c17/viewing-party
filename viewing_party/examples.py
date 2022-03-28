# FANTASY_1 = {
#     "title": "The Lord of the Functions: The Fellowship of the Function",
#     "genre": "Fantasy",
#     "rating": 4.8
# }
# FANTASY_2 = {
#     "title": "The Lord of the Functions: The Two Parameters",
#     "genre": "Fantasy",
#     "rating": 4.0
# }
# FANTASY_3 = {
#     "title": "The Lord of the Functions: The Return of the Value",
#     "genre": "Fantasy",
#     "rating": 4.0
# }
# FANTASY_4 = {
#     "title": "The Programmer: An Unexpected Stack Trace",
#     "genre": "Fantasy",
#     "rating": 4.0
# }
# ACTION_1 = {
#     "title": "The JavaScript and the React",
#     "genre": "Action",
#     "rating": 2.2
# }
# ACTION_2 = {
#     "title": "2 JavaScript 2 React",
#     "genre": "Action",
#     "rating": 4.2
# }
# ACTION_3 = {
#     "title": "JavaScript 3: VS Code Lint",
#     "genre": "Action",
#     "rating": 3.5
# }
# INTRIGUE_1 = {
#     "title": "Recursion",
#     "genre": "Intrigue",
#     "rating": 2.0
# }
# INTRIGUE_2 = {
#     "title": "Instructor Student TA Manager",
#     "genre": "Intrigue",
#     "rating": 4.5
# }
# INTRIGUE_3 = {
#     "title": "Zero Dark Python",
#     "genre": "Intrigue",
#     "rating": 3.0
# }


# friends =  [
#         {
#             "watched": [
#                 FANTASY_1,
#                 FANTASY_3,
#                 FANTASY_4,
                
#             ]
#         },
# #         {
#             "watched": [
#                 FANTASY_1,
#                 ACTION_1,
#                 INTRIGUE_1,
#                 INTRIGUE_3,
#             ]
#         }
#     ]
# user_data = {
# "watched": [
#    FANTASY_1, 
#    FANTASY_2, 
#    FANTASY_3, 
#    ACTION_1, 
#    INTRIGUE_1, 
#    INTRIGUE_2
#    ],    
# }  

# print(user_data["watched"])
# print(friends[0])
# print(friends[0]["watched"][0])
# print(movie["title"])

# unique_list = []
# for movie in user_data["watched"]:
#    if movie not in friends[0]["watched"]:
#       unique_list.append(movie)
#    # print(movie["title"])
# print(unique_list)
# # print(friends[0]["watched"][0])
#    # print(f"The unique list is: {unique_list}")
#    # print(movie)
     
#          # print(unique_list) not in friends[1]["watched"]:
#          # unique_list.append(user_data["watched"][0])
# for movie in user_data["watched"]:
#        if movie["title"] not in friends[1]["watched"]:
#          # unique_list.append(user_data["watched"][0])
#          # print(unique_list)
#          print(friends[1]["watched"])

#        else:
#           print(False)
# print(unique_list)
         #  print(user_data["watched"][0]["title"])
      #    # print(friends[1]["watched"][1]["title"])
      # print(name)
      #  print(movie)
# # def get_most_watched_genre(user_data):
# user_data=  {
# "watched": [
# {"title": "The Prince of the Functions: The Fellowship of the Function",
# "genre": "Fantasy",
# "rating": 4.8
# },

# {"title": "The King of the Functions: The Fellowship of the Function",
# "genre": "Sci-fy",
# "rating": 5.0},

# {"title": "The Queen of the Functions: The Fellowship of the Function",
# "genre": "Sci-fy",
# "rating": 5.0},
   

# ]}
# genre_count = {}
# for movie in user_data["watched"]:
#    print(f"{movie=}")
#    # print(movie["genre"])

#    if movie["genre"] not in genre_count.keys():
#       genre_count[movie["genre"]] = 1
#    elif movie["genre"] in genre_count.keys():
#       genre_count[movie["genre"]] += 1

# most_watched = max(genre_count, key=genre_count.get)
# print(genre_count)
# print("Highest value from dictionary:",most_watched)

# alpha_dict = {"g": 14, "q": 16, "h": 19}

# new_value = max(alpha_dict, key=alpha_dict.get)
# print("Highest value from dictionary:",new_value)
   
# print(user_data["watched"])
# print(user_data["watched"][0]["genre"])
# get_most_watched_genre(user_data)
   # user_data=  {
# def get_watched_avg_rating(user_data):

# user_data=  {
#    "watched": [
#    {"title": "The Prince of the Functions: The Fellowship of the Function",
#    "genre": "Fantasy",
#    "rating": 4.8
#       },

#    {"title": "The King of the Functions: The Fellowship of the Function",
#    "genre": "Fantasy",
#       "rating": 5.0},
   
#    {},

#    ]}


# user_data=  {
#    "watched": []
# }

# if user_data["watched"] == []:
#    print(0.0)
# # for  value in user_data.values():
#    if value[2] == {}:
#       print(0.0)
#    else:
#       ratings =[]
#       rate_list= value[0]
#       ratings.append(rate_list["rating"])
#       rate_list= value[1]
#       ratings.append(rate_list["rating"])
#       average_rating = sum(ratings)/ len(ratings)
#       print(ratings)
#       print(average_rating)
# for  value in user_data.values():
#    if value[2] == {}:
#       print(0.0)
#    else:
#       ratings =[]
#       rate_list= value[0]
#       ratings.append(rate_list["rating"])
#       rate_list= value[1]
#       ratings.append(rate_list["rating"])
#       average_rating = sum(ratings)/ len(ratings)
#       print(ratings)
#       print(average_rating)
   # rate_list= value[2]
   # print(rate_list)

# Solution
# def get_watched_avg_rating(user_data):
#    for  value in user_data.values():
#       if value == {}:
#          average_rating == 0.0
#          return average_rating
#       else:
#          ratings =[]
#          rate_list= value[0]
#          ratings.append(rate_list["rating"])
#          rate_list= value[1]
#          ratings.append(rate_list["rating"])
#          average_rating = sum(ratings)/ len(ratings)
#          return average_rating
      
      

    
# for key in user_data["watched"]:
#    calc_rate = []
#    calc_rate.append((user_data["watched"][i]["rating"]))
# print(calc_rate)
# print(user_data["watched"][0][str("rating")])
# get_watched_avg_rating(user_data)
   





# FANTASY_1 = {
#     "title": "The Lord of the Functions: The Fellowship of the Function",
#     "genre": "Fantasy",
#     "rating": 4.8
# }
# FANTASY_2 = {
#     "title": "The Prince of the Functions: The Fellowship of the Function",
#     "genre": "Fantasy",
#     "rating": 4.8
# }



# user_data = {
#         "watchlist": [
#             FANTASY_1,
#             HORROR_1
#         ],
#         "watched": [FANTASY_2]
#     }
# def watch_movie(user_data, HORROR_1):


#    if HORROR_1 ["title"]in user_data["watchlist"] [1]["title"]:
#       user_data["watched"].append (user_data["watchlist"][1])
#       del user_data["watchlist"] [1]
#       # print(user_data["watched"])
# watch_movie(user_data, HORROR_1)
#       # user_data["watched"]= watched_movie
#       # del user_data["watchlist"]["movie_to_watch"]
#       # return user_data
# print(user_data)
# user_data = {
#          "watchlist": [{
#              "title": "MOVIE_TITLE_1",
#              "genre": "GENRE_1",
#              "rating": "RATING_1"
#          }],
# }
# print(user_data["watchlist"])
# print(user_data["watchlist"][0]["title"])





# user_data = {
#          "watchlist": [{
#             "title": "MOVIE_TITLE_1",
#              "genre": "GENRE_1",
#              "rating": "RATING_1"
#          }],
#          "watched": []
#      }
   

# def watch_movie(user_data, title):
#    title= "MOVIE_TITLE_2"
#    watched_movie = []
#    if title != user_data["watchlist"][0]["title"]:
#       return user_data
      
#    elif title == user_data["watchlist"][0]["title"]:
#       watched_movie.append(user_data["watchlist"][0])
#       user_data["watched"]= watched_movie
#       del user_data["watchlist"][0]

# print(user_data["watchlist"][0]["title"])
# print(user_data["watchlist"])
# print(user_data["watched"])
   

# watch_movie(user_data, "title")
#    #  user_data = {
# # user_data = {
# #       "watched": [] 
# #    }

# movie = {
#       "title": "MOVIE_TITLE_1",
#       "genre": "GENRE_1",
#       "rating": "RATING_1"
#    }


# def add_to_watched(user_data, movie):
#    new_list = [ ]
#    new_list.append(movie)
#    user_data["watched"]= new_list
#    # return user_data
#    print(user_data)
# add_to_watched(user_data, movie)





# keys = ["title", "genre", "rating"]

# def create_movie(title, genre, rating):
#     MOVIE_TITLE_1 = "It Came from the Stack Trace"
#     GENRE_1 = "Horror"
#     RATING_1 = 3.5
#     values = [MOVIE_TITLE_1, GENRE_1, RATING_1]
#     movie_dict = {}
    
#     if len(keys) == len(values):
#       for index in range(len(keys)):
#          movie_dict [keys[index]] = values[index]
#       print(movie_dict)
#       return movie_dict    
    
    
#     else:
#        return None

# create_movie("title","genre", "rating")

# #  for key in movie_list:
# #         if key:
# #             movie_dict[key] = " "


# #         else:
# #             return None

#     print(movie_dict)