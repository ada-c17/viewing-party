"""
Dear Ashley (or Instructor),

Can you please take a look at the comments in my wave 3.
I tried doing something that didn't work out and so had to 
abandon it all together. I can't figure out what the problem
is and would appreciate a look.

Also, answering my questions on Wednesday!
And WOOT WOOT for finishing something I thought would even 
be able to do halfway!!!!!

Thank you so much,
Huma Hameed
(she/her)
"""



# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

    for key, value in new_movie.items():
        print(new_movie)
        if value == None:
            return None
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = []
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # for movies["title"] in user_data["watched"] == title:
    for movies in user_data["watchlist"]:
        if movies["title"] == title:
            print(title)
            user_data["watched"].append(movies)
            user_data["watchlist"].remove(movies)
    return user_data
        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0
    length = len(user_data["watched"])
    if length==0:
        return 0
    for movie in user_data["watched"]:
        sum += movie["rating"]
    avg = sum/ length
    return avg            

def get_most_watched_genre(user_data):
    genre_count = {}
    # if user_data["watched"]==[]:
    # length = len(user_data["watched"])
    # if length==0:
    #     return None
    if not user_data["watched"]:
        return None 
    for movie in user_data["watched"]:
        genre = movie["genre"] 
        if genre not in genre_count:
            genre_count[genre] = 1
        else:
            genre_count[genre] += 1
    sorted_genre = sorted(genre_count.items(), key = lambda kv:kv[1])
    return sorted_genre[-1][0]


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def friends_list(user_data):
    friends_movie_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movie_list:
                friends_movie_list.append(movie)
    return friends_movie_list

def users_list(user_data):
    users_movie_list= []
    for movie in user_data["watched"]:
        if movie not in users_movie_list:
            users_movie_list.append(movie)
    return users_movie_list

def get_unique_watched(user_data):
    user_unique_list=[]
    friends_movies = friends_list(user_data)
    users_movies = users_list(user_data)
   
    for movie in users_movies:
        if movie not in friends_movies:
            user_unique_list.append(movie)
    return user_unique_list
    # print(unique_list == friends_movies - users_movies)
    # return unique_list == friends_movies - users_movies 
    # user_unique_list == list(set(friends_movies)-set(users_movies))     
    # return user_unique_list

def get_friends_unique_watched(user_data):
    friend_unique_list=[]
    friends_movies = friends_list(user_data)
    users_movies = users_list(user_data)

    for movie in friends_movies:
        if movie not in users_movies:
            friend_unique_list.append(movie)
    return friend_unique_list
#     # print(unique_list == friends_movies - users_movies)
#     # return unique_list == friends_movies - users_movies 
#     friend_unique_list == list(set(friends_movies)-set(users_movies))     
#     return friend_unique_list

    # for movie in user_data["watched"]:
    #     for friend in user_data["friends"]:
    #         for friend_movie in friend["watched"]:
    #             if movie["title"] ==
    #         # user_data["watched"] not in friends["watched"]:
    # unique_list.append(value)
     
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    rec_movies = []
    friend_unique = get_friends_unique_watched(user_data)
    for movie in friend_unique:
        if movie["host"]==[] or user_data["subscriptions"]==[]:
            return 0
        if movie["host"] in user_data["subscriptions"]:
            rec_movies.append(movie)
    return rec_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    genre_rec = []
    genre = get_most_watched_genre(user_data)
    friend_unique = get_friends_unique_watched(user_data)
    if not user_data["watched"] or not friend_unique:
        return genre_rec
    for movie in friend_unique:
        if movie["genre"] in genre:
            genre_rec.append(movie)
    return genre_rec

def get_rec_from_favorites(user_data):
    rec_movies = []
    user_unique = get_unique_watched(user_data)
    if not user_data["favorites"] or not user_unique:
        return 0
    for movie in user_unique:
        if movie in user_data["favorites"]:
            rec_movies.append(movie)
    return rec_movies