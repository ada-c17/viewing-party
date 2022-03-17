# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        movie = None
    else:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    
    return movie

def add_to_watched(data, movie):
    data["watched"].append(movie)
    return data

def add_to_watchlist(data, movie):
    data["watchlist"].append(movie)
    return data

movie = create_movie("title 1", "genre 1", "rating 1")

user_data = {
        "watched": []
    }

updated_data = add_to_watched(user_data, movie)

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

