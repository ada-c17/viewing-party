# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_table = {}
    if title and genre and rating:
        movie_table["title"] = title
        movie_table["genre"] = genre
        movie_table["rating"] = rating
        return movie_table
def add_to_watched(user_data,movie):
        if not all((user_data,movie)):
            return None   
        watched = user_data["watched"]
        watched.append(movie)
        print(user_data) 
        return user_data
        # return updated_datas
def add_to_watchlist(user_data,movie):
        if not all((user_data,movie)):
            return None
        watchlist = user_data["watchlist"]
        watchlist.append(movie)
        return user_data
def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    new_watchlist = []
    watched = user_data["watched"]
    
    for item in range(len(list(watchlist))):
        if watchlist[item]["title"] != title:
            new_watchlist.append(watchlist[item])
        else:
            watched.append(title)
    user_data["watchlist"] = new_watchlist

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0
    watched = user_data["watched"]
    print (watched)
    total_rating = 0.0
    for movies in range(len(list(watched))):
        total_rating += watched[movies]["rating"]
    print (total_rating)
    return total_rating/len(watched) 

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    watched = user_data["watched"]
    Genre = []
    temp = {}
    for movie in range(len(list(watched))):
        Genre.append(watched[movie]["genre"])
        # Genre.append("a")
    
    for i in range(len(set(Genre))):
        temp[Genre[i]] = (Genre.count(Genre[i]))
    return(max(temp, key=temp.get))

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

