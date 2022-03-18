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
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# testing git