# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    if title and genre and rating:
        new_movie = {}
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    for index in range(0, len(user_data["watchlist"])):
        nested_movie_title_watched = user_data["watchlist"][index]["title"]
        if movie_title in nested_movie_title_watched:
            correct_movie = user_data["watchlist"][index]
            user_data["watched"].append(correct_movie)
            user_data["watchlist"].remove(correct_movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    if user_data["watched"]:
        rating_list = []
        for index in range(0, len(user_data["watched"])):
            rating= user_data["watched"][index]["rating"]
            rating_list.append(rating)
            average = sum(rating_list)/ len(rating_list)
        return average
    else:
        return 0.0

def get_most_watched_genre(user_data):

    if user_data["watched"]:
        genre_freq = {}
        for index in range(0, len(user_data["watched"]) -1):
            genre_name = user_data["watched"][index]["genre"]
            if genre_freq and genre_name in genre_freq:
                genre_freq[genre_name] += 1
            else:
                genre_freq[genre_name] = 1
        most_watched = max(genre_freq.values())

        for key in genre_freq:
            if genre_freq[key] == most_watched:
                return key
    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_user_watch_list(user_data):

    user_list = []
    for movie in user_data["watched"]:
        title = movie["title"]
        user_list.append(title)
    
    return user_list

def get_friends_watch_list(user_data):
    
    friend_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            friend_list.append(title)

    return friend_list

def get_unique_watched(user_data):

    user_list = get_user_watch_list(user_data)
    friend_list = get_friends_watch_list(user_data)

    diff = set(user_list) - set(friend_list)
    unique_list = list(diff)

    final_dict = []
    for movie in user_data["watched"]:
        if movie["title"] in unique_list:
            final_dict.append(movie)

    return final_dict

def get_friends_unique_watched(user_data):

    user_list = get_user_watch_list(user_data)
    friend_list = get_friends_watch_list(user_data)
    
    diff = set(friend_list) - set(user_list)
    unique_list = list(diff)

    final_dict = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in unique_list:
                if movie not in final_dict:
                    final_dict.append(movie)

    return final_dict
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

