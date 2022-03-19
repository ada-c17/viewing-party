
#----------WAVE01-------------
MOVIE_TITLE_1 = "It Came from the Stack Trace"
GENRE_1 = "Horror"
RATING_1 = 3.5
#----------WAVE02-------------
HORROR_1 = {
    "title": MOVIE_TITLE_1,
    "genre": GENRE_1,
    "rating": RATING_1
}
FANTASY_1 = {
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8
}
FANTASY_2 = {
    "title": "The Lord of the Functions: The Two Parameters",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_3 = {
    "title": "The Lord of the Functions: The Return of the Value",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_4 = {
    "title": "The Programmer: An Unexpected Stack Trace",
    "genre": "Fantasy",
    "rating": 4.0
}
ACTION_1 = {
    "title": "The JavaScript and the React",
    "genre": "Action",
    "rating": 2.2
}
ACTION_2 = {
    "title": "2 JavaScript 2 React",
    "genre": "Action",
    "rating": 4.2
}
ACTION_3 = {
    "title": "JavaScript 3: VS Code Lint",
    "genre": "Action",
    "rating": 3.5
}
INTRIGUE_1 = {
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0
}
INTRIGUE_2 = {
    "title": "Instructor Student TA Manager",
    "genre": "Intrigue",
    "rating": 4.5
}
INTRIGUE_3 = {
    "title": "Zero Dark Python",
    "genre": "Intrigue",
    "rating": 3.0
}
USER_DATA_2 = {
    "watched": [
        FANTASY_1, 
        FANTASY_2, 
        FANTASY_3, 
        ACTION_1, 
        INTRIGUE_1, 
        INTRIGUE_2
        ],    
}

def create_movie(title, genre, rating):
    # If title, genre, or rating are "None", return None
    if title == None or genre == None or rating == None:
        movie = None
    # Otherwise, create movie with title, genre, and rating
    else:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    
    return movie

def add_to_watched(user_data, movie):
    # Add movie to user's watched
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    # Add movie to user's watchlist
    user_data["watchlist"].append(movie)
    return user_data

# janes_data = {
#     "watchlist": [
#         FANTASY_1,
#         movie_to_watch
#     ],
#     "watched": [FANTASY_2]
# }

def watch_movie(user_data, title):
    # Move movie from user's watchlist to watched
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

#watch_movie(janes_data, movie_to_watch["title"])
# # test data
# janes_data = {
#         "watchlist": [{
#             "title": MOVIE_TITLE_1,
#             "genre": GENRE_1,
#             "rating": RATING_1
#         }],
#         "watched": []
#     }

def get_watched_avg_rating(user_data):
    sum_ratings = 0
    count_ratings = 0

    for movie in user_data["watched"]:
        sum_ratings += movie["rating"]
        count_ratings += 1

    if user_data["watched"] == []:
        avg_rating = 0
    else:
        avg_rating = sum_ratings / count_ratings

    return avg_rating

#get_watched_avg_rating(USER_DATA_2)


# movie = create_movie(MOVIE_TITLE_1, GENRE_1, RATING_1)
# updated_data = add_to_watched(janes_data, movie)
# updated_data = watch_movie(janes_data, MOVIE_TITLE_1)

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

