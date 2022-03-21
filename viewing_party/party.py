#my first commit

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    dict_of_movies = {}
    if title == None or genre  == None or rating == None:
        return None
    dict_of_movies["title"] = title
    dict_of_movies["genre"] = genre
    dict_of_movies["rating"] = rating
    return dict_of_movies

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def  add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(janes_data, MOVIE_TITLE_1):
    for movie in janes_data["watchlist"]:
        if movie["title"]==MOVIE_TITLE_1:
            watched_movie=movie
            janes_data["watched"].append(watched_movie)
            janes_data["watchlist"].remove(movie)
            break
    return (janes_data)
        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum=0
    avarage=0
    count=0
    #if not user_data["watched"]:
    if user_data["watched"]==[]:
        return 0
    for movie in user_data["watched"]:
        sum+=movie["rating"]
    count=len(user_data["watched"])
    avarage=sum/count
    return avarage

def get_most_watched_genre(user_data):
    highest_friqency=0
    most_frequent_genre_name=None

    frequentcy_of_genre={}
    for movie in user_data["watched"]:
        genre=movie["genre"]
        if genre in frequentcy_of_genre:
            frequentcy_of_genre[genre]+=1
        else:
            frequentcy_of_genre[genre]=1

    for frequency in frequentcy_of_genre:
        if frequentcy_of_genre[frequency]  >  highest_friqency:
            highest_friqency = frequentcy_of_genre[frequency] 
            most_frequent_genre_name=frequency

    return most_frequent_genre_name

    


            


        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

