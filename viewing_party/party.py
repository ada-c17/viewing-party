# ------------- WAVE 1 --------------------
#1
def create_movie(title, genre, rating):
    movie_dict = {}
    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else:
        return None
#2    
def add_to_watched(user_data, movie):
    for value in user_data.values():
        value.append(movie)
        return user_data
#3    
def add_to_watchlist(user_data, movie):
    for value in user_data.values():
        value.append(movie)
        return user_data
#4    
def watch_movie(user_data, title):
    for key, value in user_data.items():
        for i in range(len(value)):
            print(value) #[{}, {}]
            if title == value[i]["title"]:
                del value[i]
                user_data["watched"].append(title)
                return user_data
            
    return user_data

janes_data = {
        "watchlist": [{
            'genre': 'Fantasy', 
            'rating': 4.8, 
            'title': 'The Lord of the Functions: The Fellowship of the Function'}, 
            {'genre': 'Horror', 
            'rating': 3.5, 
            'title': 'It Came from the Stack Trace'
            }],
        "watched": ["The Lord of the Functions: The Two Parameters"]
    }
dict = watch_movie(janes_data, "It Came from the Stack Trace")        
print(dict)     
    
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

