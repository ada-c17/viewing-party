# ------------- WAVE 1 --------------------

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    new_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    if bool(title) == True and bool(genre) == True and bool(rating) == True:
        return new_dict
    else: 
        return None

def add_to_watched(user_data, movie):
    if len(user_data) == 1:
        user_data["watched"].append(movie)
        return user_data

def add_to_watchlist(user_data, movie):
    if len(user_data) == 1:
        user_data["watchlist"].append(movie)
        return user_data







def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data
        




# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = [movie["rating"] for movie in user_data["watched"]]
    if len(user_data["watched"]) == 0:
        return 0.0
    else:
        return sum(ratings) / len(ratings)


def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    else:
        frequently = {}
        genres = [movie["genre"] for movie in user_data["watched"]]
        for genre in genres:
            if genre in frequently:
                frequently[genre] += 1
            else:
                frequently[genre] = 1
        popular = max(frequently, key=frequently.get)
        return popular

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
 #find unique list of movie of user that their friend hasnt watch yet
    unique_user_movies = []
    friend_movies = []
    for friend in user_data["friends"]:
        friend_movies += friend["watched"]
    
    for movie in user_data["watched"]:
        if not movie in friend_movies:
            unique_user_movies.append(movie)
    
    return unique_user_movies

def get_friends_unique_watched(user_data):
  #find the unique list of movie of friends that user hasnt watch yet
    unique_friend_movies = []
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if not movie in user_data["watched"] and not movie in unique_friend_movies:
                unique_friend_movies.append(movie)
            
            
    return unique_friend_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies = []
    friends_movies = []
    for friend in user_data["friends"]:
        friends_movies += friend["watched"]

    for movie in friends_movies:
        if not movie in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommended_movies = []
    popular_genre = get_most_watched_genre(user_data)
    user_not_watched = get_friends_unique_watched(user_data)

    if popular_genre is not None:
        for movie in user_not_watched:
            if movie["genre"] in popular_genre:
                recommended_movies.append(movie)
    
    return recommended_movies




def get_rec_from_favorites(user_data):
    rec_movies = []
    unique_watched = get_unique_watched(user_data)
    for movie in unique_watched:
        if movie in user_data["favorites"]:
            rec_movies.append(movie)
    return rec_movies
        
    
    
    

