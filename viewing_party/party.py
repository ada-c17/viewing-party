# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if title == None:
        return None
    elif genre == None:
        return None
    elif rating == None:
        return None
    else:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, movie):
    movie_index = -1

    # find index of watched movie in watchlist list
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == movie:
            movie_index = i

    # if movie is found to be in watchlist
    if movie_index >= 0:
        # remove element at that index from watchlist list and add to variable
        watched_movie = user_data["watchlist"].pop(movie_index)

        # add variable to watched list
        user_data["watched"].append(watched_movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    # add up ratings
    sum = 0
    average = 0
    if len(user_data["watched"]) > 0:
        for i in range(len(user_data["watched"])):
            sum += user_data["watched"][i]["rating"]
        # divide total by number of movies (length of list) to get average
        average = sum / len(user_data["watched"])

    return average

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) > 0:
        # make new list of just genres
        genre_list = []

        for i in range(len(user_data["watched"])):
            genre_list.append(user_data["watched"][i]["genre"])
        
        most_watched_count = 0
        most_watched_genre = ''
        # iterate through genre list, updating most_watched_genre as counts increase
        for genre in genre_list:
            genre_count = genre_list.count(genre)
            if genre_count > most_watched_count:
                most_watched_count = genre_count
                most_watched_genre = genre

        return most_watched_genre
    else:
        return None
        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # create empty list to store unique movies
    user_unique_watched = []

    # iterate over user's watched list
    for i in range(len(user_data["watched"])):
        # set flag to signal if we're still looking
        searching_for_movie = True

        # set current title we're looking for
        looking_for_title = user_data["watched"][i]["title"]

        while searching_for_movie:
            friend_index = 0
            # iterate through friends list
            for friend in user_data["friends"]:
                # iterate through every movie on friend's watch list
                if searching_for_movie:
                    for num in range(len(user_data["friends"][friend_index]["watched"])):
                        # if title matches title we're looking for, break out of loop and start looking for next title
                        # once a title has been found once, we don't need to see if it's watched by multiple friends
                        if user_data["friends"][friend_index]["watched"][num]["title"] == looking_for_title:
                            searching_for_movie = False
                            break
                        else:
                            continue
                    # increment friend index to check next friend's watched list
                    friend_index += 1
                # if no longer searching for movie, break out of all loops
                if searching_for_movie == False:
                    break

            if searching_for_movie:
                # if after iterating through all friends we are still searching for movie, add it to the unique list
                user_unique_watched.append(user_data["watched"][i])
                # then change flag to switch to next movie
                searching_for_movie = False
        # continue until all movies on user's watch list have been checked. 
        continue

    return user_unique_watched       


def get_friends_unique_watched(user_data):
    friends_unique_watched = []

    friends_unique_watched_titles = []

    friend_index = 0
    
    # iterate through friends list
    for friend in user_data["friends"]:
        # iterate through specific friend's watched list
        for i in range(len(user_data["friends"][friend_index]["watched"])):
            # set title we're currently considering
            looking_for_title = user_data["friends"][friend_index]["watched"][i]["title"]

            searching_for_movie = True
            # start iterating over user's watched list
            for num in range(len(user_data["watched"])):
                # check if title matches item on user's watched list, leave loop if so
                if looking_for_title == user_data["watched"][num]["title"]:
                    searching_for_movie = False
                    break
            if searching_for_movie == False:
                continue
            # if title does not match user's watched list, see if it is already listed on unique_watched_list
            elif looking_for_title in friends_unique_watched_titles:
                continue
            else:
                friends_unique_watched_titles.append(looking_for_title)
                friends_unique_watched.append(user_data["friends"][friend_index]["watched"][i])
        # increment friend index
        friend_index += 1
    
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):

    available_recs = []

    friends_watched = get_friends_unique_watched(user_data)
    
    # check friends watched list hosts against user subscriptions
    for i in range(len(friends_watched)):
        if friends_watched[i]["host"] in user_data["subscriptions"]:
            available_recs.append(friends_watched[i])
    
    return available_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

