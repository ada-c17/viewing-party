# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if title != None and genre != None and rating != None:
        movie_dict = {"title":title, "genre":genre, "rating":rating}
        return movie_dict
    else: 
        return None




def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data



def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data    




def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"]==title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    
    return user_data





# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    avg = 0
    counter = 0
    #for k,v in user_data["watched"]:
    for i in user_data["watched"]:
        for k,v in i.items():
            if k == "rating":
                avg+=v
                counter+=1
    if counter!=0:
        avg = avg/counter
    return avg


def get_most_watched_genre(user_data):

    if len(user_data["watched"]) == 0:
        return None

    genre_dict = {}
    for i in user_data["watched"]:

            for k,v in i.items():

                if k == "genre":

                    key_found = False
                    for key in genre_dict.keys():

                        if key == v:

                            genre_dict[key]+=1

                            key_found = True

                    if key_found == False:
                        genre_dict[v] = 1

    most_watched_num = 0
    most_watched_genre = ""
    for g,f in genre_dict.items():

        if f>most_watched_num:
            most_watched_genre = g
            most_watched_num = f

    return most_watched_genre
        


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):

    unique_movies = []

    #COPY USER'S WATCHED MOVIES
    for x in user_data["watched"]:
        unique_movies.append(x)

    for movie in user_data["watched"]:

        for friend in user_data["friends"]:

            for i in friend["watched"]:
                if i["title"] == movie["title"]:
                    
                    #remove i from unique_movies
                    if i in unique_movies:
                        unique_movies.remove(i)

    return unique_movies
            


def get_friends_unique_watched(user_data):

    unique_movies = []
    #COPY FRIENDS' WATCHED MOVIES
    for friend in user_data["friends"]:
        for i in friend["watched"]:

            if i not in unique_movies:

             unique_movies.append(i)


    for friend in user_data["friends"]:
        #for movie in friend["watched"]:

        for movie in user_data["watched"]:

            for i in friend["watched"]:
                if i["title"] == movie["title"]:

                    #remove i from unique_movies
                    if movie in unique_movies:
                        unique_movies.remove(movie)


    return unique_movies












        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

