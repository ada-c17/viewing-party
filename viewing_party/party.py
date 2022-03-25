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
    watched = user_data
    updated_data = {"watched":[movie]}
    return updated_data

def add_to_watchlist(user_data, movie):
    updated_data = {"watchlist":[movie]}
    return updated_data

def watch_movie(user_data, title):
    updated_data = {}
    new_user_data = {}
    if title in user_data.values():
        new_user_data = user_data["watchlist"]
        updated_data=add_to_watched(user_data,title)
        print(updated_data)
        del(user_data["watchlist"][0])
    else:
        updated_data = user_data
    return updated_data

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
    movie_recommendations = []
    host = None
    movie_list = get_friends_unique_watched(user_data)
    for i in range (0,len(user_data["watched"])):
        genre = user_data["watched"][counter]["genre"]
        print(genre)
        genre_count = genre_counts.get(genre,0)
        genre_counts[genre] = genre_count + 1
        counter +=1
    max_genre = None
    max_value = 0
    for key,value in genre_counts.items():
        if value > max_value:
            max_genre = key
            max_value = value
    return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # write code to compare list of persons movies and compares with friends
    # return if not in friends list
    watched_list = []
    friends_watched = get_friends_unique_watched(user_data)
    for i in range (0,len(user_data["watched"])):
        watched_list.append(user_data["watched"][i]["title"])
    unique_list = set(friends_watched) - set(watched_list)
    return unique_list

def get_friends_unique_watched(user_data):
    friends_watched = []
    watched_list = []
    unique_list = []
    for i in range (0,len(user_data["friends"][1]["watched"])):
        friends_watched.append(user_data["friends"][1]["watched"][i]['title'])
    for i in range (0,len(user_data["watched"])):
            watched_list.append(user_data["watched"][i]["title"])
    unique_list = set(watched_list) - set(friends_watched)
    return unique_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    movie_recommendations = []
    host = None
    movie_list = get_friends_unique_watched(user_data)
    counter = 0
    for movie in range (0, len(movie_list)):
        comparison_movie = user_data["friends"][0]['watched'][counter]['title']
        if comparison_movie in movie_list:
            host = user_data["friends"][0]['watched'][counter]['host']
            if host in user_data["watched"][0]["host"]:
                movie_recommendations.append(comparison_movie)
        counter +=1
    return movie_recommendations
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    genre_counts = {}
    counter = 0
    movie_recommendations = []
    host = None
    movie_list = get_friends_unique_watched(user_data)
    max_value = get_most_watched_genre(user_data)
    friend_rec = get_available_recs(user_data)
    movie_list = get_friends_unique_watched(user_data)
    counter = 0
    for movie in range (0, len(movie_list)):
        comparison_movie = user_data["friends"][0]['watched'][counter]['title']
        if comparison_movie in movie_list:
            genre = user_data["friends"][0]['watched'][counter]['genre']
            if genre in user_data["watched"][0]["genre"]:
                movie_recommendations.append(comparison_movie)
        counter +=1
    return movie_recommendations

def get_rec_from_favorites(user_data):
    favorite_recommendations = []
    movie_list = get_friends_unique_watched(user_data)
    counter = 0
    for movie in range(0,len(movie_list)):
        comparison_movie = user_data['watched'][0][counter]['favorites']
        if comparison_movie in movie_list:
            favorite = user_data['watched'][0]['favorites']
            if favorite in user_data['watched'][0]['favorites']:
                favorite_recommendations.append(comparison_movie)
        counter += 1
    return favorite_recommendations