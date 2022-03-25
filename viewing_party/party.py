# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating,
        }

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data['watched'].append(movie)
            return user_data

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0.0
    else:
        sum = 0
        for movie in user_data["watched"]:
            sum += movie["rating"]
        average = sum/len(user_data["watched"])
        return average

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    genre_frequency = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_frequency:
            genre_frequency[genre] += 1
        else:
            genre_frequency[genre] = 1
    max_value = max(genre_frequency, key=genre_frequency.get)
    return max_value
        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    # Frequency of how many times user watched movies.
    movies_frequency = {} # The key is the title and the value is the number of times a user has seen it
    for movie in user_data["watched"]:
        title = movie["title"]
        if title in movies_frequency:
            movies_frequency[title] += 1
        else:
            movies_frequency[title] = 1

    # Frequency chart of how many times the friend watched movies.
    friends_movies_frequency = {} 
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            title = friend_movie["title"]
            if title in friends_movies_frequency:
                friends_movies_frequency[title] += 1
            else:
                friends_movies_frequency[title] = 1
    
    # Determine which movies the user has watched, but none of their friends have watched.
    user_watched_but_not_friends = []
    for not_watched_movie in user_data["watched"]:
        if not_watched_movie["title"] not in friends_movies_frequency:
            user_watched_but_not_friends.append(not_watched_movie)
    return user_watched_but_not_friends


def get_friends_unique_watched(user_data):
    # Frequency of how many times user watched movies.
    movies_frequency = {} # The key is the title and the value is the number of times a user has seen it
    for movie in user_data["watched"]:
        title = movie["title"]
        if title in movies_frequency:
            movies_frequency[title] += 1
        else:
            movies_frequency[title] = 1

    # Frequency chart of how many times the friend watched movies.
    friends_movies_frequency = {} 
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            title = friend_movie["title"]
            if title in friends_movies_frequency:
                friends_movies_frequency[title] += 1
            else:
                friends_movies_frequency[title] = 1
    
    # Determine a movie that at least one of the user's friends have watched, but the user has not.
    friends_watched_but_not_user = []
    seen_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in movies_frequency and movie["title"] not in seen_movies:
                friends_watched_but_not_user.append(movie)
                seen_movies.append(movie["title"])
    return friends_watched_but_not_user

            
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    # Determine a list of recommended movies.
    recommended_movies = []
    
    # The user has not watched it and at least one of the user's friends has watched
    friends_watched_but_not_user = get_friends_unique_watched(user_data)

    # The "host" of the movie is a service that is in the user's "subscriptions"
    for movie in friends_watched_but_not_user: 
        if movie['host'] in user_data['subscriptions']:
            recommended_movies.append(movie)

    # Return the list of recommended movies
    return recommended_movies 


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    # Determine a list of recommended movies
    recommended_movies = []

    # The user has not watched it and at least one of the user's friends has watched
    friends_watched_but_not_user = get_friends_unique_watched(user_data)

    # The "genre" of the movie is the same as the user's most frequent genre
    user_most_frequent_genre = get_most_watched_genre(user_data)
    for movie in friends_watched_but_not_user: 
        if movie['genre'] == user_most_frequent_genre:
            recommended_movies.append(movie)

    # Return the list of recommended movies
    return recommended_movies 


def get_rec_from_favorites(user_data):
    # Determine a list of recommended movies
    recommended_movies = []

    # The movie is in the user's "favorites"
    movies_favorites = {} 
    for movie in user_data["favorites"]:
        title = movie["title"]
        if title in movies_favorites:
            movies_favorites[title] += 1
        else:
            movies_favorites[title] = 1

    # None of the user's friends have watched it
    friends_movies_frequency = {} 
    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            title = friend_movie["title"]
            if title in friends_movies_frequency:
                friends_movies_frequency[title] += 1
            else:
                friends_movies_frequency[title] = 1

    # Determine which movies the user has watched, but none of their friends have watched.
    for not_watched_movie in user_data["favorites"]:
        if not_watched_movie["title"] not in friends_movies_frequency:
            recommended_movies.append(not_watched_movie)

    # Return the list of recommended movies
    return recommended_movies 