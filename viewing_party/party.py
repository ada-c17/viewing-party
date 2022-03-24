# ------------- WAVE 1 --------------------

from shutil import move


def create_movie(title, genre, rating):
    movie_info = [title, genre, rating]
    if None in movie_info:
        movie = None
    else:
        movie = {"title": title, "genre": genre, "rating": rating}
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,movie_title):
    for i in range(len(user_data["watchlist"])):
        for info in user_data["watchlist"][i].values():
            if info == movie_title:
                # Remove movie from watchlist
                watched_movie = user_data["watchlist"].pop(i)
                add_to_watched(user_data, watched_movie)
    
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return float(0)

    rating_sum = 0
    for i in range(len(user_data["watched"])):
        rating_sum += user_data["watched"][i]["rating"]
    
    avg_rating = rating_sum / len(user_data["watched"])
    return avg_rating

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None

    watched_genres = {}
    for movie in user_data["watched"]:
        movie_genre = movie["genre"]
        if movie_genre in watched_genres:
            watched_genres[movie_genre] += 1
        else:
            watched_genres[movie_genre] = 1

    most_watched = max(watched_genres, key = watched_genres.get)
    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_movie_titles(watched_list):
    """
    Takes in one parameter, a list of dictionaries
    """
    movie_titles = []

    for movies in watched_list:
        for info in movies.keys():
            if info == "title":
                movie_titles.append(movies["title"])

    return movie_titles

def make_list_of_friends_movies(user_data):
    friends_movies = []
    for watched_lists in user_data["friends"]:
        titles = get_movie_titles(watched_lists["watched"])
        friends_movies.append(titles)

    return friends_movies

def make_set_from_nested_list(nested_list):
    new_set = set()
    for inside_lists in nested_list:
        for items in inside_lists:
            new_set.add(items)
    return new_set

def get_unique_watched(user_data): 
    user_movies = get_movie_titles(user_data["watched"])
    friends_movies = make_list_of_friends_movies(user_data)

    friends_movies_set = make_set_from_nested_list(friends_movies)
    user_unique_watched = set(user_movies) - friends_movies_set
    
    unique_movies = []
    for movie in user_data["watched"]:
        if movie["title"] in user_unique_watched:
            unique_movies.append(movie)
    
    return unique_movies

def get_friends_unique_watched(user_data):
    user_movies = get_movie_titles(user_data["watched"])
    friends_movies = make_list_of_friends_movies(user_data)
    # Combine movies together into one set
    friends_movies_set = make_set_from_nested_list(friends_movies)

    friend_unique_watched = friends_movies_set - set(user_movies)
    
    friend_unique_movies = []
    for watched_lists in user_data["friends"]:
        for movie in watched_lists["watched"]:
            if movie["title"] in friend_unique_watched:
                if movie in friend_unique_movies:
                    continue
                friend_unique_movies.append(movie)
    
    return friend_unique_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    friend_unique_movies = get_friends_unique_watched(user_data)
    reccomended_movies = []
    for movie in friend_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            reccomended_movies.append(movie)
    
    return reccomended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def find_most_watched_genre(user_data):
    genre_frequency = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre not in genre_frequency:
            genre_frequency[genre] = 1
        elif genre in genre_frequency:
            genre_frequency[genre] += 1
    
    highest_count = 0
    most_watched_genre = None
    for genre, count in genre_frequency.items():
        if count > highest_count:
            highest_count = count
            most_watched_genre = genre
    
    return most_watched_genre

def get_new_rec_by_genre(user_data):
    available_recs = get_friends_unique_watched(user_data)
    most_popular_genre = find_most_watched_genre(user_data)
    recs_by_genre = []
    for movie in available_recs:
        if movie["genre"] == most_popular_genre:
            recs_by_genre.append(movie)
    
    return recs_by_genre

def get_rec_from_favorites(user_data):
    user_unique_movies = get_unique_watched(user_data)
    recs_by_favorites = []
    for movie in user_unique_movies:
        if movie in user_data["favorites"]:
            recs_by_favorites.append(movie)
    
    return recs_by_favorites