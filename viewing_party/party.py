# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    
    movie = {}
    movie['title'] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, movie_title):
    watched_movie = {}
    #find movie_title in user_data["watchlist"]
    for movie in user_data["watchlist"]:
        # movie is a dict
        if movie['title'] == movie_title:
            # add movieto user_data["watched"]
            user_data["watched"].append(movie)
            # remove movie_title in user_data["watchlist"]
            user_data["watchlist"].remove(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"]
    count = len(watched_movies)
    total_ratings = 0

    if count == 0:
        return 0

    for wacthed_movie in watched_movies:
        total_ratings += float(wacthed_movie["rating"])
    avg = total_ratings / count
    
    return avg

def get_most_watched_genre(user_data):
    watched_movies = user_data["watched"]
    genres = {}

    if len(watched_movies) == 0:
        return None

    for watched_movie in watched_movies:
        genre = watched_movie["genre"]
        if genre not in genres:
            genres[genre] = 1
        else:
            genres[genre] += 1

    most_watched_times = 1
    most_watched_genre = ""

    for genre, watched_times in genres.items():
        if watched_times > most_watched_times:
            most_watched_times = watched_times
            most_watched_genre = genre
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

