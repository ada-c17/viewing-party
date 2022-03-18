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
    # user_data = {}
    # movie_list = []
    # for movie_watched in movie:
    #     movie_list.append(movie)
    # user_data["watched"] = movie
    user_data = { 
        "watched": []
    }
    user_data["watched"].append(movie)
    return user_data


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

