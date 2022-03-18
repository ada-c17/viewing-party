# ------------- WAVE 1 --------------------
#adding a comment in the code to commit :)
def create_movie(title, genre, rating):
    
    user_data = {
        "watched": [],
        "watchlist": []
        }

    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    if None in new_movie.values():
        return None

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist_length = len(user_data['watchlist']) #1
    movie_index = None

    for i in range(watchlist_length):
        if user_data['watchlist'][i]['title'] == title:
            movie_index = i   
            user_data['watched'].append(user_data['watchlist'][movie_index])
            del user_data['watchlist'][movie_index]
    
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    sum_rating = 0
    watched_length = len(user_data['watched'])

    if watched_length < 1:
        return avg_rating

    for movie in user_data['watched']:
        sum_rating += movie["rating"]

    avg_rating = sum_rating/watched_length
    
    return avg_rating

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

