# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    new_movie ={}
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
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data 


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        average_rating = 0.0
        return average_rating
    total = 0
    for movie in user_data["watched"]:
        total += movie["rating"]
    average_rating = total/len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None

    genres =[]
    count = 0
    for movie in user_data["watched"]:
        genres.append(movie["genre"])

    for genre in genres:
        current_frequency= genres.count(genre)
        if current_frequency > count:
            count = current_frequency
            top_genre = genre
        return top_genre

    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friends_titles = []
    user_unique_movie_list = []

    for friend in user_data['friends']:
        for movies in friend["watched"]:
            friends_titles.append(movies['title'])

    for movie in user_data["watched"]:
        if movie['title'] not in friends_titles:
            user_unique_movie_list.append(movie)
    return user_unique_movie_list 
    

def get_friends_unique_watched(user_data):
    user_titles = []
    friends_unique_movie_list = []

    for movie in user_data["watched"]:
        user_titles.append(movie["title"])

    for friend in user_data['friends']:
        for movie in friend["watched"]:
            if movie["title"] not in user_titles and \
            movie not in friends_unique_movie_list:
                    friends_unique_movie_list.append(movie)
    return friends_unique_movie_list
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)
    recommended_movies = []
    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    most_watched_genre_user = get_most_watched_genre(user_data)
    get_friends_unique_movies = get_friends_unique_watched(user_data)
    movie_recs_by_genre_for_user = []

    for movie in get_friends_unique_movies:
        if movie["genre"] == most_watched_genre_user:
            movie_recs_by_genre_for_user.append(movie)
    return movie_recs_by_genre_for_user


def get_rec_from_favorites(user_data):
    friends_movie_list = []
    rec_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie_list.append(movie["title"])

    for movie in user_data["favorites"]:
        if movie["title"] not in friends_movie_list:
            rec_movies.append(movie)
    return rec_movies





