# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if not (title and genre and rating):
        return None
    
    movie = {
                "title": title,
                "genre": genre,
                "rating": rating
            
            }
    return movie

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    
    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    
    return user_data

def watch_movie(user_data, title): 

    #loop through each movie in the watchlist
    for movie in user_data["watchlist"]:

        #if it matches the title passed as the arg add it to watch
        if title == movie["title"]:

            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
        
    return user_data
            



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    subtotal = 0

    watched_movies = user_data["watched"]
    
    if watched_movies: 

        for movie in watched_movies:
            subtotal += movie["rating"]
        
        avg_rating = subtotal/float(len(user_data["watched"]))
        
    else: 
        avg_rating = 0

    return avg_rating

def get_most_watched_genre(user_data):

    watched_movies = user_data["watched"]

    if not watched_movies:

        return None

    watched_genres = {}

    #calculate frequency
    for movie in watched_movies:

        if movie["genre"] in watched_genres:

            watched_genres[movie["genre"]] += 1
        
        else: 
            watched_genres[movie["genre"]] = 1

    
    #find which genre is most watched
    
    list_of_frequencies = list(watched_genres.values())

    list_of_frequencies.sort()

    most_watched_value = list_of_frequencies[-1]

    for genre in watched_genres:

        if watched_genres[genre] == most_watched_value:

            most_watched_genre = genre



    return most_watched_genre


   


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friends_watched_movies(user_data):

    your_watched_movies = user_data["watched"]

    friends = user_data["friends"]

    friends_watched_movies = []

    for friend in friends:

        for movie in friend["watched"]:

            if movie not in friends_watched_movies:

                friends_watched_movies.append(movie)
    
    return friends_watched_movies


def get_unique_watched(user_data):

    your_watched_movies = user_data["watched"]

    friends_watched_movies = get_friends_watched_movies(user_data)

    unique_watched = []
   
    for movie in your_watched_movies:
    
       if movie not in friends_watched_movies:

           unique_watched.append(movie)


    return unique_watched

def get_friends_unique_watched(user_data):

    your_watched_movies = user_data["watched"]

    friends_watched_movies = get_friends_watched_movies(user_data)

    friends_unique_watched = []

    for movie in friends_watched_movies:
    
       if movie not in your_watched_movies:

           friends_unique_watched.append(movie)


    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):

    recommended_movies = []

    friends_unique_watched = get_friends_unique_watched(user_data)

    for movie in friends_unique_watched: 

        if movie["host"] in user_data["subscriptions"]:

            recommended_movies.append(movie)
    
    return recommended_movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    new_rec_by_genre = []

    most_watched_genre = get_most_watched_genre(user_data)

    friends_unique_watched = get_friends_unique_watched(user_data)

    for movie in friends_unique_watched:

        if movie["genre"] == most_watched_genre:

            new_rec_by_genre.append(movie)
    
    return new_rec_by_genre

def get_rec_from_favorites(user_data):

    favorites = user_data["favorites"]
    recommendations = []

    friends_watched_movies = get_friends_watched_movies(user_data)

    for movie in favorites:

        if movie not in friends_watched_movies:

            recommendations.append(movie)
    
    return recommendations
