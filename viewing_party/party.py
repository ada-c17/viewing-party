# ------------- WAVE 1 --------------------

from tests.test_constants import MOVIE_TITLE_1


def create_movie(title, genre, rating):
    '''
    take three parameters: `title`, `genre`, `rating`
    If those three attributes are truthy, then return a dictionary. 
    This dictionary should...
    Have three key-value pairs, with specific keys
    The three keys should be `"title"`, `"genre"`, and `"rating"`
    The values of these key-value pairs should be appropriate values
    If `title` is falsy, `genre` is falsy, or `rating` is falsy, 
    this function should return `None`
    
    '''
    if title and genre and rating:
        dict = {"title": title,
                "genre": genre,
                "rating": rating}
        return dict
    return None


def add_to_watched(user_data, movie):
    '''
    take two parameters: `user_data`, `movie`
    the value of `user_data` will be a dictionary with a key `"watched"`, 
    and a value which is a list of dictionaries representing the movies the user has watched
    An empty list represents that the user has no movies in their watched list
    the value of `movie` will be a dictionary in this format:
    - ```python
    {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }
    ```
    add the `movie` to the `"watched"` list inside of `user_data`
    return the `user_data`
    
    '''
    #user_data = { “watched”: []}, never watched any movie
    #user_data = {“watched”: [{“title”: “title A”, “genre”: “horror”, “rating”: 4}]}
    #movie is a dict, user_data is a dict, watch value is list
    user_data["watched"].append(movie)
    return user_data
    

def add_to_watchlist(user_data, movie):
    '''
    take two parameters: `user_data`, `movie`
    the value of `user_data` will be a dictionary with a key `"watchlist"`, and a value which is a list of dictionaries representing the movies the user wants to watch
    An empty list represents that the user has no movies in their watchlist
    the value of `movie` will be a dictionary in this format:
    ```python
    {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }
    ```
    add the `movie` to the `"watchlist"` list inside of `user_data`
    return the `user_data`
    
    '''
    user_data["watchlist"].append(movie)
    return user_data 


def watch_movie(user_data, title):
    '''
    take two parameters: `user_data`, `title`
    the value of `user_data` will be a dictionary with a `"watchlist"`and a `"watched"`
    This represents that the user has a watchlist and a list of watched movies
    the value of `title` will be a string
    This represents the title of the movie the user has watched
    If the title is in a movie in the user's watchlist:
    remove that movie from the watchlist
    add that movie to watched
    return the `user_data`
    If the title is not a movie in the user's watchlist:
    return the `user_data`
    Note: For Waves 2, 3, 4, and 5, your implementation of each 
    of the functions should not modify `user_data`.
'''
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data

    return user_data




# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# {"watched":[rating: 3.3]}
def get_watched_avg_rating(user_data):
    '''
    take one parameter: `user_data`
    the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries
    This represents that the user has a list of watched movies
    Calculate the average rating of all movies in the watched list
    The average rating of an empty watched list is `0.0`
    return the average rating
    
    '''
    avgerage_rating = 0
    total_rating = 0
    if user_data["watched"]:
        for movie in user_data["watched"]:
            total_rating += movie["rating"]
        avgerage_rating = total_rating/len(user_data["watched"])
        return avgerage_rating
    else: 
        return 0.0


def get_most_watched_genre(user_data):
    '''
    take one parameter: `user_data`
    the value of `user_data` will be a dictionary with a `"watched"` 
    list of movie dictionaries. Each movie dictionary has a key `"genre"`.
    This represents that the user has a list of watched movies. 
    Each watched movie has a genre.
    The values of `"genre"` is a string.
    Determine which genre is most frequently occurring in the watched list
    return the genre that is the most frequently watched
    If the value of "watched" is an empty list, `get_most_watched_genre` should return `None`.
    
    '''
    #if user's watched list is not empty, we count the number of genre 
    #watched most frequently  
    #["horror", "fantasy", "horror"]
    #{"horror": 2, "fantasy": 1}
    frequent_genre = None
    genre_counts = {}
    most_watched_count = 0
    if user_data["watched"]:
        for movie in user_data["watched"]:
            
            if movie["genre"] in genre_counts:
                genre_counts[movie["genre"]]+=1
            else: 
                genre_counts[movie["genre"]]= 1
        
        for genre in genre_counts:
            if genre_counts[genre] > most_watched_count:
                most_watched_count = genre_counts[genre]
                frequent_genre = genre
        return frequent_genre  
    return frequent_genre



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def combined_friends(friends):
    '''
    This is a helper function to combine 
    the two friend watched lists in the user data
    It will be used by the two below functions
    '''
    #helper function
    # put two friends watched movie into new list 
    # loop all friends watched list and append it to a list
    combined_friend_watch = [] 
    for friend in friends:
        for watch in friend["watched"]:  
            combined_friend_watch.append(watch)
    return combined_friend_watch


