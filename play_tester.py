# import source code
from viewing_party.party import *

# import test data
from tests.test_constants import *

# import "pretty-print" library
import pprint
pp = pprint.PrettyPrinter(indent=4)

# play testing section
print("\n-----Wave 01 test data-----")
pp.pprint(HORROR_1)
pp.pprint(FANTASY_1)
pp.pprint(FANTASY_2)

print("\n-----Wave 02 user_data-----")
pp.pprint(clean_wave_2_data())


    

print("\n-----Wave 03 user_data-----")
pp.pprint(clean_wave_3_data())

user_data = {   'friends': [   {   'watched': [   {   'genre': 'Fantasy',
                                          'rating': 4.8,
                                          'title': 'The Lord of the Functions: '
                                                   'The Fellowship of the '
                                                   'Function'},
                                      {   'genre': 'Fantasy',
                                          'rating': 4.0,
                                          'title': 'The Lord of the Functions: '
                                                   'The Return of the Value'},
                                      {   'genre': 'Fantasy',
                                          'rating': 4.0,
                                          'title': 'The Programmer: An '
                                                   'Unexpected Stack Trace'},
                                      {   'genre': 'Horror',
                                          'rating': 3.5,
                                          'title': 'It Came from the Stack '
                                                   'Trace'}]},
                   {   'watched': [   {   'genre': 'Fantasy',
                                          'rating': 4.8,
                                          'title': 'The Lord of the Functions: '
                                                   'The Fellowship of the '
                                                   'Function'},
                                      {   'genre': 'Action',
                                          'rating': 2.2,
                                          'title': 'The JavaScript and the '
                                                   'React'},
                                      {   'genre': 'Intrigue',
                                          'rating': 2.0,
                                          'title': 'Recursion'},
                                      {   'genre': 'Intrigue',
                                          'rating': 3.0,
                                          'title': 'Zero Dark Python'}]}],
    'watched': [   {   'genre': 'Fantasy',
                       'rating': 4.8,
                       'title': 'The Lord of the Functions: The Fellowship of '
                                'the Function'},
                   {   'genre': 'Fantasy',
                       'rating': 4.0,
                       'title': 'The Lord of the Functions: The Two '
                                'Parameters'},
                   {   'genre': 'Fantasy',
                       'rating': 4.0,
                       'title': 'The Lord of the Functions: The Return of the '
                                'Value'},
                   {   'genre': 'Action',
                       'rating': 2.2,
                       'title': 'The JavaScript and the React'},
                   {'genre': 'Intrigue', 'rating': 2.0, 'title': 'Recursion'},
                   {   'genre': 'Intrigue',
                       'rating': 4.5,
                       'title': 'Instructor Student TA Manager'}]}


def get_unique_watched(user_data):
    user_watched = []
    friend_watched = [] 
    friend_no_repeat = []
    user_unique = []
    # create a list of all movies only user has seen

    for movie in user_data['watched']: 
        user_watched.append(movie['title'])
    print(f'USER WATCHED LIST {user_watched}')
    print(f'numer of friend movies is {len(friend_watched)}')
    for friend in user_data['friends']: 
        for a_movie in friend['watched']:
            friend_watched.append(a_movie['title'])
    print(f'FRIENDS WATCHED LIST : {friend_watched}')
    print(f'numer of friend movies is {len(friend_watched)}')

    for i in range(len(friend_watched)):
        if friend_watched[i] not in friend_watched[i + 1:]: 
            friend_no_repeat.append(friend_watched[i])
    print(len(friend_no_repeat))

    for i in range(len(user_watched)):
        if user_watched[i] not in friend_no_repeat[i + 1:]: 
            user_unique.append(user_watched[i])
    print('{user_unique=}')

    return(user_unique)


print(get_unique_watched(user_data))

Wave 04 user data
print("\n-----Wave 04 user_data-----")
pp.pprint(clean_wave_4_data())

# Wave 05 user data
#print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())
