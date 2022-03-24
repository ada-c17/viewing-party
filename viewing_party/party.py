# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # Only create/return a movie dict if all arguments are valid (truthy)
    # Assumes rating is greater than 0
    if all([title, genre, rating]):
        return {
            "title": title,
            "genre": genre,
            "rating": rating,
        }
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watched_list = user_data["watched"]
    watchlist = user_data["watchlist"]

    # Iterate through each movie in watchlist, looking for a match to the argument title
    for index, movie in enumerate(watchlist):
        if movie["title"] == title:
            # Move movie dict from one list to the other
            transfer_movie = watchlist.pop(index)
            watched_list.append(transfer_movie)
            break
    # Return argument passed in, which may have been updated by for loop
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings = []
    for movie in user_data["watched"]:
        # All values should be float, no need to cast them to float
        ratings.append(movie["rating"])
    
    if not ratings:
        return 0.0
    else:
        # Average rating
        return sum(ratings) / len(ratings)


def get_most_watched_genre(user_data):
    genre_list = []
    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])
    
    # Find the most common genre by using key with count(), will return None if the list is empty
    # Will only return one value, even if there is a tie
    max_genre = max(genre_list, default=None, key=genre_list.count)
    return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # Each index is a "friend" holding a dictionary
    friends_list = user_data["friends"]
    # Will hold friends' "watched" movie dicts on one level
    friends_watched_list = []
    for friend in friends_list:
        friends_watched_list += friend["watched"]

    # m is a movie dictionary
    unique_list = [m for m in user_data["watched"] if m not in friends_watched_list]
    return unique_list

def get_friends_unique_watched(user_data):
    unique_list = []
    # Go through each friend and then each movie they have watched
    # Compare it to what the user has watched, don't take in duplicates
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in unique_list:
                unique_list.append(movie)
    return unique_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    # Movies the user hasn't watched and at least one friend has watched
    friends_watched_list = get_friends_unique_watched(user_data)
    # m is a movie dictionary, keep ones based on user's subscriptions list
    rec_list = [m for m in friends_watched_list if m["host"] in user_data["subscriptions"]]
    return rec_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    # Recommend movie based on user's favorite genre
    fav_genre = get_most_watched_genre(user_data)
    friends_watched_list = get_friends_unique_watched(user_data)
    # m is a movie dictionary
    rec_list = [m for m in friends_watched_list if m["genre"] == fav_genre]
    return rec_list

def get_rec_from_favorites(user_data):
    rec_list = []
    # Make list of movies that the friends have watched, on one level
    friends_watched_list = []
    for friend in user_data["friends"]:
        friends_watched_list += friend["watched"]

    # Add to rec_list any user favorite movie that friends haven't watched
    for movie in user_data["favorites"]:
        if movie not in friends_watched_list:
            rec_list.append(movie)

    return rec_list