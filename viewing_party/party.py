# ------------- WAVE 1 --------------------

# import pdb
from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    result = None
    if not title or not genre or not rating:
        return None
    movie = {}
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating
    return movie

    
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

    new_movie_list = []

    friends_movie_titles = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_movie_titles.append(movie)
        
    for movie in user_data['watched']:
        if movie not in friends_movie_titles:
            new_movie_list.append(movie)
    return new_movie_list


        

def friends_movies(user_data):
    friends_movie_titles = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_movie_titles.append(movie)
    return friends_movie_titles
    
def get_friends_unique_watched(user_data):
    list_of_movies = []
    for movie in friends_movies(user_data):
        if movie not in user_data['watched'] and movie not in list_of_movies:
            list_of_movies.append(movie)
        
    return list_of_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommendations = []
    for movie in get_friends_unique_watched(user_data):
        if movie['host'] in user_data['subscriptions']:
            recommendations.append(movie)
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre_recommendations = []
    popular_genre = get_most_watched_genre(user_data)
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie['genre'] == popular_genre and movie not in user_data['watched']:
                genre_recommendations.append(movie)
    return genre_recommendations



def get_rec_from_favorites(user_data):
    favorites_recommendation = []
    new_movie = get_unique_watched(user_data) 
    for movie in user_data['watched']:
        if movie in user_data['favorites'] and movie in new_movie:
            favorites_recommendation.append(movie)
    return favorites_recommendation


