# ------------- WAVE 1 --------------------

#DONE
import re

def create_movie(movie_title, genre, rating):
    dict = {}
    
    if movie_title is None:
        return None
    elif genre is None:
        return None
    elif rating is None:
        return None
    else:
        dict["title"] = movie_title
        dict["genre"] = genre
        dict["rating"] = rating
        return dict
    pass

#DONE
def add_to_watched(user_data, movie):
    #hmm I have no idea why I created and empty dictionary and appended user_data["watched"] to it, seeems unnecessary
    emptyDict = {}
    user_data["watched"].append(emptyDict)
    user_data["watched"][0]["title"] = movie["title"]
    user_data["watched"][0]["genre"] = movie["genre"]
    user_data["watched"][0]["rating"] = movie["rating"]
    return user_data
    pass

#DONE
def add_to_watchlist(user_data, movie):
    emptyDict = {}
    user_data["watchlist"].append(emptyDict)
    user_data["watchlist"][0]["title"] = movie["title"]
    user_data["watchlist"][0]["genre"] = movie["genre"]
    user_data["watchlist"][0]["rating"] = movie["rating"]
    return user_data
    pass

#DONE
def watch_movie(janes_data, movie_title):
    for i in range(len(janes_data["watchlist"])):
        if janes_data["watchlist"][i]["title"] == movie_title:
            removed = janes_data["watchlist"].pop(i)
            janes_data["watched"].append(removed)
    return janes_data
    pass


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

#DONE
def get_watched_avg_rating(janes_data):
    sum = 0
    if len(janes_data["watched"]) == 0:
        return 0
    for movie in janes_data["watched"]:
        sum += movie["rating"]
    return sum/(len(janes_data["watched"]))
    pass

#DONE
def get_most_watched_genre(data):
    genreDict = {}
    for movie in data["watched"]:
        genre = movie["genre"]
        if genre not in genreDict:
            genreDict[genre] = 1
        elif genre in genreDict:
            genreDict[genre] += 1 
    maxValue = 0
    for value in genreDict.values():
        if value > maxValue:
            maxValue = value
    for key,value in genreDict.items():
        if value == maxValue:
            return key   
    pass

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
import copy 

#DONE
def get_unique_watched(data):
    #amandaUniqueMovieList = []

    #can't do it this way because it changes the original list
    #anotherList = data["watched"]

    #list of movies amanda has seen
    #print(data["watched"])

    #this is a list of the first friend's watched movies
    #print(data["friends"][0]["watched"])
    
    #this is a list of the second friend's watched movies
    #print(data["friends"][1]["watched"])
    
    #newList = []

    origCopy = data["watched"]
    listCopy = copy.deepcopy(origCopy)
    for j in range(len(data["friends"])):
        for i in range(len(data["friends"][j]["watched"])):
            if data["friends"][j]["watched"][i] in listCopy:
                listCopy.remove(data["friends"][j]["watched"][i])
    return listCopy
            #this prints all the movies in the friends watch list from every dictionary in the list
            #print(data["friends"][j]["watched"][i]["title"])

            #this prints all the dictionaries of movies all friends have watched 
            #print(data["friends"][j]["watched"][i])

            #this is giving me the wrong list, it's a list of movies everyone has seen 
            #if data["friends"][j]["watched"][i] in data["watched"]:
                #newList.append(data["friends"][j]["watched"][i])
    #print(newList)
            
            #can't do it this way because it changes the original list
            #if data["friends"][j]["watched"][i] in anotherList:
                #anotherList.remove(data["friends"][j]["watched"][i])
    #print(anotherList)


    #this was wrong
    #for movie in data["watched"]:
        #if movie["title"] not in data["friends"]:
            #amandaUniqueMovieList.append(movie)
    #print(amandaUniqueMovieList)

    pass

#DONE!
def get_friends_unique_watched(data):
    newList = []
    for j in range(len(data["friends"])):
        for i in range(len(data["friends"][j]["watched"])):
            if data["friends"][j]["watched"][i] not in data["watched"]:
                if data["friends"][j]["watched"][i] not in newList:
                    newList.append(data["friends"][j]["watched"][i])
    return newList
    pass

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

#DONE!
def get_available_recs(data):
    recList = []
    for j in range(len(data["friends"])):
        for i in range(len(data["friends"][j]["watched"])):
            if data["friends"][j]["watched"][i] not in data["watched"] and data["friends"][j]["watched"][i]["host"] in data["subscriptions"]:
                recList.append(data["friends"][j]["watched"][i])
    return recList
    pass

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(data):
    genreRecList = []
    mostWatchedGenre = get_most_watched_genre(data)
    
    for j in range(len(data["friends"])):
        for i in range(len(data["friends"][j]["watched"])):
            if data["friends"][j]["watched"][i] not in data["watched"] and data["friends"][j]["watched"][i]["genre"] == mostWatchedGenre:
                genreRecList.append(data["friends"][j]["watched"][i])
    return genreRecList
    pass


def get_rec_from_favorites(data):
    faveRecList = []
    #movies none of the user's friends have watched
    uniqueList = get_unique_watched(data)
    for movie in uniqueList:
        if movie in data["favorites"]:
            faveRecList.append(movie)
    return faveRecList
    pass
