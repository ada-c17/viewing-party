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
    print(user_data)
def get_unique_watched(user_data):
    set_friends_watched=set()
    list_friend=user_data["friends"]
    for friend in list_friend:
        moview_watched_friend=friend["watched"]
        for movie in moview_watched_friend:
            title=movie["title"]
            set_friends_watched.add(title)
    user_set_of_watched_movies=set()        
    for movie in user_data["watched"]:
        title_of_movie=movie['title']
        user_set_of_watched_movies.add(title_of_movie)

    unique_movies_set=user_set_of_watched_movies.difference(set_friends_watched) 
    list_of_unique_movies=[]   
    for movie in user_data["watched"]:
        if movie["title"]in unique_movies_set:
            list_of_unique_movies.append(movie)
    return list_of_unique_movies  




def get_friends_unique_watched(user_data):
    allMovies=[]
    friends_watched=user_data["friends"]
    for f in friends_watched:
       
        allMovies.extend(f["watched"])
    #result = list(set(val for dic in allMovies for val in dic.values()))

    uniqueMovies = {}
    for movie in allMovies:
        movieTitle = movie["title"]
        if movieTitle in uniqueMovies:
            continue
        else:
            uniqueMovies[movieTitle] = movie
    
    print(uniqueMovies.values())
    return uniqueMovies.values() 


    #helper function
def find_unique_user_movies(user_data):
    list_of_titles=[]
    watched =user_data["watched"]
    for movie in watched:
        title = movie["title"]
        list_of_titles.append(title)
    set_user_unique_movies=set(list_of_titles)   
    return set_user_unique_movies


def find_user_movies(user_data):
    watched =user_data["watched"]
    return watched


def get_friends_unique_watched(user_data):
    list_of_titles=[]
    list_all_movies=[]

    all_friends=user_data["friends"]
#print (all_friends)
    for f in all_friends:
        friend_unique_movies = find_unique_user_movies(f)
        list_of_titles.extend(friend_unique_movies)
        list_all_movies.extend(find_user_movies(f))
#print (list_all_movies)



    set_of_unique_titles_friends=set(list_of_titles)
    set_user_watched = find_unique_user_movies(user_data)


#print(set_of_unique_titles_friends)
    movies_only_friends_watched=set_of_unique_titles_friends.difference(set_user_watched)

    output=[]
    for m in list_all_movies:
        if m["title"] in movies_only_friends_watched:
            output.append(m)
            movies_only_friends_watched.remove(m["title"])
    print (output)  
    return output      



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recom_movies=[]
    unique_movies=get_friends_unique_watched(user_data)
    for movie in unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recom_movies.append(movie)
    return recom_movies        


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommended_movies=[]
    dict_of_freq_genre={}

    watched_by_user=user_data["watched"]

    for movie in watched_by_user:
        if movie["genre"] in dict_of_freq_genre:
            dict_of_freq_genre[movie["genre"]]+=1
        else:
            dict_of_freq_genre[movie["genre"]]=1
    
    print(dict_of_freq_genre)
    most_freq_movie=0
    most_freq_genre_name = ""

    for genre in dict_of_freq_genre:
        if dict_of_freq_genre[genre]>most_freq_movie:
            most_freq_movie=dict_of_freq_genre[genre]
            most_freq_genre_name = genre

    unique_movies=get_friends_unique_watched(user_data)

    for movie in unique_movies:
        if movie["genre"]==most_freq_genre_name:
            recommended_movies.append(movie)
    return recommended_movies        

def get_movies_user_fav_friends_not_watched(user_data):
    set_friends_watched=set()
    list_friend=user_data["friends"]
    for friend in list_friend:
        moview_watched_friend=friend["watched"]
        for movie in moview_watched_friend:
            title=movie["title"]
            set_friends_watched.add(title)
    user_set_of_watched_movies=set()        
    for movie in user_data["watched"]:
        title_of_movie=movie['title']
        user_set_of_watched_movies.add(title_of_movie)

    unique_movies_set=user_set_of_watched_movies.difference(set_friends_watched) 
    list_of_unique_movies=[]   
    for movie in user_data["favorites"]:
        if movie["title"]in unique_movies_set:
            list_of_unique_movies.append(movie)
    return list_of_unique_movies  


def get_rec_from_favorites(user_data):
    recom_fav_movies=[]
    unique_movies_of_friends=get_movies_user_fav_friends_not_watched(user_data)

    for m in user_data["favorites"]:
        if m in unique_movies_of_friends:
            recom_fav_movies.append(m)
    return recom_fav_movies        



