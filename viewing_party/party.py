# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict ={}
    if title and genre and rating:
        movie_dict["title"] = title 
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict    
    else:
        return None


def add_to_watched(user_data, movie):
    watched_movies = user_data
    watched_movies["watched"].append(movie)
    return watched_movies


def add_to_watchlist(user_data, movie):
    watch_list = user_data
    watch_list["watchlist"].append(movie)
    return watch_list


def watch_movie(user_data, movie_title):
    update_watched = user_data
    for movie in user_data["watchlist"]:
        if movie_title in movie["title"]:
            update_watched["watched"].append(movie)
            update_watched["watchlist"].remove(movie)
    print(update_watched)
    return update_watched    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    
    users_data = user_data
    avg_values = 0
    counter = 0
    movies = users_data["watched"]
    if movies:
        for items in users_data.values():
            for num in items:
                avg_values += num["rating"]
                counter += 1
        result = avg_values/counter  
        return result
    else:
        return 0

# for items in users_data.values(): is'nt this the same as "movies"?
# def get_most_watched_genre(user_data):
#     users_data = user_data
#     data = user_data.values()
#     list = []   
#     movies = users_data["watched"]

#     if movies:
#         for item in data:
#             for i in item:
#                 list.append(i["genre"])
#         most_commom = max(set(list), key = list.count)
#         return most_commom  
#     else: 
#         return most_commom


def get_most_watched_genre(user_data):

    watched_genres = {}
    watched_movies = user_data["watched"]

    if not watched_movies:
        return None

    for movie in watched_movies:
        if movie["genre"] in watched_genres:
            watched_genres[movie["genre"]] += 1
        else: 
            watched_genres[movie["genre"]] = 1
    list_of_freq = list(watched_genres.values())
    list_of_freq.sort()
    most_watched_value = list_of_freq[-1]

    for genre in watched_genres:
        if watched_genres[genre] == most_watched_value:
            most_watched_genre = genre
    return most_watched_genre

def friends_watched(user_data):

    users_data = user_data
    my_movies = users_data["watched"]
    friends = users_data["friends"]
    friends_watched_movies = []
    if my_movies:
        for movies in friends:
            for movie in movies["watched"]:
                if movie not in friends_watched_movies:
                    friends_watched_movies.append(movie)
        return friends_watched_movies
    else:
        return friends_watched_movies  

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    users_data = user_data
    my_movies = users_data["watched"]
    friends_watched_movies = friends_watched(user_data)
    unique_list = []   
    

    if my_movies:
        for movie in my_movies:
            if movie not in friends_watched_movies:
                unique_list.append(movie)
        return unique_list
    else:
        return unique_list  

def get_friends_unique_watched(user_data):

    users_data = user_data
    your_watched_movies = users_data["watched"]
    friends_watched_movies = friends_watched(user_data)
    friends_unique_watched = []

    for movie in friends_watched_movies:
        if movie not in your_watched_movies:
            friends_unique_watched.append(movie)
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    users_data = user_data
    recommended_movies = []
    friends_unique_watched = get_friends_unique_watched(user_data)

    for movie in friends_unique_watched: 
        if movie["host"] in users_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies


def get_new_rec_by_genre(user_data):

    users_data = user_data
    new_rec_by_genre = []
    most_watched_genre = get_most_watched_genre(users_data)
    friends_unique_watched = get_friends_unique_watched(users_data)

    for movie in friends_unique_watched:
        if movie["genre"] == most_watched_genre:
            new_rec_by_genre.append(movie)

    return new_rec_by_genre


def get_rec_from_favorites(user_data):

    users_data = user_data
    favorites = users_data["favorites"]
    recommend = []
    friends_watched_movies = friends_watched(users_data)

    for movie in favorites:
        if movie not in friends_watched_movies:
            recommend.append(movie)
    return recommend

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    users_data = user_data
    new_rec_by_genre = []
    most_watched_genre = get_most_watched_genre(users_data)
    friends_unique_watched = get_friends_unique_watched(users_data)

    for movie in friends_unique_watched:
        if movie["genre"] == most_watched_genre:
            new_rec_by_genre.append(movie)
    return new_rec_by_genre


def get_rec_from_favorites(user_data):

    users_data = user_data
    favorites = users_data["favorites"]
    recommend = []
    friends_watched_movies = friends_watched(users_data)

    for movie in favorites:
        if movie not in friends_watched_movies:
            recommend.append(movie)
    return recommend















