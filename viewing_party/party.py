# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if isinstance(title, str) and isinstance(genre, str) and isinstance(rating, float):
        new_movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
        return new_movie
    else: 
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

#create watch_movie function with parameters user_data and title
#create var that access watchlist and one for watched
#loop through the titles for the movie in watchlist 
#look for title value in watchlist and compare 
#if found remove from watchlist and move dictionary for movie to watched
#return user data
def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    for movie in watchlist:
        if title == movie["title"]:
            watchlist.remove(movie)
            watched.append(movie)
            return user_data
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

#create a get_watched_avg_rating() function with one parameter user_data
#create a variable called "watched" to access dictioanry of movies watched
#create an empty list to hold ratings
#check if watched has any values if so loop through them else return 0.0
#loop through each movie in watched and access "rating" for each movie
#append each rating to list
#calculate average of list outside loop
#return rating
def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    ratings_list = []
    if len(watched) > 0:
        for movie in watched:
            ratings_list.append(movie["rating"])
        return sum(ratings_list)/len(ratings_list)
    return 0.0





# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

