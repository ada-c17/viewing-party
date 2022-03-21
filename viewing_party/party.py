# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {'title': title, 'genre': genre, 'rating': rating}
    else:
        return None
    
    return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_dict, movie_title):
    movie_watched = None
    for i in range(len(user_dict["watchlist"])):
        if user_dict["watchlist"][i]["title"] == movie_title:
            movie_watched = user_dict["watchlist"].pop(i)
    if movie_watched == None:
        return user_dict
    else:
        user_dict["watched"].append(movie_watched)
    return user_dict


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_dict):
    rating_total = 0
    if user_dict["watched"]:
        for i in range(len(user_dict["watched"])):
            rating_total += user_dict["watched"][i]["rating"]
            avg_rating = rating_total / (i + 1)
    else:
        avg_rating = 0
    return avg_rating

def get_most_watched_genre(user_dict):
    if user_dict["watched"]:
        genre_count = {}
        
        for i in range(len(user_dict["watched"])):
            genre = user_dict["watched"][i]["genre"]
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1
        return max(genre_count, key=lambda key:genre_count[key])
    else:
        return None
    


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_dict):
    friends_watched_list = user_dict["friends"]
    combined_friends_list = []
    for watched_dict in friends_watched_list:
        combined_friends_list.extend(watched_dict["watched"])
    users_watched_list = user_dict["watched"]
    unique_watched = []
    for movie in users_watched_list:
        if movie not in combined_friends_list:
            unique_watched.append(movie)
    return unique_watched


def get_friends_unique_watched(user_dict):
    friends_watched_list = user_dict["friends"]
    combined_friends_list = []
    for watched_dict in friends_watched_list:
        combined_friends_list.extend(watched_dict["watched"])
    users_watched_list = user_dict["watched"]
    unique_watched = []
    for movie in combined_friends_list:
        if movie not in users_watched_list:
            if movie not in unique_watched:
                unique_watched.append(movie)
    return unique_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

