# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else:
        return None
    
def add_to_watched(user_data, movie):
    for value in user_data.values():
        value.append(movie)
        return user_data
    
def add_to_watchlist(user_data, movie):
    for value in user_data.values():
        value.append(movie)
        return user_data
    
def watch_movie(user_data, title):
    #3dict = {"watch":[{},{},{}], "watched"[{},{},{}]} 
    for key in user_data:
        if title in user_data["watchlist"]:
            user_data["watchlist"].remove(title)
            user_data["watched"].append(title)
    
    return user_data
janes_data = {
            "watchlist": [{
                "title": "It Came from the Stack Trace",
                "genre": "drama",
                "rating": 3
            }],
            "watched": [{'genre': 'Fantasy', 'rating': 4.8, 'title': 'The Lord of the Functions: The Fellowship of the Function'}, {'genre': 'Horror', 'rating': 3.5, 'title': 'It Came from the Stack Trace'}]
        }
dict = watch_movie(janes_data, "no such")        
print(dict)     
    
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

