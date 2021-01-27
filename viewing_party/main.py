def create_movie(title, genre, rating):
    if(title and genre and rating):
        return {"title":title, "genre":genre, "rating":rating}
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    remove = False
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            remove = movie
            user_data["watched"].append(movie)
    if remove:
        user_data["watchlist"].remove(remove)
    return user_data

def get_watched_avg_rating(user_data):
    ratings = 0.0
    count = 0
    for movie in user_data["watched"]:
        ratings += movie["rating"]
        count += 1
    
    if count <= 1:
        return ratings
    return (ratings / count)

def get_most_watched_genre(user_data):
    genres = {}
    for movie in user_data["watched"]:
        try:
            genre = movie["genre"]
        except KeyError:
            genre = ""
        if genre in genres:
            genres[genre] += 1
        else:
            genres[genre] = 1
    
    max_count = 0
    max_genre = ""
    for key, value in genres.items():
        if(value > max_count):
            max_genre = key
            max_count = value
    if max_genre == "":
        return None
    return max_genre

def get_unique_watched(user_data):
    friends_movies = []
    unwatched = []
    friends = user_data["friends"]
    for friend in friends:
        watched = friend["watched"]
        for movie in watched:
            if movie["title"] not in friends_movies:
                friends_movies.append(movie["title"])
    for movie in user_data["watched"]:
        if movie["title"] not in friends_movies:
            unwatched.append(movie)
    return unwatched

def get_friends_unique_watched(user_data):
    unwatched = []
    friends = user_data["friends"]
    for friend in friends:
        watched = friend["watched"]
        for movie in watched:
            if movie not in unwatched and movie not in user_data["watched"]:
                unwatched.append(movie)
    return unwatched

def get_available_recs(user_data):
    recs = []
    friends = user_data["friends"]
    for friend in friends:
        watched = friend["watched"]
        for movie in watched:
            if movie not in recs and movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                recs.append(movie)
    return recs

def get_new_rec_by_genre(user_data):
    pref_genre = get_most_watched_genre(user_data)
    friends_movies = []
    recs = []
    friends = user_data["friends"]
    for friend in friends:
        watched = friend["watched"]
        for movie in watched:
            if movie not in recs and movie not in user_data["watched"] and movie["genre"] == pref_genre:
                recs.append(movie)
    return recs

def get_rec_from_favorites(user_data):
    pref_genre = get_most_watched_genre(user_data)
    friends_movies = []
    recs = []
    friends = user_data["friends"]
    for friend in friends:
        watched = friend["watched"]
        for movie in watched:
            if movie not in friends_movies:
                friends_movies.append(movie)
    for movie in user_data["favorites"]:
        try:
            test_genre = movie["genre"]
        except KeyError:
            test_genre = None
        if movie not in friends_movies and test_genre == pref_genre:
            recs.append(movie)
    return recs