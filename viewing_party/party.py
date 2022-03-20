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

#create a get_most_watched_genre function with parameter user_data
#create variable called "watched" to access dict of movies watched
#create an empty dictionary with genre as key and total as value
#check if watched has any values, if empty return None
#if there are values, loop through each movie and access "genre"
#append genre as key to dictionary if not there and set value to 1
#if genre already in dictionary add one to the value for that genre
# return genre with highest count
# What should it return if there are no genre's with more than oen movie?
def get_most_watched_genre(user_data):
    watched = user_data["watched"]
    genre_dict = {}
    if len(watched) > 0:
        for movie in watched:
            genre = movie["genre"]
            if genre in genre_dict:
                genre_dict[genre] += 1
            else:
                genre_dict[genre] = 1
        return max(genre_dict, key = genre_dict.get)
    return None

# Create get_unique_watched function with one parameter user_data 
#create variable called "watched_user" to access list of movies watched by user
#create variable called "friends" to access list of friends watched dictionaries
#create empty list to hold unique movies
#if watched not an empty list then loop through 
#nest a loop to iterate through the list of friends
#within list of friends iterate through the movies in their watched list
#compare the titles from friends movies to titles in user movies
#if movie appears in both append to duplicate list
#iterate through user list and dupes and create list of unique movies to return

def get_unique_watched(user_data):
    watched_user = user_data["watched"]
    friends = user_data["friends"]
    dupes = []
    for friend in friends:
        watched_friend = friend["watched"]
        for movie in watched_user:
            if movie in watched_friend:
                dupes.append(movie)
    unique_user_movies = [movie for movie in watched_user if movie not in dupes]
    return unique_user_movies





# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

