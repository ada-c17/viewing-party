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