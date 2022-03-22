# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    if not title or not genre or not rating:
        return None
    else:
        new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
        
    return new_movie

def add_to_watched(user_data, movie):
    
    user_data["watched"].append(movie)          # updated_data = user_data.update({"watched": movie})
    return user_data

def add_to_watchlist(user_data, movie):
     user_data["watchlist"].append(movie)
     return user_data 

def watch_movie(user_data, title):
    # for title in user_data["watchlist"][0].values():    #Figure out how to make it dynamic. 
    for movie in range(len(user_data["watchlist"])): 
        # print(f"HERE: {title}")
        if title in user_data["watchlist"][movie].values():            
            user_data = add_to_watched(user_data, user_data["watchlist"][title])
            user_data["watchlist"].pop(title)
            
        else:
            len(["watchlist"]) == 0
            
    return user_data 
    
# example_dict[ key_to_find_inner_list ][ index_to_find_element ]

    janes_data = {
        "watchlist": [{
            "title": MOVIE_TITLE_1,
            "genre": GENRE_1,
            "rating": RATING_1
        }],
        "watched": []
    }
# new_movie = create_movie(movie_title, genre, rating)

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

# def create_movie(title, genre, rating):
#     movies = {}
#     if title and genre and rating: 
#         movies["title"] = title
#         movies["genre"] = genre
#         movies["rating"] = rating
#         return movies
#     else:
#         return None