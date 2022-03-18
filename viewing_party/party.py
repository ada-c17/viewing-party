# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == movie:
            movie_dict = user_data["watchlist"].pop(i)
            user_data["watched"].append(movie_dict)
    return user_data

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    ratings = [] # Initialize list that will store all ratings 
    watched_list = user_data["watched"] # Extract the watched list from the rest of the user data
    
    for movie in watched_list: # Iterate through the watched list
        ratings.append(movie["rating"]) # Add each movies rating to ratings list

    ratings_sum = 0.0
    for rating in ratings:
        ratings_sum += rating
    avg_rating = ratings_sum / len(ratings)
    return avg_rating



# HORROR_1 = {
#     "title": "Us",
#     "genre": "Horror",
#     "rating": 5.0
# }
# FANTASY_1 = {
#     "title": "The Lord of the Functions: The Fellowship of the Function",
#     "genre": "Fantasy",
#     "rating": 4.8
# }
# FANTASY_2 = {
#     "title": "The Lord of the Functions: The Two Parameters",
#     "genre": "Fantasy",
#     "rating": 4.0
# }
# FANTASY_3 = {
#     "title": "The Lord of the Functions: The Return of the Value",
#     "genre": "Fantasy",
#     "rating": 4.0
# }
# FANTASY_4 = {
#     "title": "The Programmer: An Unexpected Stack Trace",
#     "genre": "Fantasy",
#     "rating": 4.0
# }
# ACTION_1 = {
#     "title": "The JavaScript and the React",
#     "genre": "Action",
#     "rating": 2.2
# }
# ACTION_2 = {
#     "title": "2 JavaScript 2 React",
#     "genre": "Action",
#     "rating": 4.2
# }
# ACTION_3 = {
#     "title": "JavaScript 3: VS Code Lint",
#     "genre": "Action",
#     "rating": 3.5
# }
# INTRIGUE_1 = {
#     "title": "Recursion",
#     "genre": "Intrigue",
#     "rating": 2.0
# }
# INTRIGUE_2 = {
#     "title": "Instructor Student TA Manager",
#     "genre": "Intrigue",
#     "rating": 4.5
# }
# INTRIGUE_3 = {
#     "title": "Zero Dark Python",
#     "genre": "Intrigue",
#     "rating": 3.0
# }

# USER_DATA_2 = {
#     "watched": [
#         FANTASY_1, 
#         FANTASY_2, 
#         FANTASY_3, 
#         ACTION_1, 
#         INTRIGUE_1, 
#         INTRIGUE_2
#         ],    
# }

# get_watched_avg_rating(USER_DATA_2)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

