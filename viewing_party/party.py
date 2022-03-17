# ------------- WAVE 1 --------------------

user_data = {}

def create_movie(movie_title, genre, rating):
    if movie_title and genre and rating:
        new_movie = {
            "title": movie_title,
            "genre": genre,
            "rating": rating
        }
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"]= [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"]= [movie]
    return user_data

watch_list = []
def watch_movie(user_data, movie):
    # user_data["watched"] = [movie]
    already_watched_list = user_data["watchlist"]
    user_data["watched"]= watch_list.append(movie)
    already_watched_list.remove(movie)
    return user_data
    
    # AssertionError: assert ['It Came from the Stack Trace'] is [{'genre': 'Horror', 'rating': 3.5,\
    #  'title': 'It Came from the Stack Trace'}]


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

