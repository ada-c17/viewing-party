# ------------- WAVE 1 --------------------
# test_wave_01 - line 7 to line 59
from logging import StringTemplateStyle

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    new_movie = {'title':title,
    'genre': genre,
    'rating': rating}
    return new_movie

# test_wave_01 - line 61 to line 81
def add_to_watched(user_data,movie):
    user_data['watched'].append(movie)
    return user_data

# test_wave_01 line 104 to line 121  
def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data
# test_wave_01
def watch_movie(user_data,title):
    
    watch_list = user_data['watchlist']
    for index in range(len(watch_list)):
        movie = watch_list[index]
        if movie['title']==title:
            watch_list.pop(index)
            user_data['watched'].append(movie)
    return user_data

# -----------test_wave_02----------
# line 5 to line 28 on test_wave02

# user_data is a dict with they key=watch list with a dict of movies. 
# movie has 3 keys: title, genre, rating
    # movie_list=user_data['watched']
def get_watched_avg_rating(user_data):
    print(user_data)
    count=0
    score_sum=0
    
    if user_data['watched']==[]:
        average_rating=0.0
    else:
        for movie in user_data['watched']:
            score_sum+= movie['rating']
            count+=1
        average_rating=score_sum/count
    return average_rating

# testwave 02 - line 29 on   
def get_most_watched_genre(user_data):
    movie_list=user_data['watched']
    genre_list=[]
    genre_dict={}
    count=0
    if movie_list==[]:
        return None
    else:
        for movie in movie_list:
            genre_list.append(movie['genre'])
        print(f' the genre list is {genre_list}')            
    for i in genre_list:
        if i in genre_dict:
            genre_dict[i]+=1
        else:
            genre_dict[i]=1
    print(f' the genre dict is {genre_dict}')

    most_often=0
    movies_most_often=None
    for genre in genre_dict:
        if genre_dict[genre]>most_often:
            most_often=genre_dict[genre]
            movies_most_often=genre
        print(f' most often is {movies_most_often}')
        print(f' dict is {genre_dict}')
    
    return movies_most_often
        
#--------------test_wave_03-------------

def get_unique_watched(user_data):
    user_watched_list= user_data['watched']
    friends_list=user_data['friends']
    friends_movie_list=[]
    title_set=set()
    user_unique_movie_list=[]
    
    for friend in friends_list:
        for movie in friend['watched']:
            if movie['title'] not in title_set:
                title_set.add(movie['title'])
                friends_movie_list.append(movie)
    
    for movie in user_watched_list:
        unique = True
        for fmovie in friends_movie_list:
            if movie['title'] == fmovie['title']:
                unique=False
                break      
        if unique:
                user_unique_movie_list.append(movie)
    return user_unique_movie_list

def get_friends_unique_watched(user_data):
    movie_list=user_data['watched']
    friends_list=user_data['friends']
    title_set=set()
    fmovie_list=[]
    
    for friend in friends_list:
        for movie in friend['watched']:
            if movie['title'] not in title_set:
                title_set.add(movie['title'])
                fmovie_list.append(movie)
    
    friends_unique_movie_list=[]
    for fmovie in fmovie_list:
        unique=True
        for movie in movie_list:
            if fmovie['title']==movie['title']:
                unique=False
                break
        if unique:
            friends_unique_movie_list.append(fmovie)
    return friends_unique_movie_list
    
        

        

# -----------test_wave04-------------
'''
user_data has another key called 'subscriptions'.  The value is a list of String that represent the names of \
streaming services that the user has access to

each movie in a friend watched list now has an additional key called 'host'.  The value associated with the host is a string that says what \
streaming service it's hosted on 
call on the previous function to get friend unique watched list
'''

def get_available_recs(user_data):
    recommended_movie_list=[]
    friend_final_movie_list=get_friends_unique_watched(user_data)
    for movie in friend_final_movie_list:
        if movie['host'] in user_data['subscriptions']:
            recommended_movie_list.append(movie)
    return recommended_movie_list
    
#------------test_wave05---------------
#what is the user most frequently watched genre ; 
# what is a list of recommended movies
# create a new list that (1) user has not watched (2) a friend has watched and 
# (3)the genre is the same as the user most watched genre

def get_new_rec_by_genre(user_data):

    recommended_movie_list_by_genre=[]
    user_most_watched_genre= get_most_watched_genre(user_data)
    
    friends_unique_movie_list = get_friends_unique_watched(user_data)
    for fmovie in friends_unique_movie_list:
        if fmovie['genre'] == user_most_watched_genre:
            recommended_movie_list_by_genre.append(fmovie)
    return recommended_movie_list_by_genre

def get_rec_from_favorites(user_data):
    user_recommended_movie_list=[]
    user_fav_movies_list=user_data['favorites']

    friends_list=user_data['friends']
    title_set=set()

    for friend in friends_list:
        for fmovie in friend['watched']:
            title_set.add(fmovie['title'])
                
    for movie in user_fav_movies_list:
        if movie['title'] not in title_set:
            user_recommended_movie_list.append(movie)

    return user_recommended_movie_list
    


