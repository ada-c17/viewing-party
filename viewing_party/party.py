# ------------- WAVE 1 --------------------

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

    print(user_data)
    print(title)
    
    
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]

    # for movie in watchlist:
    watchlist_index = len([ele for ele in watchlist if isinstance(ele, dict)])

    # print(watchlist_index)
    count = 0
    print(type(watchlist_index))
    for i in range(watchlist_index):
        print(watchlist[i])
        print(i)
        print(range(watchlist_index))
        print("Tori")
        print(watchlist[i])
        print(watchlist[i]["title"])
        if (watchlist[i]["title"]) == title:
            print("test")
            watched_movie = watchlist.pop(i)
            print(watched_movie)
            print(watchlist)

            for value in user_data:
                watched.append(watched_movie)
                print(watched)
                return user_data

        elif (watchlist[i]["title"]) != title:
            print("elst statremnt")
    
    return user_data


    
#     del user_data("watchlist")[i]

#     print(watchlist)
#     print(watched)
#     print(user_data)

# else:
#     return user_data

    # for i in range(len(watchlist, )):
    #     if user_watched_movie == True:
    #         print(watchlist)
    #         print(i)


            #     user_watched_movie = True
            # if user_watched_movie == True:




            # for i, x in enumerate(watchlist):
            #     if watchlist["title"] == title:
            #         watched_movie = watchlist.pop(i)
            #         print(watched_movie)
            #         print(watchlist)

    # user_data = {user_data[watchlist], user_data[watched]}
    #    for movie in user_data["watchlist"]:

    # for key, value in user_data.items():
    #     for watchlist in value:
    #         if title in watchlist:
    #             del title

    # for watched in value:
    #     watched.append(title) 
    #     print(user_data) 
    #     return user_data

                    # if title in watchlist["title"]:


                
    # for key, value in user_data.items():
    #     for watchlist in value:
    #         if watchlist["title"] == title:
    #             print(i for i in range(len(user_data["watchlist"])))
    #             watched_movie = watchlist.pop("title")
    #             print(watched_movie)
    #             print(watchlist)
    

    # for key, value in range(len(user_data.items())):
    #     for watchlist in value:
    #         if value["title"] == title:
    #                 watched_movie = watchlist.pop(index)
    #                 print(watched_movie)
    #                 print(watchlist)


    # for i in range(len(watchlist)):
    #     if watchlist.items() == title:
    #         print("Tori")
    #         watched_movie = watchlist.pop("title")
    #         print(watched_movie)
    #         print(watchlist)

                    
                #     for key, value in user_data.items():
                #         for watched in value:
                #             watched.append(watched_movie)
                #             return user_data
                    
                #     del user_data("watchlist")[i]

                #     print(watchlist)
                #     print(watched)
                #     print(user_data)

                # else:
                #     return user_data






# for index in range(len(my_list)): if my_list[index]['id'] == 2: del my_list[index] break print("The result is :") print(my_list)




    #if title is in watchlist
    #remove the movie from watchlist
    #add movie to watched
    #return user_data

    #if title not in watchlist
    #return user_data






#the value of user_data will be a dictionary with a key "watched", and a value which is a list of dictionaries representing the movies the user has watched
#An empty list represents that the user has no movies in their watched list
#the value of movie will be a dictionary in this format:




#If those three attributes are truthy, then return a dictionary. This dictionary should...
# Have three key-value pairs, with specific keys
# The three keys should be "title", "genre", and "rating"
# The values of these key-value pairs should be appropriate values
# If title is falsy, genre is falsy, or rating is falsy, this function should return None


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

