# ------------- WAVE 1 --------------------

from time import monotonic


def create_movie(title, genre, rating):
    movie_dict = {}

    if title and genre and rating:
        movie_dict['title'] = title 
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating
    else:
        return None
    return movie_dict

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, movie):
    for i in user_data['watchlist']:
        if i['title'] == movie:
            user_data['watched'].append(i)
            user_data['watchlist'].remove(i)    
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_total = 0
    counter = 0
    for i in user_data['watched']:
        rating_total += i['rating']
        counter += 1
        
    if rating_total >0:
        avg_rating = rating_total/counter
    else:
        avg_rating = 0
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

