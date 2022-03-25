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
    sum_rating += rating
    count += 1 #adding counter everytime goes through watched dictionary
  if count != 0:
    average_rating = sum_rating / count
    return average_rating
  else:
    return average_rating #this works because avg_rating italized to 0

def get_most_watched_genre(user_data):
  genres_list = []
  for i in range(len(user_data["watched"])):
    genre = user_data["watched"][i]['genre']
    genres_list.append(genre)

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
  unique_list_user_watched = []

  for i in user_data["watched"]: #iterating through every value
    movies_user_watched.append(i)

  for i in range(len(user_data["friends"])):
    for item in user_data["friends"][i]["watched"]: #this loop goes into the 2 watched key inside friends key
      movies_friends_watched.append(item) #append all movies that friends watched

  for i in movies_user_watched: #comparing elements in movies_user_watched to movies_friends_watched
    if i not in movies_friends_watched:
      unique_list_user_watched.append(i)
  return unique_list_user_watched

def get_friends_unique_watched(user_data): #Test 16 is similar to test 15, instead of testing for 
  #movies watched by user and not friends, we test for movies watched by friends but not user. 

  movies_friends_watched = [] 
  movies_user_watched = []
  unique_list_friends_watched = []
  no_dup_list = []

  for i in user_data["watched"]:
    movies_user_watched.append(i)

  for i in range(len(user_data["friends"])): #0,1,2,3,4,5,6,7
    for item in user_data["friends"][i]["watched"]: #this loop goes into the 2 watched key inside friends key
      movies_friends_watched.append(item) #append all movies that friends watched

  for i in movies_friends_watched:
    if i not in movies_user_watched:
      unique_list_friends_watched.append(i)

  for i in unique_list_friends_watched: #go through unique_list_friends_watched
    if i not in no_dup_list: #if each movie is not already in no_dup_list
      no_dup_list.append(i) #append the movie to this list. thus not appending any duplicate movies
  return no_dup_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
  movies_friends_watched = []
  movies_user_watched = []
  recommended_movies = []
  movies_friends_no_dup = []

  for movie in user_data["watched"]:
    movies_user_watched.append(movie)

  for movie in range(len(user_data["friends"])):
    for friends_watched in user_data["friends"][movie]["watched"]:
      movies_friends_watched.append(friends_watched)

  for movie in movies_friends_watched: #testing for duplicates from friends and user
    if movie not in movies_user_watched:
      movies_friends_no_dup.append(movie) #list without duplicates

  for movie in movies_friends_no_dup: #list without duplicates and compare movie["host"] is in list of subscriptions
    if movie["host"] in user_data["subscriptions"]:
      recommended_movies.append(movie)

  return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
  movies_friends_watched = []
  movies_user_watched = []
  movies_friends_no_dup = []
  recommended_movies = []
  most_watched_genre = ""
  
  for movie in user_data["watched"]:
    movies_user_watched.append(movie)

  for movie in range(len(user_data["friends"])):
    for friends_watched in user_data["friends"][movie]["watched"]:
      movies_friends_watched.append(friends_watched)

  for movie in movies_friends_watched: #testing for duplicates from friends and user
    if movie not in movies_user_watched:
      movies_friends_no_dup.append(movie) #list without duplipcates

  most_watched_genre = get_most_watched_genre(user_data) #calling get_most_watched_genre function

  for movie in movies_friends_no_dup: #list without duplicates and compare movie["host"] is in list of subscriptions
    if movie["genre"] == most_watched_genre:
      recommended_movies.append(movie)
  return recommended_movies

def get_rec_from_favorites(user_data):
  fav_movies = []
  movies_friends_watched = []
  for movie in range(len(user_data["friends"])):
    for friends_watched in user_data["friends"][movie]["watched"]:
      movies_friends_watched.append(friends_watched)

  for movie in user_data["favorites"]:
    if movie not in movies_friends_watched:
      fav_movies.append(movie)
  return fav_movies
