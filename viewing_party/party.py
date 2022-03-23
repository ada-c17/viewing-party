# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    if not title or not genre or not rating:
        return None
    else:
        new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
        
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)          # updated_data = user_data.update({"watched": movie})
    return user_data

def add_to_watchlist(user_data, movie):
     user_data["watchlist"].append(movie)
     return user_data 

def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:    
        if movie_title in movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings_data = []
    watched_movies = user_data["watched"] #An array of dictionaries 
    average = 0.0
    for movie in watched_movies:    #For each dictionary/movie in this array 
            ratings_data.append(movie["rating"])
            # print(f"*********This is the: {ratings_data=}")
        
            ratings_total = sum(ratings_data)
            average = ratings_total / len(ratings_data)

    return average

def get_most_watched_genre(user_data):
    #I'm guessing this may be a frequency map
    popular_genre_dict = {}
    watched_movies = user_data["watched"] #An array of dictionaries representing each watched film  
    if len(watched_movies) == 0:
        return None

    for movies in watched_movies:
        # print(f"*********This is the value of: {movies=}")     
        # print(f"*********This is the value of: {genre=}")
        # for genre, frequency in popular_genre.items():
        genre = movies["genre"]
        if genre in popular_genre_dict:
            frequency = popular_genre_dict[genre] + 1 
            print(f"*********This is the value of: {frequency=}")
        else:
            frequency = 1
            # popular_genre = {str(genre): frequency}
        popular_genre_dict.update({genre: frequency})
        print(f"*********This is the value of: {popular_genre_dict=}")
    popular_genre = None
    highest_frequency = 0
    for genre, frequency in popular_genre_dict.items():
        if frequency > highest_frequency:
            highest_frequency = frequency
            popular_genre = genre
        # highest_frequency = max(popular_genre_dict.values)
        # popular_genre = max(popular_genre_dict, genre = popular_genre_dict.get) 
        
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_friends_watched_movies(user_data):
    friends = user_data["friends"]  #Each element in the friends list is a dictionary 
    friends_watched_list = []
    for friend in friends:
        # print(f" THIS IS FRIEND HERE: {friend=}")
        for movie in friend["watched"]:
            # print(f" THIS IS FRIEND HERE: {friend=}")
            friends_watched_list.append(movie)
        
    return friends_watched_list

def get_unique_watched(user_data):
    unique_watched_list = []
    watched_movies = user_data["watched"] #An array of dictionaries representing each watched film  
    friends_watched_list = get_friends_watched_movies(user_data)
    for movie in watched_movies:
        if movie not in friends_watched_list:
            unique_watched_list.append(movie)
    #Movie title variable? For each movie in movie ditionary in watched movies
    
    return unique_watched_list

def get_friends_unique_watched(user_data):
    friends_unique_watched_list = []
    watched_movies = user_data["watched"] #An array of dictionaries representing each watched film  
    friends_watched_list = get_friends_watched_movies(user_data)
    for movie in friends_watched_list:
        if movie in friends_unique_watched_list:
            continue 
        elif movie not in watched_movies:
            friends_unique_watched_list.append(movie)
            
    #Movie title variable? For each movie in movie ditionary in watched movies
    print(f"HERE IS THE LIST*************** {friends_unique_watched_list}")       
    return friends_unique_watched_list





# user_data = {
#     "watchlist": [{
#         "title": MOVIE_TITLE_1,
#         "genre": GENRE_1,
#         "rating": RATING_1
#     }],
#     "watched":  [{
#         "title": MOVIE_TITLE_1,
#         "genre": GENRE_1,
#         "rating": RATING_1
#     }]
# }
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# def create_movie(title, genre, rating):
#     movies = {}
#     if title and genre and rating: 
#         movies["title"] = title
#         movies["genre"] = genre
#         movies["rating"] = rating
#         return movies
#     else:
#         return None




    # for title in user_data["watchlist"][0].values():    #Figure out how to make it dynamic. 
    
    
    # for movie in range(len(user_data["watchlist"])): 
    #     # print(f"HERE: {title}")
    #     if title in user_data["watchlist"][movie].values():            
    #         user_data = add_to_watched(user_data, user_data["watchlist"][title])
    #         user_data["watchlist"].pop(title)
            
    #     else:
    #         len(["watchlist"]) == 0
            
    # return user_data 
    
# example_dict[ key_to_find_inner_list ][ index_to_find_element ]