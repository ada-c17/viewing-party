# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if title is None or genre is None or rating is None:
        return None
    movie_dict["title"] = title
    movie_dict["genre"] =  genre 
    movie_dict["rating"] =  rating
    return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"] =  [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] =  [movie]
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        print(f"i:{i}")
        print(f"value:{user_data['watchlist'][i]['title']}")
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
            return user_data
    return user_data


# janes_data = {
#     "watchlist": [{
#         "title": "a",
#         "genre": "b",
#         "rating": "c"
#     }, 
#     {
#         "title": "d",
#         "genre": "e",
#         "rating": "f"
#     }],
#     "watched": ["p"]
# }
# print(watch_movie(janes_data, "d"))





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

