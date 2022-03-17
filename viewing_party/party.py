# Testing connection
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}

    if title == None or genre == None or rating == None:
        return None

    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] .append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    rating_lst = []
    for movie in user_data["watched"]:
        rating_lst.append(movie["rating"])
    
    if len(rating_lst) == 0: 
        return 0

    return sum(rating_lst)/len(rating_lst)

def get_most_watched_genre(user_data):
    
    genre_freq = {}
    watched_lst = user_data["watched"]

    # Check empty watched list
    if not watched_lst:
        return None
    
    for movie in watched_lst:
        genre = movie["genre"]
        if genre not in genre_freq.keys():
            genre_freq[genre] = 1
        else:
            genre_freq[genre] += 1

    most_watched_freq = max(genre_freq.values())

    for genre, freq in genre_freq.items():
        if freq == most_watched_freq:
            return genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