def get_unique_watched(user_data):
    '''
    take one parameter: `user_data`
    the value of `user_data` will be a dictionary with a `"watched"` 
    list of movie dictionaries, and a `"friends"`
    This represents that the user has a list of watched movies 
    and a list of friends
    The value of `"friends"` is a list
    Each item in `"friends"` is a dictionary. 
    This dictionary has a key `"watched"`, 
    which has a list of movie dictionaries.
    Each movie dictionary has a `"title"`.
    Consider the movies that the user has watched, 
    and consider the movies that their friends have watched. 
    Determine which movies the user has watched, but none of their friends have watched.
    Return a list of dictionaries, that represents a list of movies
    
    '''
    #user has watched and none of friends have watched
    #loop user watched dict,take user first movie compared to my friend first movie
    #check if user watched movie is not in friends'combined watched list
    #then added to user_watched_friends_not list
    
    friends = user_data["friends"]
    user_watched_friends_not = []
    

    for movie in user_data["watched"]:
        if movie not in combined_friends(friends):
            user_watched_friends_not.append(movie)
    return user_watched_friends_not

def get_friends_unique_watched(user_data):
    '''
    take one parameter: `user_data`
    the value of `user_data` will be a dictionary with 
    a `"watched"` list of movie dictionaries, and a `"friends"`
    This represents that the user has a list of watched movies 
    and a list of friends
    The value of `"friends"` is a list
    Each item in `"friends"` is a dictionary. 
    This dictionary has a key `"watched"`, which has a list of movie dictionaries.
    Each movie dictionary has a `"title"`.
    Consider the movies that the user has watched, 
    and consider the movies that their friends have watched. 
    Determine which movies at least one of the user's friends have watched, 
    but the user has not watched.
    Return a list of dictionaries, that represents a list of movies

    '''
    #friends have watched but user hasn't watched
    #loop through friend combined list (helper function)
    #check if friend watched is not in user watched list
    #and friend_have_watched_user_not list(to prevent duplicate)
    #if not add to friend_have_watched_user_not list

    friends = user_data["friends"]

    friends_have_watched_user_not = []

    for friend_watch in combined_friends(friends):
        if (friend_watch not in user_data["watched"] 
            and friend_watch not in friends_have_watched_user_not):

            friends_have_watched_user_not.append(friend_watch)
    return friends_have_watched_user_not


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    '''
    takes one parameter: `user_data`
    `user_data` will have a field `"subscriptions"`. 
    The value of `"subscriptions"` is a list of strings
    This represents the names of streaming services that the user has access to
    Each friend in `"friends"` has a watched list. 
    Each movie in the watched list has a `"host"`, 
    which is a string that says what streaming service it's hosted on
    Determine a list of recommended movies. 
    A movie should be added to this list if and only if:
    The user has not watched it
    At least one of the user's friends has watched
    The `"host"` of the movie is a service that is in the user's `"subscriptions"`
    Return the list of recommended movies
    
    '''
    #user_data={"watched":[{}],"subscriptions": ["Netflix", "hulu"]}
    #friends={"watched":[{“title”: “title A”, “genre”: “horror”, “rating”: 4,"host": "Netflix"}]}
    #create a list of user subscription and a list of recommended movie
    #loop through user subscription and append to subscripton list
    #loop through friend unique watched list and 
    ##if subscription and not watch, add to recommend list
    #check if the host exist in user_subscription list
    #append the movie to the recommended_movies
    #return recommended movies
    recommended_movies = []
    user_subscription = []
    

    for sub in user_data["subscriptions"]:
        user_subscription.append(sub)
    print(user_subscription)

    for movie in get_friends_unique_watched(user_data):
        if movie["host"] in user_subscription:
            recommended_movies.append(movie)
    return recommended_movies



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    '''
    takes one parameter: `user_data`
    Consider the user's most frequently watched genre. 
    Then, determine a list of recommended movies. 
    A movie should be added to this list if and only if:
    The user has not watched it
    At least one of the user's friends has watched
    The `"genre"` of the movie is the same as the user's most frequent genre
    Return the list of recommended movies
    '''
    #recommended =[{“title”: “title A”, “genre”: “horror”}]
    #use the function from previous to get most watched genre
    #iterate over friend unique watch(movie friend watch user hasn't)
    #for each movie if it is in the popular genre add to recommend list
    #movie = {"title":"title", "genre":"genre"}
    recommend_movie = []
    popular_genre = get_most_watched_genre(user_data)

    for movie in get_friends_unique_watched(user_data):
        if popular_genre == movie["genre"]:
            recommend_movie.append(movie)
    return recommend_movie


def get_rec_from_favorites(user_data):
    '''
    takes one parameter: `user_data`
    `user_data` will have a field `"favorites"`. 
    The value of `"favorites"` is a list of movie dictionaries
    This represents the user's favorite movies
    Then, determine a list of recommended movies. 
    A movie should be added to this list if and only if:
    The movie is in the user's `"favorites"`
    None of the user's friends have watched it
    Return the list of recommended movie
    '''

    #favorites = [{}]
    #use previous user unique watched list(get_unique_watched) 
    #to get user has watched friends have not
    #loop through user favorites and check if it in the user unique watched list
    #If yes, add to recommend movie list


    favorites = []
    recommended_movies = []
    possible_recom = get_unique_watched(user_data)

    for movie in user_data["favorites"]:
        if movie in possible_recom:
            recommended_movies.append(movie)
    return recommended_movies
        


