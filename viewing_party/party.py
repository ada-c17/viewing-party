# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return{
            "title": title, 
            "genre": genre, 
            "rating": rating,
            }
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie) #user_data w/key "watched", append to parameter "movie"
    return user_data                    #return updated user_data



def add_to_watchlist(user_data, movie):
    for movie in user_data["watchlist"]:    #for movie inside user_data w/ key "watchlist"
        
        if movie["title"] == movie:         #if movie w/ key "title" is == to movie
            user_data["watchlist"].remove(movie)    #then user_data w/ key in watchlist, REMOVE movie (already)
            user_data = add_to_watched(user_data, movie) #the user_data is set to equal add_to_watched(user_data,movie)
    
    return user_data        #return updated user_data




def watch_movie(user_data, title):
    for movie in user_data["watchlist", "watched"]:     #for movie in user_data w/ key "watchlist" & "watched":
        if movie["title"] == title:                     #if movie key "title" is title
            user_data["watchlist"].remove(movie)            #user_data w key of "watchlist", if title has been watch, then remove "movie"
            user_data = add_to_watched(user_data, movie)    #user_data is set to equal add_to_watched function?????

        return user_data                                #return updated user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_rating = 0.0
    
    if len(user_data["watched"]) == 0:
        return 0.0
    
    for movie in user_data["watched"]:
        total_rating += movie["rating"]
    
    return total_rating / len(user_data["watched"])

def get_most_watched_genre(user_data):
    genre_count = {}
    
    if len(user_data["watched"]) == 0:
        return None
    
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] =+ 1
        else:
            genre_count[genre] = 1
    
    return max(genre_count) #google

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    final_list = user_data["watched"].copy()

    for friend in user_data["friends"]: #removed movie that friends watch from movie list
        for movie in friend["watched"]:
            if movie in final_list:
                final_list.remove(movie)
        
    return final_list 

def get_friends_unique_watched(user_data): #flip flop 
    final_list = []
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in final_list:
                final_list.remove(movie)
            final_list.append(movie)
    
    for movie in user_data["watched"]: #removed movie that friends watch from movie list
        if movie in final_list:
            final_list.remove(movie)
    
    return final_list 
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    movies_friends_watched_list = get_friends_unique_watched(user_data) #wave 3
    final_list = list()

    for movie in movies_friends_watched_list:
        if movie["host"] in user_data["subscriptions"]:
            final_list.append(movie)
            
    return final_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    
    friends_recs = get_friends_unique_watched(user_data) #wave 3
    favorite_genre = get_most_watched_genre(user_data) #wave 2
    genre_recs = []

    for friend in friends_recs:
        if friend["genre"] == favorite_genre:
            genre_recs.append(friend)
    return genre_recs


def get_rec_from_favorites(user_data): 
    
    user_recs = get_unique_watched(user_data)   #wave 3
    recs_movies = []

    for user_rec in user_recs:
        for movie in user_data ["favorites"]:
            if movie["title"] == user_rec["title"]:
                recs_movies.append(movie)
    
    return recs_movies
