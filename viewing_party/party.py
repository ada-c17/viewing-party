# ------------- WAVE 1 --------------------
movies = {}

def create_movie(title, genre, rating):
    if title != None and genre != None and rating != None:
        movies.update({"genre": genre, "rating": rating, "title": title})
        return movies
    else:
        return None

def add_to_watched(user_data, movie):
    user_data.update({"watched": [movie]})
    return user_data

def add_to_watchlist(user_data, movie):
    user_data.update({"watchlist": [movie]})
    return user_data

def watch_movie(user_data, title):

    #work through the whole watchlist; copy it first so no DANGERZONE/index/key errors
    copy_list = user_data["watchlist"]
    for i in range(len(copy_list)):

    #find the title of the movie in the watchlist
        if user_data["watchlist"][i]["title"] == title:

            #if the title is in the watchlist, move it to watched then delete
            user_data["watched"].append(user_data["watchlist"][i])
            del user_data["watchlist"][i]

    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total = 0

    #make sure the dictionary isn't empty
    if user_data["watched"]:
        #iterate over the watched list and add averages to total
        for i in range(len(user_data["watched"])):
            total += user_data["watched"][i]["rating"]

    #if nothing in the watched list, return 0
    else:
        return 0

    #calculate the average and return it
    average = total/len(user_data["watched"])
    return average

def genres(user_data):
    #set up set, dictionary for the count
    genres = set()
    
    #make a set of genres, and return it as a list
    for i in range(len(user_data["watched"])):
        genres.add(user_data["watched"][i]["genre"])
    return list(genres)

def genre_count(user_data):
    #set up set, dictionary for the count
    user_genres = genres(user_data)
    genre_count = {}

    #iterate over the genres and add a count to a dictionary
    for i in range(len(user_data["watched"])):
        count = 0
        for genre in user_genres:
            if user_data["watched"][i]["genre"] == genre:
                count += 1
                genre_count[genre] = count
        return genre_count

def get_most_watched_genre(user_data):
    #make sure the watched list has data
    if user_data["watched"]:
        watched_genre_count = genre_count(user_data)
        most_watched = max(watched_genre_count, key=watched_genre_count.get)
        return most_watched
    
    #if no data, return None
    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_friend_data(user_data):
    #make comprehensive list of all friend data
    friend_data = []
    for i in range(len(user_data["friends"])):
        for j in range(len(user_data["friends"][i]["watched"])):
            friend_data.append(user_data["friends"][i]["watched"][j])
    return friend_data

def get_unique_watched(user_data):
    unique_watched = []
    friend_data = get_friend_data(user_data)

    #iterate over friend data and if movie isn't in friend data, add it to unique_watched
    for i in range(len(user_data["watched"])):
        if user_data["watched"][i] not in friend_data:
            unique_watched.append(user_data["watched"][i])

    return unique_watched

def get_friends_unique_watched(user_data):
    friends_unique_watched = []

    #iterate over friends' watched lists, and if it's not in the user's list,
    #append it to a new list and return it
    for i in range(len(user_data["friends"])):
        for j in range(len(user_data["friends"][i]["watched"])):
            if user_data["friends"][i]["watched"][j] not in user_data["watched"]:
                if user_data["friends"][i]["watched"][j] not in friends_unique_watched:
                    friends_unique_watched.append(user_data["friends"][i]["watched"][j])
    return friends_unique_watched
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    #initialize data
    recommendations = []
    friends_unique_watched = get_friends_unique_watched(user_data)

    #go through list of subscriptions, then find which among user's friend's unique watched
    #user hasn't watched
    for i in range(len(user_data["subscriptions"])):
        for j in range(len(friends_unique_watched)):
            if user_data["subscriptions"][i] == friends_unique_watched[j]["host"]:
                recommendations.append(friends_unique_watched[j])
    return recommendations
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    #initialize data
    friends_unique_watched = get_friends_unique_watched(user_data)
    most_frequent_genre = get_most_watched_genre(user_data)
    recommendations = []   
    #interate over the movies that user's friends have watched,
    #that user has not watched
    for i in range(len(friends_unique_watched)):
        #if a friend's movie is user's favorite genre, recommend it
        if friends_unique_watched[i]["genre"] == most_frequent_genre:
            recommendations.append(friends_unique_watched[i])
    return recommendations

def get_rec_from_favorites(user_data):
    recommendations = []

    #get list of all friend movies watched
    friend_data = get_friend_data(user_data)

    #interate over list of favorites, then see what's in favorites 
    #that aren't in friends watched list.
    for i in range(len(user_data["favorites"])):
        for j in range(len(friend_data)):
            if user_data["favorites"][i] not in friend_data:
                if user_data["favorites"][i] not in recommendations:
                        recommendations.append(user_data["favorites"][i])
    return recommendations