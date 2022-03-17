# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating,
    }
    for value in movie_dict.values():
        if not value:
            return None
    return movie_dict

def add_to_watched(user_data, movie):
    for key,value in user_data.items():
        if key == "watched":
            value.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    for key,value in user_data.items():
        if key == "watchlist":
            value.append(movie)
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