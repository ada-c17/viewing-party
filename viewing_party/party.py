from collections import Counter

# ------------- WAVE 1 -----------
def create_movie(title, genre, rating):
    new_movie={}
    if title == None or genre == None or rating == None:
        return None
    new_movie["title"]=title
    new_movie["genre"]=genre
    new_movie["rating"]=rating
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    for data in user_data["watchlist"]:
        if data["title"]== movie_title:
            user_data["watchlist"].remove(data)
            user_data["watched"].append(data)
            return user_data 
    return user_data    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    count=len(user_data['watched'])
    if count ==0:
        return 0.0
    total=sum(item['rating'] for item in user_data['watched'])
    return total/count

def get_most_watched_genre(user_data):
    if len(user_data['watched']) ==0:
        return None
    frequency=Counter(d['genre'] for d in user_data['watched'])
    return frequency.most_common(1)[0][0]


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_unique_movies=list(user_data['watched'])
    for data in user_data['friends']:
        for movie in data['watched']:
            if movie in user_unique_movies:
                user_unique_movies.remove(movie)
    return user_unique_movies   

def get_friends_unique_watched(user_data):
    friends_unique_movies=[]
    for data in user_data['friends']:
        for movie in data['watched']:
            if movie not in user_data['watched'] and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)
    return friends_unique_movies 
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommendations=[]
    for data in user_data['friends']:
        for movie in data['watched']:
            if movie not in user_data['watched'] and movie['host'] in user_data['subscriptions']:
                recommendations.append(movie)
    return recommendations 


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

