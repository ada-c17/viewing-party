# ------------- WAVE 1 --------------------
 # create_movie returns a dictionary with "title", "genre"
 # and "rating" as keys
def create_movie(title, genre, rating):
    movie_table = {}

    if title and genre and rating:
        movie_table["title"] = title
        movie_table["genre"] = genre
        movie_table["rating"] = rating
        return movie_table


def add_to_watched(user_data,movie):
        if not all((user_data,movie)):
            return None   
        user_data["watched"].append(movie) 
        return user_data
    # return updated_datas

def add_to_watchlist(user_data,movie):
        if not all((user_data,movie)):
            return None
        user_data["watchlist"].append(movie)
        return user_data

def watch_movie(user_data, title):
    # print (user_data)
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0

    rating_list = [movie["rating"] for movie in user_data["watched"]]

    return sum(rating_list)/len(rating_list)

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    genre_list = [movie["genre"] for movie in user_data["watched"]]
    return max(set(genre_list ), key = genre_list .count)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique = []
    watched = user_data["watched"]
    friends_watched = user_data["friends"]
    all_movies = []
    # print (len(list(friends_watched)))
    
    for friends in range(len(list(friends_watched))):
        for movie in range(len(list(friends_watched[friends]["watched"]))):
            all_movies.append(friends_watched[friends]["watched"][movie]["title"])
        

    for movie in range(len(watched)):
        if watched[movie]["title"] not in all_movies:

            unique.append(watched[movie])
            
    return unique

def get_friends_unique_watched(user_data):
    
    watched = user_data["watched"]
    friends_watched = user_data["friends"]
    all_movies = []
    for movies in range(len(list(watched))):
        all_movies.append(watched[movies]["title"])
    friends_movies = []
    for movie in range(len(friends_watched)):
    
        friends_movies.append(friends_watched[movie]["watched"])
    print(f"all_movies_friends are equal to {friends_movies}")
    result = []
    for movies in range(len(friends_movies)):
        for name in range(len(friends_movies[movie])):
            if friends_movies[movies][name]["title"] not in all_movies:
                result.append(friends_movies[movies][name])
          

    return result

        

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    watched = user_data["watched"]
    friends_watched = user_data["friends"]
    
    watched_user = []
    for movie in range(len(list(watched))):
        watched_user.append(watched[movie]["title"])
    

    results = []
    for i in range(len(list(friends_watched[0]["watched"]))):
        if friends_watched[0]["watched"][i]["title"] not in watched_user and friends_watched[0]["watched"][i]["host"] in user_data["subscriptions"]:
            results.append(friends_watched[0]["watched"][i])
        
    print(results)
    return results
    
    

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

from collections import Counter
def   get_new_rec_by_genre(user_data):
    if not user_data["watched"] and user_data["friends"]:
        return []
    watched = user_data["watched"]
    friends_watched = user_data["friends"]
    genre = []
    watched_user = []
    for movie in range(len(list(watched))):
        watched_user.append(watched[movie]["title"])
        genre.append(watched[movie]["genre"])
    favorite = Counter(genre)
    fave_max = max(favorite, key=favorite.get)
    results = []

    for i in range(len(list(friends_watched[0]["watched"]))):
        if friends_watched[0]["watched"][i]["title"] not in watched_user and friends_watched[0]["watched"][i]["genre"] == fave_max:
                results.append(friends_watched[0]["watched"][i])
   

    return results

def get_rec_from_favorites(user_data):
    if not user_data["favorites"] and user_data["friends"]:
        return []
    favorites = user_data["favorites"]
    
    all = []
    # print(favorites)
    friends_watched = user_data["friends"]
    
    for a in range(len(friends_watched)):
        for b in range(len(friends_watched[a]["watched"])):
            all.append(friends_watched[a]["watched"][b]["title"])
    
    mutual = []
    for movie in range(len(favorites)):
        if favorites[movie]["title"] in all :
            mutual.append(favorites[movie])
    

    c = [x for x in favorites if x not in mutual]
    
    return c


