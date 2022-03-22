# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating: 
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if title in user_data["watchlist"][i].values():
            user_data = add_to_watched(user_data, user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0
    if user_data["watched"]:
        for i in range(len(user_data["watched"])):
            sum += user_data["watched"][i]["rating"]
        return sum/(len(user_data["watched"]))
    else:
        return sum

def get_most_watched_genre(user_data):
    genres = []
    if user_data["watched"]:
        for i in range(len(user_data["watched"])):
            genres.append(user_data["watched"][i]["genre"])
        return max(set(genres), key = genres.count)
    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies = []
    # for movie in user_data["watched"]:
    #     if movie not in user_data["friends"][0]["watched"] and movie not in user_data["friends"][1]["watched"]:
    #         unique_movies.append(movie)
    friend_count = len(user_data["friends"])
    for i in range (friend_count):
        if i == friend_count - 1:
            break
        for movie in user_data["watched"]:
            if movie not in user_data["friends"][i]["watched"] and movie not in user_data["friends"][i+1]["watched"]:
                unique_movies.append(movie)

    return unique_movies


def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    friend_count = len(user_data["friends"])
    for i in range (friend_count):
        for movie in user_data["friends"][i]["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)
    return friends_unique_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    reccomendations = []
    friend_count = len(user_data["friends"])
    for i in range (friend_count):
        for movie in user_data["friends"][i]["watched"]:
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"] and movie not in reccomendations:
                reccomendations.append(movie)
    return reccomendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    reccomendations = []
    genre = get_most_watched_genre(user_data)
    friend_count = len(user_data["friends"])
    for i in range (friend_count):
        for movie in user_data["friends"][i]["watched"]:
            if movie not in user_data["watched"] and movie["genre"] == genre and movie not in reccomendations:
                reccomendations.append(movie)
    return reccomendations

def get_rec_from_favorites(user_data):
    reccomendations = []
    unique_movies = get_unique_watched(user_data)
    friend_count = len(user_data["friends"])
    for i in range (friend_count):
        for movie in user_data["favorites"]:
            if movie in unique_movies and movie not in reccomendations:
                reccomendations.append(movie)
    return reccomendations
    
