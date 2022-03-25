# ------------- WAVE 1 --------------------

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    new_movie = {
        "title": MOVIE_TITLE_1,
        "genre": GENRE_1, 
        "rating": RATING_1
    }

    if not title or not genre or not rating:
        return None 
    else: 
        new_movie = {}
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    return new_movie 


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for key in user_data["watchlist"]:
        if key["title"] == title:
            user_data["watchlist"].remove(key)
            user_data["watched"].append(key)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    avg_rating = 0
    total_rating = 0
    if user_data["watched"]:
        for movie in user_data["watched"]:
            total_rating += movie["rating"]
        avg_rating = total_rating/len(user_data["watched"])
        return avg_rating
    else:
        return 0.0

def get_most_watched_genre(user_data):
    popular_genre = None
    count = {}
    frequent_count = 0
    for movie in user_data["watched"]: 
        if movie["genre"] not in count:
            count[movie["genre"]] = 0
        count[movie["genre"]] =+ 1
    
    for genre in count:
        if count[genre] > frequent_count:
            frequent_count = count[genre]
            popular_genre = genre
    return popular_genre 

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friends_watched = []
    final_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)    
    
    for movie in user_data["watched"]:
        if movie not in friends_watched:
            # print(movie)
            final_list.append(movie)
    return final_list

def get_friends_unique_watched(user_data):
    user_watched = []
    friends_watched = []
    total_list = []


    for movie in user_data["watched"]:
        # if movie not in user_data["watched"]:
        user_watched.append(movie)
            
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    for movie in friends_watched:
        if movie not in user_watched and movie not in total_list: 
            total_list.append(movie)
    
    return total_list



        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies = []

    for movie in get_friends_unique_watched(user_data):
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies




# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# 
def get_new_rec_by_genre(user_data):
    user_genre = []

    for movie in get_friends_unique_watched(user_data):
        if movie["genre"] == get_most_watched_genre(user_data):
            user_genre.append(movie)
    return user_genre

def get_rec_from_favorites(user_data):
    user_favorite = []
    friend_movies = []
    friends_watched = get_friends_unique_watched(user_data)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)

    for movie in user_data["favorites"]:
        if movie not in friend_movies:
            user_favorite.append(movie)
    return user_favorite

