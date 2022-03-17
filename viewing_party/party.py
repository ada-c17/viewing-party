# ------------- WAVE 1 --------------------

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
    
    most_watched_genre = max(genre_dict, key=genre_dict.get)
    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

