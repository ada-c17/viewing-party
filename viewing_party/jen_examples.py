user_data = {
    "watchlist": [
        {
        "title": "Star Wars",
        "genre": "Fiction",
        "rating": 4
        },
        {
        "title": "TDD",
        "genre": "Adventurous",
        "rating": 3
        }
        ],
    "watched": [
        {
        "title": "Free Guy",
        "genre": "Fiction",
        "rating": 4
        }
    ]
}

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
# prob: take a movie "Starwars" out of watchlist, 
# move it to watched:
# print(user_data["watchlist"])
# print(user_data("watched"))

# movie_to_move = user_data["watchlist"][0] 
# user_data["watched"].append(movie_to_move)
# user_data["watchlist"].remove(movie_to_move)

# print(user_data["watchlist"])
# print(user_data("watched"))

def get_unique_watched(user_data):
    # movies watched by user, and by friends
    movies_user_watched = []
    movies_friends_watched = []

    # loop thru movie dictionaries to get the movie, then loop thru to get movie_title,
    # add movie_title to the lists
    for movie in user_data["watched"]:
        for movie_title in movie:
            movies_user_watched.append(movie_title)

    for movie in user_data["friends"]["watched"]:
        for movie_title in movie:
            movies_friends_watched.append(movie_title)
        print(movie)

    # use set to compare the lists, taking the difference between the user's set from the friends set.
    user_set = (movies_user_watched)
    friends_set = (movies_friends_watched)
    # new_set = set_a - set_b
    unique_user_set = user_set - friends_set

    return list(unique_user_set)

get_unique_watched(user_data)