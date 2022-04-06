import copy
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    #return None of title, genre, and rating are empty
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

    watchlist_copy = copy.deepcopy(user_data["watchlist"])# copy list of movies in the watch list

    #loop through each movie in the watchlist
    for movie in watchlist_copy:
        #if it matches the title passed as the arg add it to watch
        if title == movie["title"]:

            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
        
    return user_data
            

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    watched_movies = user_data["watched"]

    if watched_movies: 
        
        subtotal = 0

        for movie in watched_movies:

            subtotal += movie["rating"] #add up ratings
        
        avg_rating = subtotal/float(len(watched_movies)) #calculate avg
        
    else: #avg is 0 if no watched movies
        avg_rating = 0

    return avg_rating


def get_most_watched_genre(user_data):

    #list of dictionaries with watched movies
    watched_movies = user_data["watched"]

    if not watched_movies:

        return None

    #initialize dictionary to track genres and frequencies
    watched_genres = {}

    #calculate frequency
    for movie in watched_movies:

        if movie["genre"] in watched_genres:

            watched_genres[movie["genre"]] += 1
        
        else: 
            watched_genres[movie["genre"]] = 1

    
    #find the frequency of most watched genre
    
    list_of_frequencies = list(watched_genres.values())

    list_of_frequencies.sort()

    most_watched_value = list_of_frequencies[-1]

    #loop through the gengand find the first movie that matches that frequency
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

    #loop though each friend and all of the movies they watched and
    for friend in friends:

        for movie in friend["watched"]:
            
            if movie not in friends_watched_movies: #check for duplicates

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
    
    #find the most watched genre
    most_watched_genre = get_most_watched_genre(user_data)

    #generate movies that only your friends have seen
    friends_unique_watched = get_friends_unique_watched(user_data)

    #loop through movies that only friends have seen
    for movie in friends_unique_watched:

        #if the movies is in the most watched genre add it to the list
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
