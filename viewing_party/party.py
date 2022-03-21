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
  unique_list_user_watched = []

  for i in user_data["watched"]: #iterating through every value
    movies_user_watched.append(i)
  #print(movies_user_watched)
  #print(len(movies_user_watched))

  for i in range(len(user_data["friends"])): #0,1,2,3,4,5,6,7
    for item in user_data["friends"][i]["watched"]: #this loop goes into the 2 watched key inside friends key
      movies_friends_watched.append(item) #append all movies that friends watched
    #print(movies_friends_watched)

  for i in movies_user_watched: #comparing elements in movies_user_watched to movies_friends_watched
    if i not in movies_friends_watched:
      unique_list_user_watched.append(i)
  #print(unique_list)
  return unique_list_user_watched

def get_friends_unique_watched(user_data): #Test 16 is similar to test 15, instead of testing for 
  #movies watched by user and not friends, we test for movies watched by friends but not user. 
  ### I need to make this code more efficient because i copied and pasted it from previous function.
  movies_friends_watched = [] 
  movies_user_watched = []
  unique_list_friends_watched = []
  no_dup_list = []

  for i in user_data["watched"]: #iterating through every value
    movies_user_watched.append(i)
  #print(movies_user_watched)
  #print(len(movies_user_watched))

  for i in range(len(user_data["friends"])): #0,1,2,3,4,5,6,7
    for item in user_data["friends"][i]["watched"]: #this loop goes into the 2 watched key inside friends key
      movies_friends_watched.append(item) #append all movies that friends watched
    #print(movies_friends_watched)

  for i in movies_friends_watched:
    if i not in movies_user_watched:
      unique_list_friends_watched.append(i)
      #print(i)
    print(unique_list_friends_watched) #last two elements are duplicates
  #print(len(unique_list_friends_watched)) #prints 4 but expected 3
  for i in unique_list_friends_watched: #go through unique_list_friends_watched
    if i not in no_dup_list: #if each movie is not already in no_dup_list
      no_dup_list.append(i) #append the movie to this list. thus not appending any duplicate movies
  return no_dup_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
  recommended_movies = []
  movies_friends_watched = [] 
  movies_user_watched = []
  user_host_list = []
  for movie in user_data["watched"]:
    movies_user_watched.append(movie)
  print(movies_user_watched)
  print()
  print()
  for movie in range(len(user_data["friends"])):
    for friends_watched in user_data["friends"][movie]["watched"]:
      movies_friends_watched.append(friends_watched)
  print(movies_friends_watched)
  print("hi")
  for movie in movies_friends_watched:
    if movie not in movies_user_watched: #and user_data["watched"][movie]["host"] == 'hulu' or 'netflix':
      recommended_movies.append(movie)
  print(recommended_movies) #rn i have the unique recommended movies
  # but do not have the host distinguished 
  #seems like the next step, after having the recommended movies, 
  # is to compare the recommended movies host and once again code it make it equal user subscription


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
