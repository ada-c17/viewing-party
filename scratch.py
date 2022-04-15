from viewing_party.movie import Movie
from viewing_party.user import User

saw = Movie("saw", "horror", "4.3", "Netflix")

print(saw.title)

jaws = Movie("jaws", "horror", "3.3", "HBO")

lindsey = User()

taiki = User()



lindsey.add_to_watchlist(saw)

print(lindsey.watchlist[0].genre)

taiki.add_to_watchlist(jaws)

lindsey.watch_movie("saw")

print(lindsey.watched[0].title)

lindsey.friends.append(taiki)

unique = lindsey.get_unique_watched()

print(unique[0].title)

t_unique = lindsey.get_friends_unique_watched()

print(t_unique)
