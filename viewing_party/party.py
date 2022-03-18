# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
  dict = {}
  if title and genre and rating:
    return {
      "title": title,
      "genre": genre,
      "rating": rating,
    }
  else:
    return None

def add_to_watched(user_data, movie):
  # user_data = {"watched": [ {} {}]}
  # empty [] means user has no movies 
  user_data["watched"].append(movie) #append returns None when assigned to a variable
  return user_data

def add_to_watchlist(user_data, movie): #adding movides to watchlist
  user_data["watchlist"].append(movie) #via appending movie to dict
  return user_data

def watch_movie(user_data, title):
  if title == user_data["watchlist"][0]["title"]: #suggestion to make variables
    #position = user_data["watchlist"].index("title")
    user_data["watchlist"].pop(0) #leads to empty watchlist 
    user_data["watched"].append(title)
    return user_data
  else:
    return user_data
  print (user_data)
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

