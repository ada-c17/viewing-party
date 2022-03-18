# ------------- WAVE 1 --------------------

from tests.test_constants import USER_DATA_5


def create_movie(title, genre, rating):
    movies = {"title" : title,
                "genre" : genre,
                "rating" : rating}
    if not title or not genre or not rating:
        movies = None
    return movies

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, MOVIE_TITLE_1):
    for movie in user_data["watchlist"]:
        if movie["title"] == MOVIE_TITLE_1:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_rating = 0
    for movie in user_data["watched"]:
        total_rating += movie["rating"]
    try:
        ave_rating = total_rating / len(user_data["watched"])
    except ZeroDivisionError:
        ave_rating = 0
    return ave_rating

def get_most_watched_genre(user_data):
    genre_dict = {}
    for movie in user_data["watched"]:
        watched_genre = movie["genre"]
        if watched_genre in genre_dict:
            genre_dict[watched_genre] += 1
        else:
            genre_dict[watched_genre] = 0
    try:
        most_watched_genre = max(genre_dict, key=genre_dict.get)
    except ValueError:
        most_watched_genre = None
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friends_watched_movie = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if not movie in friends_watched_movie:
                friends_watched_movie.append(movie)

    unique_watched_movie = []
    for movie in user_data["watched"]:
        if not movie in friends_watched_movie:
            unique_watched_movie.append(movie)
    
    return unique_watched_movie

def get_friends_unique_watched(user_data):
    friends_uniqute_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if not movie in user_data["watched"] and not movie in friends_uniqute_watched:
                friends_uniqute_watched.append(movie)

    return friends_uniqute_watched

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommendations = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    for movie in friends_unique_watched:
        try:
            if movie["host"] in user_data["subscriptions"]:
                recommendations.append(movie)
        except KeyError:
            recommendations.append(movie)
    return recommendations




# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommendations_genre = []
    most_watched_genre_of_user = get_most_watched_genre(user_data)
    possible_recs = get_available_recs(user_data) #-> [{},{}]
    for movie in possible_recs:
        if movie["genre"]== most_watched_genre_of_user and not movie["genre"] in recommendations_genre:
            recommendations_genre.append(movie)

    return recommendations_genre

def get_rec_from_favorites(user_data):
    recommendations_fav = []
    user_favorites = user_data["favorites"]
    user_unique_watched = get_unique_watched(user_data)
    for movie in user_favorites:
        if movie in user_unique_watched:
            recommendations_fav.append(movie)
        
    return recommendations_fav
        

