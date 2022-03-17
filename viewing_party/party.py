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
  user_data["watched"].append(movie) #append returns None
  return user_data
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

