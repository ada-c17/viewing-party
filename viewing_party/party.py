# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    if title and genre and rating:
        new_movie = {"title": title, "genre": genre, "rating": rating}
        return new_movie
    else:
        return None



def add_to_watched(user_data, movie):

    #put movie inside value list of of movies
    user_data["watched"].append(movie)

    #return user data

    return user_data

def add_to_watchlist(user_data, movie):
    
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    
    watchlist = user_data["watchlist"] #list we iterate over
    new_watchlist = [] #new list, avoiding mutating iterated list^
    watched = user_data["watched"] #list we append to

    for i in range(len(watchlist)):
        if title in watchlist[i].values(): #titles
            #if value==title: #if movie was watched
            watched.append(watchlist[i]) #add to watched list
        else: #remain in watchlist
            new_watchlist.append(watchlist[i])

    user_data["watchlist"] = new_watchlist #update watchlist in user data

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    #initiate running total for rating score
    total = 0
    for i in range(len(user_data["watched"])):
            total += user_data["watched"][i]["rating"]
    
    try: #get avg rating score
        average = total/len(user_data["watched"])
    except ZeroDivisionError: #if empty list
        return 0

    return average

def get_most_watched_genre(user_data):

    #return None for empty watched list
    if len(user_data["watched"]) == 0:
        return None
    
    #set count for each genre
    genre_count = {"Fantasy": 0, "Action": 0, "Intrigue": 0, "Horror": 0}

    #loop over each item's genre and check which genre it matches, 
    for movie in user_data["watched"]:
        if movie["genre"] == "Fantasy":
            genre_count["Fantasy"]+=1
        elif movie["genre"] == "Action":
            genre_count["Action"]+=1
        elif movie["genre"] == "Intrigue":
            genre_count["Intrigue"] += 1
        else:
            genre_count["Horror"] += 1
    
    #return max genre count genre
    return max(genre_count, key = genre_count.get)
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    #user_data= {watched: [{}, {}, {}], friends: [watched: [{title: string}, {title: string}, {title: string}], [], []]}

    #compare movie titles for every movie in user_data["watched"] to movie titles for every movie of every friend in user_data["friends"] and append unique MOVIES to list
    
    #access friends' movie titles as list of strings
    friends_watched_titles = []

    for friends in user_data["friends"]:
        for movie in friends["watched"]:
            friends_watched_titles.append(movie["title"])

    #initialize unique movie list of dicts
    unique_movies = []   

    #compare every title between user and friends
    for user_movie in user_data["watched"]:
        if user_movie["title"] not in friends_watched_titles: #compare title names
            unique_movies.append(user_movie) #append unique movies

    #list of dictionaries
    return unique_movies


def get_friends_unique_watched(user_data):
    
    #get list of dicts of all friend watched movies
    friends_watched_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_movies.append(movie)

    #access user movie titles as list of strings
    user_watched_titles = []

    for movie in user_data["watched"]:
        user_watched_titles.append(movie["title"])
    
    #initialize unique movie list of dicts
    unique_movies = []   
    #compare every title between user and friends
    for friend_movie in friends_watched_movies:
        if friend_movie["title"] not in user_watched_titles and friend_movie not in unique_movies: #compare titles, avoid duplicates in unique movies
            unique_movies.append(friend_movie)
    
    return unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    #user_data = {"watched": [{}], "friends": [{"watched": [{"title": string, "host": string}, {}]}], "subscriptions": [string, string, string]}

    #get movies friends have watched but user has not
    friends_unique_watched_movies = get_friends_unique_watched(user_data)

    #initialize list of recs
    recommended_movies = []

    for movie in friends_unique_watched_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    
    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    
    #determine most frequently watched genre
    most_watched_genre = get_most_watched_genre(user_data)

    #get movies friends have watched but user has not
    friends_unique_watched_movies = get_friends_unique_watched(user_data)

    #initialize unqiue movie list
    recommended_movies = []

    for movie in friends_unique_watched_movies:
        if movie["genre"] == most_watched_genre:
            recommended_movies.append(movie)
    
    return recommended_movies


def get_rec_from_favorites(user_data):
    
    #access friends' movie titles as list of strings
    friends_watched_titles = []

    for friends in user_data["friends"]:
        for movie in friends["watched"]:
            friends_watched_titles.append(movie["title"])

    #initialize unique movie list of dicts
    recommended_movies = []   

    #compare every title between user and friends
    for user_movie in user_data["favorites"]:
        if user_movie["title"] not in friends_watched_titles: #compare title names
            recommended_movies.append(user_movie) #append unique movies


    return recommended_movies