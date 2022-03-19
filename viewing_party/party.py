from collections import Counter
import copy
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

#-----WAVE 3--------
USER_DATA_3 = copy.deepcopy(USER_DATA_2)
USER_DATA_3["friends"] =  [
        {
            "watched": [
                FANTASY_1,
                FANTASY_3,
                FANTASY_4,
                HORROR_1,
            ]
        },
        {
            "watched": [
                FANTASY_1,
                ACTION_1,
                INTRIGUE_1,
                INTRIGUE_3,
            ]
        }
    ]  

#-----WAVE 4--------

HORROR_1b = copy.deepcopy(HORROR_1)
FANTASY_1b = copy.deepcopy(FANTASY_1)
FANTASY_2b = copy.deepcopy(FANTASY_2)
FANTASY_3b = copy.deepcopy(FANTASY_3)
FANTASY_4b = copy.deepcopy(FANTASY_4)
ACTION_1b = copy.deepcopy(ACTION_1)
ACTION_2b = copy.deepcopy(ACTION_2)
ACTION_3b = copy.deepcopy(ACTION_3)
INTRIGUE_1b = copy.deepcopy(INTRIGUE_1)
INTRIGUE_2b = copy.deepcopy(INTRIGUE_2)
INTRIGUE_3b = copy.deepcopy(INTRIGUE_3)

HORROR_1b["host"] = "netflix"
FANTASY_1b["host"] = "netflix"
FANTASY_2b["host"] = "netflix"
FANTASY_3b["host"] = "amazon"
FANTASY_4b["host"] = "hulu"
ACTION_1b["host"] = "amazon"
ACTION_2b["host"] = "amazon"
ACTION_3b["host"] = "hulu"
INTRIGUE_1b["host"] = "hulu"
INTRIGUE_2b["host"] = "disney+"
INTRIGUE_3b["host"] = "disney+"

USER_DATA_4 = {
    "watched": [
        FANTASY_1b, 
        FANTASY_2b, 
        FANTASY_3b, 
        ACTION_1b, 
        INTRIGUE_1b, 
        INTRIGUE_2b
        ],  
    "friends":  [
        {
            "watched": [
                FANTASY_1b,
                FANTASY_3b,
                FANTASY_4b,
                HORROR_1b,
            ]
        },
        {
            "watched": [
                FANTASY_1b,
                ACTION_1b,
                INTRIGUE_1b,
                INTRIGUE_3b,
            ]
        }  
    ]
}

USER_DATA_4["subscriptions"] = ["netflix", "hulu"]  


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

def watch_movie(user_data, title):
    # Move movie from user's watchlist to watched
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

####### test data #######
# janes_data = {
#         "watchlist": [{
#             "title": MOVIE_TITLE_1,
#             "genre": GENRE_1,
#             "rating": RATING_1
#         }],
#         "watched": []
#     }
# janes_data = {
#     "watchlist": [
#         FANTASY_1,
#         movie_to_watch
#     ],
#     "watched": [FANTASY_2]
# }

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

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

def get_most_watched_genre(user_data):
    if user_data["watched"] == []:
        most_watched_genre = None
    
    else:
        genre_list = []

        for movie in user_data["watched"]:
            genre_list.append(movie["genre"])
        
        frequency = Counter(genre_list)
        most_watched_genre = frequency.most_common(1)[0][0]

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_unique_watched = []
    for movie in user_data["watched"]:
        movie_unique = True
        for friend in range(len(user_data["friends"])):
            if movie in user_data["friends"][friend]["watched"]:
                movie_unique = False
        if movie_unique == True:
            user_unique_watched.append(movie)

    return user_unique_watched

def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    for friend in range(len(user_data["friends"])):
        for movie in user_data["friends"][friend]["watched"]:
            if movie not in friends_unique_watched:
                movie_unique = True
                if movie in user_data["watched"]:
                    movie_unique = False
                if movie_unique == True:
                    friends_unique_watched.append(movie)

    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    recommendations = []
    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommendations.append(movie)
    
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)

    # available_recommendations = get_available_recs(user_data) <--using this 
    # instead of the following 4 lines requires the user_data to have a list
    # of subscriptions
    friends_unique_watched = get_friends_unique_watched(user_data)
    available_recommendations = []
    for movie in friends_unique_watched:
        available_recommendations.append(movie)
    
    recs_by_genre = []
    for movie in available_recommendations:
        if movie["genre"] == most_watched_genre:
            recs_by_genre.append(movie)
    return recs_by_genre

def get_rec_from_favorites(user_data):
    user_unique_watched = get_unique_watched(user_data)
    recommended = []
    for movie in user_unique_watched:
        if movie in user_data["favorites"]:
            recommended.append(movie)

    return recommended