# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None

    return {"title": title, "genre": genre, "rating": rating}

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
            break
    return user_data
        
# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0.0

    mysum = 0.0
    for movie in user_data["watched"]:
        mysum += movie["rating"]
    
    return mysum / len(user_data["watched"])

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None

    counts = {}
    for movie in user_data["watched"]:
        if movie["genre"] in counts:
            counts[movie["genre"]] += 1
        else:
            counts[movie["genre"]] = 1

    most_watched_genre = ""
    most_watched_genre_count = 0
    for genre in counts:
        if counts[genre] > most_watched_genre_count:
            most_watched_genre_count = counts[genre]
            most_watched_genre = genre

    return most_watched_genre

# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    friends_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie["title"])

    unique_movies = []

    for movie in user_data["watched"]:
        if not movie["title"] in friends_movies:
            unique_movies.append(movie)
    
    return unique_movies

def get_friends_unique_watched(user_data):
    friends_movies = []

    for movie in user_data["watched"]:
        friends_movies.append(movie["title"])

    unique_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if not movie["title"] in friends_movies and not movie in unique_movies:
                unique_movies.append(movie)
    
    return unique_movies

# ------------- WAVE 4 --------------------
def get_available_recs(user_data):
    recommended_movies = []

    friends_movies = get_friends_unique_watched(user_data)

    for movie in friends_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies

# ------------- WAVE 5 --------------------
def get_new_rec_by_genre(user_data):
    recommended_movies = []

    most_frequent_genre = get_most_watched_genre(user_data)

    movies = get_friends_unique_watched(user_data)

    for movie in movies:
        if movie["genre"] == most_frequent_genre:
            recommended_movies.append(movie)

    return recommended_movies

def get_rec_from_favorites(user_data):
    recommended_movies = []

    for movie in user_data["favorites"]:
        good_for_recommendation = True

        for friend in user_data["friends"]:
            if movie in friend["watched"]:
                good_for_recommendation = False
                break

        if good_for_recommendation:
            recommended_movies.append(movie)

    return recommended_movies