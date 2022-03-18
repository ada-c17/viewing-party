# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if None in [title, genre, rating]:
        return None
    
    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating,
    }
    return movie_dict

def add_to_watched(user_data, movie):
    watched = user_data["watched"]
    watched.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = user_data["watchlist"]
    watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    index = 0
    transfer_movie = False
    # dictionary
    for key,value in user_data.items():
        if key == "watchlist":
            # list
            for movie in value:
                # dictionary
                m_key = "title"
                if movie[m_key] == title:
                    transfer_movie = value.pop(index)
                index += 1
        if key == "watched" and transfer_movie:
            user_data[key].append(transfer_movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = []
    movie_list = user_data["watched"]
    
    for dict in movie_list:
        ratings.append(dict["rating"])
    
    if not ratings:
        return 0.0
    else:
        return sum(ratings) / float(len(ratings))

def get_most_watched_genre(user_data):

    #list of movie dicts
    watched_list = user_data["watched"]
    
    if not watched_list:
        return None

    movie_count = {
            "Fantasy": 0,
            "Action": 0,
            "Horror": 0,
            "Intrigue": 0
        }

    #movie is a dictionary with key "genre"
    for movie in watched_list:
        movie_count[movie["genre"]] += 1
    
    max_count = max(movie_count.values())

    for genre in movie_count:
        if movie_count[genre] == max_count:
            return genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
