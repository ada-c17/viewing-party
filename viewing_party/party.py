# ------------- WAVE 1 --------------------
import pdb

def create_movie(title, genre, rating):
    new_movie = {"title": title,
                "genre": genre,
                "rating": rating
                }
    if title is None or genre is None or rating is None:
        return None
    return new_movie



def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data
    

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
       
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating_list=[]
    if user_data["watched"] == []:
        return 0
    else:
        for movie in user_data["watched"]:
            rating_list.append(movie["rating"])
    return sum(rating_list)/len(rating_list)

def get_most_watched_genre(user_data):
    genre_count={}
    if user_data["watched"] == []:
        return None
    else:
        for movie in user_data["watched"]:
            if movie["genre"] not in genre_count.keys():
                genre_count[movie["genre"]]=1
            else:
                genre_count[movie["genre"]]+=1
    inverse = [(value, key) for key, value in genre_count.items()]
    return max(inverse)[1]
    # took this line from https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary /
    # and dont understand that much what it does.        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_watched = []
    all_watched = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            all_watched.add(movie["title"])
    for movie in user_data["watched"]:
        if movie["title"] not in all_watched:
            unique_watched.append(movie)

    return unique_watched 
        
def get_friends_unique_watched(user_data):
    watched_friends = []
    unique_watched_friends =[]

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            watched_friends.append(movie)
    for movie in watched_friends:
        if movie not in user_data["watched"] and movie not in unique_watched_friends:
            unique_watched_friends.append(movie)
            
    return unique_watched_friends


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    rec_movies=[]
    try:
        for friend in user_data["friends"]:
            for movie in friend["watched"]:
             if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                    rec_movies.append(movie)
        return rec_movies
    except KeyError as error:
        return []

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    rec_movies = get_available_recs(user_data)
    genre = get_most_watched_genre(user_data)
    rec_movies_genre = []
    # if user_data["watched"]==[]:
    #     return []
    # else:
    try:
        for movie in rec_movies:
            if movie["genre"] == genre:
                rec_movies_genre.append(movie)
        return rec_movies_genre
    except KeyError as error:
        return []

