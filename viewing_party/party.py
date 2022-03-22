# ------------- WAVE 1 --------------------

from audioop import avg
from collections import Counter


def create_movie(title, genre, rating):

    if title and genre and rating:
    
        movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
            }
        return movie
    
    else:
        return None
    
def add_to_watched(user_data, movie):
    
    watched = []

    user_data = {"watched": watched}

    for value in user_data:
        watched.append(movie)
                
    return user_data

def add_to_watchlist(user_data, movie):

    watchlist = []

    user_data = {"watchlist": watchlist}

    for value in user_data:
        watchlist.append(movie)

    return user_data

def watch_movie(user_data, title):

    watchlist = user_data["watchlist"]
    watched = user_data["watched"]

    watchlist_index = len([ele for ele in watchlist if isinstance(ele, dict)])

    for i in range(watchlist_index):
        if (watchlist[i]["title"]) == title:
            watched_movie = watchlist.pop(i)

            for value in user_data:
                watched.append(watched_movie)
                return user_data

        elif (watchlist[i]["title"]) != title:
            print("test") # delete print statement but get check for errors before and after

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    ratings_list = []
    watched = user_data["watched"]

    for movie in watched:
        ratings_list.append(movie["rating"])
    
    if ratings_list == []:
        return 0
    else: 
        return sum(ratings_list) / len(ratings_list)

def get_most_watched_genre(user_data):

    genre_list = []
    genre_count = {}

    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])

    if genre_list == []:
        return None
    
    else:
        genre_frequency = Counter(genre_list)
        most_common_genre_frequency = genre_frequency.most_common(1)
        most_common_genre = most_common_genre_frequency[0]
        return most_common_genre[0]

        
        #return most_common_genre
        
        
        # for genre in genre_list:
        #     print(genre_list)
        #     if genre not in genre_count:
        #         genre_count[genre] = 1
        #     else:
        #         genre_count[genre] += 1
        #         print(genre_list)
        #         print(genre_count)
        #         genre_count_set = set(genre_count)
        #         print()
        #         print(genre_count_set)
        
        
        





    # number_or_ratings = len(ratings_list)
    # average_ratings = sum_of_user_ratings / number_or_ratings

    # average_ratings = float(average_ratings)
    # return average_ratings

# user_ratings = get_watched_avg_rating()
# print(user_ratings)
# average_ratings = avg(user_ratings)
# print(average_ratings)

                

    # rating = watched["rating"]
    # print(ratings)

    # number_movies_watched = len([ele for ele in watched if isinstance(ele, dict)])
    # print(number_movies_watched)

    # print(user_data["watched"].get("rating"))
    
    # list_ratings = []
    # for i in range(number_movies_watched):
    #     ratings = sum([user_data["watched"][i]["rating"] for key in user_data])
    #     list_ratings.append("ratings")
    #     print(list_ratings)

    # total_rating = []

    # for key, value in user_data.items():
    #     for watched in value:
    #         for rating in key:
    #             total_rating.append(watched["rating"])
    #             return total_rating
            

    # for key, value in user_data.items():
    #     for watched in value:
    #         print(watched["rating"])


    # for i in range(number_movies_watched):

                # for rating in key:
                # for rating in value:


#     Calculate the average rating of all movies in the watched list
# The average rating of an empty watched list is 0.0
# return the average rating


# This represents that the user has a list of watched movies. Each watched movie has a genre.
# The values of "genre" is a string.
# Determine which genre is most frequently occurring in the watched list
# return the genre that is the most frequently watched





# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

