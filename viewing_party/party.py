# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if title and genre and rating:
        movie_dict["title"] = title   
        movie_dict["genre"] = genre        
        movie_dict["rating"] = rating
    else: 
        return None    
    return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for item in user_data["watchlist"]:
        if item["title"] == title:
            user_data["watched"].append(item)
            user_data["watchlist"].remove(item)
    return user_data
        # else:
        #    return user_data    

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    average_rating = 0.0
    rating_sum = 0.0
    
    if len(user_data["watched"]) > 0:
        for movie in range(len(user_data["watched"])):
            rating_sum += user_data["watched"][movie]["rating"]  
        average_rating = rating_sum / len(user_data["watched"])
    return average_rating 

def get_most_watched_genre(user_data):
    genre_dict = {}
    if len(user_data["watched"]) == 0:
        return None
    else:
        for movie in range(len(user_data["watched"])):
            if user_data["watched"][movie]["genre"] in genre_dict:
                genre_dict[user_data["watched"][movie]["genre"]] += 1
            else:
                genre_dict[user_data["watched"][movie]["genre"]] = 0
    most_watched = max(genre_dict, key=genre_dict.get)            
    return most_watched                  
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

