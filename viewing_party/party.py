def create_movie(title,genre,rating):
    if not title or not genre or not rating:
        return None
    return {"title":title,"genre":genre,"rating":rating}

def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    index_to_move = None # initiate flag index_to_move to store index of movie in watchlist if movie is found to later append it to watched and remove it from watchlist
    for index, movie in enumerate(user_data["watchlist"]):
        if movie["title"] == title:
            index_to_move = index
            break # break here to save the for loop redundant additional iterations
    if index_to_move is not None: # cannot use if not index_to_move as 0 is a valid index number but evaluated as a falsey
        user_data["watched"].append(user_data["watchlist"][index_to_move])
        del user_data["watchlist"][index_to_move]   
    return user_data

def get_watched_avg_rating(user_data):
    ratings_sum = 0 
    n = len(user_data["watched"])
    if n == 0:
        return 0
    for movie in user_data["watched"]:
        ratings_sum+=movie["rating"]
    return ratings_sum/n
        
def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    genre_counts = {}
    max_count = 0 # initiate max_count variable to 0 to keep track of max occurrences we've seen with each iteration of the for loop
    max_genre = None # initiate max_genre variable to None to keep track of which genre we've seen has the max occurrences with each iteration of the for loop
    for movie in user_data["watched"]:
        genre = movie["genre"]
        genre_counts[genre] = genre_counts.get(genre,0)+1 # create genre_counts[genre] and set to 1 if doesn't exist, add 1 if it does for each time we see a movie with the genre
        if genre_counts[genre] > max_count:
            max_count = genre_counts[genre]
            max_genre = genre
    return max_genre

def get_unique_watched(user_data):
    friends_list = user_data["friends"]
    watched_list = user_data["watched"]
    friends_watched = []
    no_overlap = []
    for friend in friends_list:
        for movie in friend["watched"]:
            if movie not in friends_watched and movie in watched_list:
                friends_watched.append(movie)
    for watched_movie in watched_list:
        if watched_movie not in friends_watched:
            no_overlap.append(watched_movie)
    return no_overlap

def get_friends_unique_watched(user_data):
    friends_list = user_data["friends"]
    watched_list = user_data["watched"]
    friends_watched_unique = []
    for friend in friends_list:
        for movie in friend["watched"]:
            if movie not in friends_watched_unique and movie not in watched_list:
                friends_watched_unique.append(movie)
    return friends_watched_unique

def get_available_recs(user_data):
    friends_watched_unique = get_friends_unique_watched(user_data) # use get_friends_unique_watched first so later we only have to check if each movie's host is one in user's subscriptions
    recommended = []
    for movie in friends_watched_unique:
        if movie["host"] in user_data["subscriptions"]:
            recommended.append(movie)
    return recommended

def get_new_rec_by_genre(user_data):
    genre_rec = []
    most_watched_genre = get_most_watched_genre(user_data)
    overall_recs = get_friends_unique_watched(user_data)
    for rec in overall_recs:
        if rec["genre"] == most_watched_genre:
            genre_rec.append(rec)
    return genre_rec

def get_rec_from_favorites(user_data):
    friends_list = user_data["friends"]
    fav_list = user_data["favorites"]
    friends_watched = []
    no_overlap = []
    for friend in friends_list:
        for movie in friend["watched"]:
            if movie not in friends_watched and movie in fav_list:
                friends_watched.append(movie)
    for fav_movie in fav_list:
        if fav_movie not in friends_watched:
            no_overlap.append(fav_movie)
    return no_overlap