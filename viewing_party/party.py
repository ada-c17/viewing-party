# ------------- WAVE 1 --------------------

from collections import UserString
from collections import Counter


def create_movie(movie, genre, rating):
    if movie == None or genre == None or rating == None:    
        return None 
    new_movie = {'title': movie,
            'genre': genre,
            'rating': rating}

    return new_movie


def add_to_watchlist(user_data, movie): 
    user_data['watchlist'].append(movie)
    return user_data 


def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data 


def watch_movie(user_data, title):
    watch_list = user_data['watchlist']
    
    for movie_data in watch_list:       
        if movie_data['title'] == title:
            add_to_watched(user_data, movie_data)
            watch_list.remove(movie_data)

    return user_data
        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

 
def get_watched_avg_rating(user_data): 
    sum = 0
    average = 0 
    try:
        for movie in user_data['watched']: 
            sum += movie['rating']
        average = sum / len(user_data['watched'])
        return average
    except: 
        return 0.0
            
    
def get_most_watched_genre(user_data):
    genre_list = []
    try: 
        for movie in user_data['watched']:
            genre_list.append(movie['genre'])

        genre_count = Counter(genre_list)
        fave_genre = ((genre_count.most_common(1))[0][0])
        return fave_genre   
    except: 
        return None 
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def friend_watched_list(user_data):
    friend_watched = []     
    for friend in user_data['friends']: 
        for a_movie in friend['watched']:
            if a_movie in friend_watched: 
                continue 
            else: 
                friend_watched.append(a_movie)
    return friend_watched 


def get_unique_watched(user_data):
    friend_watched = friend_watched_list(user_data)
    user_unique = []
   
    for movie in user_data['watched']: 
        if movie not in friend_watched: 
            user_unique.append(movie)

    return(user_unique)


def get_friends_unique_watched(user_data): 
    friend_watched = friend_watched_list(user_data)
    friend_unique = []  
    for movie in friend_watched: 
        if movie not in user_data['watched']: 
            friend_unique.append(movie)

    return(friend_unique)

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_subscriptions = user_data['subscriptions']
    friend_watched = get_friends_unique_watched(user_data)
    movie_recommendations = []

    for movie in friend_watched: 
        if movie['host'] in user_subscriptions: 
            movie_recommendations.append(movie)

    return(movie_recommendations)



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)
    friend_watched = get_friends_unique_watched(user_data)
    movie_recommendations = []

    for movie in friend_watched: 
        if movie['genre'] == fav_genre: 
            movie_recommendations.append(movie)
    return movie_recommendations 
   

def get_rec_from_favorites(user_data): 
    user_favorites = user_data['favorites']
    user_unique = get_unique_watched(user_data)
    user_recommendations = [] 

    for movie in user_unique:
        if movie in user_favorites: 
            user_recommendations.append(movie)
    return user_recommendations 




  
