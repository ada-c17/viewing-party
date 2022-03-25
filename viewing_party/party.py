
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    creating a movie dictionary where arguments title, genre, 
    & rating are dict values
    '''
    #initializing dictionary
    movie_dict = {}
    #error handling for None inputs
    if title is None or genre is None or rating is None:
        return None
    #adding in key-value pairs to dict
    movie_dict["title"] = title
    movie_dict["genre"] = genre 
    movie_dict["rating"] = rating
    return movie_dict

def add_to_watched(user_data, movie):
    '''
    Adding in movie to user's watched list
    '''
    #adding in key-value pairs to dict where movie is a list nested in the dict
    user_data["watched"] =  [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    Adding in movie to user's watchlist list
    '''
    #adding in key-value pairs to dict where movie is a list nested in the dict
    user_data["watchlist"] =  [movie]
    return user_data

def watch_movie(user_data, title):
    '''
    Moving movie into user's watched list if movie is in user's watchlist
    '''
    #looping through user's watchlist
    for i in range(len(user_data["watchlist"])):
        #conditional statement to see if title is in the watchlist
        if user_data["watchlist"][i]["title"] == title:
            #add the movie details to user's watched list
            user_data["watched"].append(user_data["watchlist"][i])
            #remove title from user's watchlist
            user_data["watchlist"].pop(i)
            return user_data
    return user_data

# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    '''
    Calculates the average rating of all movies from the user's watched list
    '''
    #edge case for if user's data is empty
    if not user_data["watched"]:
        return 0
    else:
        #create new list with ratings to find the average
        avg_list = [movie_data['rating'] for movie_data in user_data["watched"]]
        return sum(avg_list) / len(avg_list)

def get_most_watched_genre(user_data):
    '''
    Determines the most watched genre from the user's watched list
    '''    
    #edge case for if user's data is empty
    if not user_data["watched"]:
        return None
    else:
        #initialize most watched dictionary to talley frequency of genre
        most_watched_dict = {}
        #looping through user's watched list to access genre
        for movie_data in user_data["watched"]:
            genre = movie_data["genre"]
            #conditional to talley frequency of each genre
            if genre in most_watched_dict:
                most_watched_dict[genre] += 1
            else:
                most_watched_dict[genre] = 1
        return max(most_watched_dict, key=most_watched_dict.get)


# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):
    '''
    Creates a list of movies where user has watched but their friends have not
    '''
    #initialize lists used for tracking 
    friends_watched_list = []

    #looping through friend's watched list to append title into a list for reference
    for friend in user_data['friends']:
        for movie_data in friend['watched']:
            friends_watched_list.append(movie_data['title'])
    
    #creates final list with movie data if the user's movie title is not in their friends watched list     
    final_list = [movie_data for movie_data in user_data['watched'] \
        if not movie_data['title'] in friends_watched_list]      
    return final_list

def get_friends_unique_watched(user_data):
    '''
    Creates a list of movies where their friends have watched but the user have not
    '''

    #initialize final list which is what gets return at the end of the function
    final_list = []

    #looping through user's watched list to append title into a list for reference
    users_watched_list = [movie_data['title'] for movie_data in user_data['watched']]

    #looping through friend's watchedlist to determine movie titles user has not watched
    for friend in user_data['friends']:
        for movie_data in friend['watched']:
            #conditional for if movie title is not in the user's watched list and 
            #if the title has not been added to the final list (to avoid duplicate recommendations)
            if not movie_data['title'] in users_watched_list \
                and not movie_data in final_list:
                final_list.append(movie_data)
    return final_list

# ------------- WAVE 4 --------------------

def get_available_recs(user_data):
    '''
    Creates a list of movies where their friends have watched but the user have not
    AND movie's host is a subcription the user has access to
    '''
    #list of subcription user has
    available_subscriptions = user_data['subscriptions']

    #initialize final list which is what gets return at the end of the function
    final_list = []

    #looping through user's watched list to append title into a list for reference
    users_watched_list = [movie_data['title'] for movie_data in user_data['watched']]

    #looping through friend's watchedlist to determine movie titles user has not watched
    for friend in user_data['friends']:
        for movie_data in friend['watched']:
            #conditional for if movie title is not in the user's watched list,
            # if movie's host in a subcripton user has access to, and 
            # if the title has not been added to the final list (to avoid duplicate recommendations)
            if not movie_data['title'] in users_watched_list and movie_data['host'] \
                in available_subscriptions and not movie_data in final_list:
                    final_list.append(movie_data)
    return final_list

# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):
    '''
    Creates a list of movies where their friends have watched but the user have not
    AND movie's genre is user's top genre
    '''
    #edge case for if user's watched list or friends watched list is empty
    if not user_data["watched"] or not user_data['friends']:
        return []
    else:
        #determine user's top genre by looping through user's watched list
        top_genre_list = [movie_data['genre'] for movie_data in user_data['watched']]
        top_genre = max(set(top_genre_list), key = top_genre_list.count)

        #initialize lists used for tracking - final list is what gets return at the end of the function       
        final_list = []

        #looping through user's watched list to append title into a list for reference
        users_watched_list = [movie_data['title'] for movie_data in user_data['watched']]
            
        #looping through friend's watchedlist to determine movie titles user has not watched
        for friend in user_data['friends']:
            for movie_data in friend['watched']:
            #conditional for if movie title is not in the user's watched list and
            # if movie title is the user's top genre
                if not movie_data['title'] in users_watched_list and movie_data['genre'] == top_genre:
                    final_list.append(movie_data)
        return final_list

def get_rec_from_favorites(user_data):
    '''
    Creates a list of movies where the movie is a user's favorite 
    AND their friend has NOT watched the movie
    '''
    #edge case for if user's watched list or friends watched list is empty
    if not user_data["watched"] or not user_data['friends']:
        return []
    else:
        #initialize list used for tracking
        friends_watched_list = []

        #looping through friend's watched list to append title into a list for reference
        for friend in user_data['friends']:
            for movie_data in friend['watched']:
                friends_watched_list.append(movie_data['title'])
                
        #creates final list with movie data if the user's favorite movie title is not in their friends watched list 
        final_list = [movie_data for movie_data in user_data['favorites'] \
            if not movie_data['title'] in friends_watched_list]        
        return final_list


