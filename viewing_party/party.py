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

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0
    else:
        avg_list = []
        for i in range(len(user_data["watched"])):
            avg_list.append(user_data["watched"][i]["rating"])
        return sum(avg_list) / len(avg_list)


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    else:
        most_watched_dict = {}
        for i in range(len(user_data["watched"])):
            genre = user_data["watched"][i]["genre"]
            if genre in most_watched_dict:
                most_watched_dict[genre] += 1
            else:
                most_watched_dict[genre] = 1
        return max(most_watched_dict, key=most_watched_dict.get)





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
#     "watched": [{
#         "title": "aa",
#         "genre": "bb",
#         "rating": "cc"
#     }, 
#     {
#         "title": "dd",
#         "genre": "ee",
#         "rating": "ff"
#     },
#     {
#         "title": "aa",
#         "genre": "bb",
#         "rating": "cc"
#     }, 
#     {
#         "title": "dd",
#         "genre": "bb",
#         "rating": "ff"
#     }]
# }

# test_most_watched_genre(janes_data)








# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

