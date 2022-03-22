# ------------- WAVE 1 --------------------

from multiprocessing.sharedctypes import Value


def create_movie(title, genre, rating):
    
    if None in [title, genre, rating]:
        return None
    
    
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
    
    return movie_dict
    


    
def add_to_watched(user_data, movie):
    """Takes in a user_data list of dictionaries containing
    watched movies. Takes in a movie and adds to this watched
    list."""
    user_data["watched"].append(movie)
    return user_data
    

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
    
def watch_movie(user_data, title):
    # Find if title is in list of watchlist movies
    for movie in user_data["watchlist"]:
        if movie.get("title") == title:
            # Found the title in list of movies
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
        
    # Never found movie in the watchlist
    return user_data
    


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    #iterate through the user data and find rating
    sum_rating = 0
    if len(user_data["watched"]) == 0:
        return sum_rating
    for movie in user_data["watched"]:
        #add ratings and divide by len(rating)
        sum_rating += movie.get("rating", 0)
    
    return sum_rating / len(user_data["watched"])


def get_most_watched_genre(user_data):
    popular_genre = {}
    for movie in user_data["watched"]:
        genre = movie.get("genre")
        if genre in popular_genre:
            popular_genre[genre] += 1
        else:
            popular_genre[genre] = 1
            
    maxi = 0
    popular = None
    for genre,count in popular_genre.items():
        if count > maxi:
            maxi = count
            popular = genre
            
    return popular
              



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    pass

def get_friends_unique_watched(user_data):
    pass
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    pass



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    pass

def get_rec_from_favorites(user_data):
    pass