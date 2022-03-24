# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}

    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    else:
        return None

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    watched_movie = {}

    for list, movie_data in user_data.items():
        for data in movie_data:
            if data["title"] == title:
                watched_movie = data
                user_data["watchlist"].remove(data)

    if len(watched_movie) >= 1:
        add_to_watched(user_data, watched_movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating_sum = 0
    rating_count = 0

    for list, movie_data in user_data.items():
        for data in movie_data:
            rating_sum += data["rating"]
            rating_count += 1

    if len(user_data["watched"]) >= 1:
        average_rating = rating_sum / rating_count
        return average_rating
    else:
        return 0

def get_most_watched_genre(user_data):
    genre_counter = {}

    for list, movie_data in user_data.items():
        for data in movie_data:
            genre = data["genre"]
            if genre in genre_counter:
                genre_counter[genre] += 1
            else:
                genre_counter[genre] = 1

    if len(genre_counter) == 0:
        return None
    else:
        favorite_genre = max(genre_counter, key=genre_counter.get)
        return favorite_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    movies_watched = []
    movies_friends_watched = []
    unique_watched = []

    for list, movie_data in user_data.items():
        for movie_detail in user_data["watched"]:
            movies_watched.append(movie_detail)
        for friends_watched_movies in user_data["friends"]:
            for friends_movie_details in friends_watched_movies["watched"]:
                movies_friends_watched.append(friends_movie_details)

    for movie in movies_watched:
        if movie in movies_friends_watched:
            continue
        elif movie not in movies_friends_watched and movie not in unique_watched:
            unique_watched.append(movie)

    return unique_watched

def get_friends_unique_watched(user_data):
    movies_watched = []
    movies_friends_watched = []
    friends_unique_watched = []

    for list, movie_data in user_data.items():
        for movie_detail in user_data["watched"]:
            movies_watched.append(movie_detail)
        for friends_watched_movies in user_data["friends"]:
            for friends_movie_details in friends_watched_movies["watched"]:
                movies_friends_watched.append(friends_movie_details)

    for movie in movies_friends_watched:
        if movie in movies_watched:
            continue
        elif movie not in movies_watched and movie not in friends_unique_watched:
            friends_unique_watched.append(movie)

    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
