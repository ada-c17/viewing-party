
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    if title and genre and rating:
        movie_dict = {}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
    else:
        return None
    
    return movie_dict


def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)

    return user_data


def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, title):

#loop through the dictionaries in the list user_data["watchlist"]
#if the dictionary key == "title", check if the value == title (parameter)
#if the value == title, save the dictionary to user_data["watched"]. Then delete the dictionary from user_data["watchlist"]


    for dict in user_data["watchlist"]:
        if dict["title"] == title:
            user_data["watched"].append(dict)
            user_data["watchlist"].remove(dict)

    return user_data


# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):

    ratings_list = []
    
    if len(user_data["watched"]) > 0:
        for dict in user_data["watched"]:
            ratings_list.append(dict["rating"])
        
        average_rating = sum(ratings_list) / len(ratings_list)
        
    else:
        average_rating = 0.0
    
    return average_rating
    
    
def get_most_watched_genre(user_data):

    genre_frequency = {}


    if len(user_data["watched"]) > 0:
        for dict in user_data["watched"]:
            for k, v, in dict.items():
                if k == "genre":
                    if v not in genre_frequency:
                        genre_frequency[v] = 1
                    else:
                        genre_frequency[v] += 1

 
        most_frequent_genre = max(genre_frequency, key=genre_frequency.get)
    
    else:
        most_frequent_genre = None

    return most_frequent_genre


# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):

    friend_watched = []
    difference = []

    for dict in user_data["friends"]:
        for k, v, in dict.items():
                if k == "watched":
                    friend_watched.extend(v)
        
    for dict in user_data["watched"]:
        if dict not in friend_watched:
            difference.append(dict)

    return difference


def get_friends_unique_watched(user_data):

    friend_watched = []
    difference1 = []
    difference2 = []

    for dict in user_data["friends"]:
        for k, v, in dict.items():
                if k == "watched":
                    friend_watched.extend(v)
        
    for dict in friend_watched:
        if dict not in user_data["watched"]:
            difference1.append(dict)

    for i in difference1:
        if i not in difference2:
            difference2.append(i)
    
    return difference2


# ------------- WAVE 4 --------------------

def get_available_recs(user_data):

    reco_movies = []
    friends_unique_watched = get_friends_unique_watched(user_data)


    for dict in friends_unique_watched:
        if dict["host"] in user_data["subscriptions"]:
            reco_movies.append(dict)

    return reco_movies


# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):

    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)

    reco_by_genre = []

    for dict in friends_unique_watched:
        if dict["genre"] == most_watched_genre:
            reco_by_genre.append(dict)

    return reco_by_genre


def get_rec_from_favorites(user_data):

    recos = []
    friend_watched = []

    for dict in user_data["friends"]:
            for k, v, in dict.items():
                    if k == "watched":
                        friend_watched.extend(v)

    for dict in user_data["favorites"]:
        if dict not in friend_watched:
            recos.append(dict)

    return recos