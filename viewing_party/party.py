# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    new_movie = {}
    if movie_title == None or genre == None or rating == None:
        new_movie = None
        return new_movie
    else:
        new_movie = {'title':movie_title,'genre':genre, 'rating':rating}
        return new_movie

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    count = 0
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            add_to_watched(user_data,movie)
            del(user_data["watchlist"][count])
        count += 1
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0
    for i in range (0,len(user_data["watched"])):
        print(user_data["watched"][i]["rating"])
        sum += user_data["watched"][i]["rating"]
    if sum == 0:
        average = 0.0
        return average
    else:
        average = sum/len(user_data["watched"])
        return average

def get_most_watched_genre(user_data):
    genre_counts = {}
    counter = 0
    if len(user_data['watched']) < 1:
        return None
    for i in range(len(user_data["watched"])):
        genre = user_data["watched"][counter]["genre"]
        genre_count = genre_counts.get(genre,0)
        genre_counts[genre] = genre_count + 1
        counter +=1
    max_genre = max(genre_counts, key=genre_counts.get)
    return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # write code to compare list of persons movies and compares with friends
    # return if not in friends list
    watched_list = []
    list_difference = []
    friends_watched = []
    result = []
    for i in range(len(user_data['watched'])):
        watched_list.append(user_data["watched"][i])
    for i in range(len(user_data['friends'])):
        for movie in range(len(user_data['friends'][i]["watched"])):
            friends_watched.append(user_data['friends'][i]["watched"][movie])
    for movie in watched_list:
        if movie not in friends_watched :
            list_difference.append(movie)
    for movie in list_difference:
        if movie not in result:
            result.append(movie)
    return list_difference

def get_friends_unique_watched(user_data):
    friends_watched = []
    watched_list = []
    list_difference = []
    result = []
    for i in range(len(user_data['watched'])):
        watched_list.append(user_data["watched"][i])
    for i in range(len(user_data['friends'])):
        for movie in range(len(user_data['friends'][i]["watched"])):
            friends_watched.append(user_data['friends'][i]["watched"][movie])
    for movie in friends_watched:
        if movie not in watched_list:
            list_difference.append(movie)
    for movie in list_difference:
        if movie not in result:
            result.append(movie)
    return result
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    movie_recommendations = []
    movie_list = get_friends_unique_watched(user_data)
    for movie in movie_list:    
            if movie["host"] in user_data['subscriptions']:
                movie_recommendations.append(movie)
    return movie_recommendations
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    movie_recommendations = []
    movie_list = get_friends_unique_watched(user_data)
    max_genre = get_most_watched_genre(user_data)
    for movie in movie_list:
        if movie['genre'] == max_genre:
                movie_recommendations.append(movie)
    return movie_recommendations

def get_rec_from_favorites(user_data):
    favorite_recommendations = []
    favorite_list = []
    movie_list = get_friends_unique_watched(user_data)
    for i in range(len(user_data['favorites'])):
        favorite_list.append(user_data["favorites"][i])
    for movie in favorite_list:
        if movie not in movie_list:
            favorite_recommendations.append(movie)
    return favorite_recommendations