user_data = {
    "watchlist": [
        {
        "title": "Star Wars",
        "genre": "Fiction",
        "rating": 4
        },
        {
        "title": "TDD",
        "genre": "Adventurous",
        "rating": 3
        }
        ],
    "watched": [
        {
        "title": "Free Guy",
        "genre": "Fiction",
        "rating": 4
        }
    ]
}

# prob: take a movie "Starwars" out of watchlist, 
# move it to watched:
print(user_data["watchlist"])
print(user_data("watched"))

movie_to_move = user_data["watchlist"][0] 
user_data["watched"].append(movie_to_move)

print(user_data["watchlist"])
print(user_data("watched"))