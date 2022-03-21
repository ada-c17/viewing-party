def create_movie(title,genre,rating):
    if not bool(title) or not bool(genre) or not bool(rating):
        return None
    return {"title":title,"genre":genre,"rating":rating}

def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data

def get_watched_avg_rating(user_data):
    ratings_sum = 0 
    n = len(user_data["watched"])
    if n == 0:
        return 0
    for movie in user_data["watched"]:
        ratings_sum+=movie["rating"]
    return ratings_sum/n
        
def get_most_watched_genre(user_data):
    genre_counts = {}
    if len(user_data["watched"]) == 0:
        return None
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_counts:
            genre_counts[movie["genre"]]+=1
        else:
            genre_counts[movie["genre"]] = 1
    
    key = max(genre_counts,key=lambda k: genre_counts[k])
    return key

def get_unique_watched(user_data):
    friends_list = user_data["friends"]
    watched_list = user_data["watched"]
    friends_watched = []
    no_overlap = []
    for friend in friends_list:
        for movie in friend["watched"]:
            if movie not in friends_watched and movie in watched_list:
                friends_watched.append(movie)
    for watched_movie in watched_list:
        if watched_movie not in friends_watched:
            no_overlap.append(watched_movie)
    return no_overlap

def get_friends_unique_watched(user_data):
    friends_list = user_data["friends"]
    watched_list = user_data["watched"]
    friends_watched_unique = []
    for friend in friends_list:
        for movie in friend["watched"]:
            if movie not in friends_watched_unique and movie not in watched_list:
                friends_watched_unique.append(movie)
    return friends_watched_unique

def get_available_recs(user_data):
    recommended = []
    friends_list = user_data["friends"]
    watched_list = [movie["title"] for movie in user_data["watched"]]
    for friend in friends_list:
        for movie in friend["watched"]:
            if movie not in recommended and movie["title"] not in watched_list and movie["host"] in user_data["subscriptions"]:
                recommended.append(movie)
    return recommended