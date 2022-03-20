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
  user_data["watched"].append(movie) #append returns None when assigned to a variable
  return user_data

def add_to_watchlist(user_data, movie): #adding movides to watchlist
  user_data["watchlist"].append(movie) #via appending movie to dict
  return user_data

def watch_movie(user_data, title):
  for i in range(len(user_data["watchlist"])): #used for loop to iterate through n number of watchlists
    if title == user_data["watchlist"][i]["title"]: #suggestion to make variables
      user_data["watchlist"].pop(i) #leads to empty watchlist, pop only works for index
      user_data["watched"].append(title)
    #print(user_data)
  return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
  average_rating = 0
  sum_rating = 0
  count = 0
  for i in range(len(user_data["watched"])):
    rating = user_data["watched"][i]['rating']
    #rating_in_list.append(rating)
    sum_rating += rating
    count += 1 #adding counter everytime goes through watched dictionary
  if count != 0:
    average_rating = sum_rating / count
    return average_rating
  else:
    return average_rating #this works because avg_rating italized to 0????

def get_most_watched_genre(user_data):
  genres_list = []
  for i in range(len(user_data["watched"])):
    genre = user_data["watched"][i]['genre']
    genres_list.append(genre)
  #print(genres_list) #correct list
  if len(genres_list) != 0:
    most_watched_genre = max(genres_list, key = genres_list.count)
  #using max and count function to count genres and find the most common element
    return most_watched_genre
  else: 
    return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
  movies_friends_watched = []
  movies_user_watched = []
  unique_list = []

  print(user_data)
  for i in user_data["watched"]:
    movies_user_watched.append(i)
  #print(movies_user_watched)
  #print(len(movies_user_watched))

  for i in range(len(user_data["friends"])): #0,1,2,3,4,5,6,7
    for item in user_data["friends"][i]["watched"]:
      movies_friends_watched.append(item)
  #print(movies_friends_watched)

  for i in movies_user_watched: #comparing elements in movies_user_watched to movies_friends_watched
    if i not in movies_friends_watched:
      unique_list.append(i)
  #print(unique_list)
  return unique_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# a = {"abc": [{
#   "123" : [{
#     "abc123": "def456"
#   }]
# }]}

# print(a["abc"][0]["123"][0]["abc123"])