# ------------- WAVE 1 --------------------
movie_list = {}

def create_movie(title, genre, rating):
    movie = {'title': title,'genre': genre, 'rating': rating}
    
    for category in movie.values():
        if category == None:
            return None

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    for movie in user_data['watchlist']:
        if movie["title"] == movie_title:
            user_data['watched'].append(movie)
            user_data['watchlist'].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    average = 0
    for movie in user_data["watched"]:
        rating = movie["rating"]
        average += rating
    if len(user_data["watched"])>0:
        average /= len(user_data["watched"])

    return average

def get_most_watched_genre(user_data):
    genre_list = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if movie["genre"] in genre_list:
            genre_list[genre] += 1
        else:
            genre_list[genre] = 1
    max = 0
    for genre, count in genre_list.items():
        if count > max:
            max = count
            most_watched = genre
        elif count == max:
            most_watched = list(most_watched, genre)
    
    if max == 0:
        return None
    
    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    #user_data -> [jessica][watched][title] & [friends][watched][title]
    friends_movies = []
    for friend in user_data["friends"]:
        for i in range(len(friend['watched'])):
            title = friend['watched'][i]['title']
            if title not in friends_movies:
                friends_movies.append(title)
    unique_movies = []
    for movie in user_data["watched"]:
        if movie['title'] not in friends_movies:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    friends_movies = []
    
    for friend in user_data["friends"]:
        for movie in friend['watched']:
            if movie not in friends_movies:
                friends_movies.append(movie)

    for movie in user_data["watched"]:
        if movie in friends_movies:
            friends_movies.remove(movie)

    return friends_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friend_recs = get_friends_unique_watched(user_data)
    usable_recs = []

    for movie in friend_recs:
        if movie['host'] in user_data['subscriptions']:
            usable_recs.append(movie)
    
    return usable_recs
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):  
    favorite_genres = []
    genre_recs = []
    if len(user_data['watched']) == 0:
        return genre_recs
    recs = get_available_recs(user_data)  

    if len(recs) > 0:
        for fav in user_data['favorites']:
            if fav['genre'] not in favorite_genres:
                favorite_genres.append(fav['genre'])

        for rec in recs:
            if rec['genre'] in favorite_genres:
                genre_recs.append(rec)
    
    return genre_recs

def get_rec_from_favorites(user_data):
    unique_watched = get_unique_watched(user_data)
    recs = []

    for movie in unique_watched:
        if movie in user_data['favorites']:
            recs.append(movie)

    return recs