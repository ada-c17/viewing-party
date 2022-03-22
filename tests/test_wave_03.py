import pytest
from viewing_party.party import *
from tests.test_constants import *

# @pytest.mark.skip()
def test_my_unique_movies():
    # Arrange
    amandas_data = clean_wave_3_data()

    # Act
    amandas_unique_movies = get_unique_watched(amandas_data)

    # Arrange
    assert len(amandas_unique_movies) == 2
    assert FANTASY_2 in amandas_unique_movies
    assert INTRIGUE_2 in amandas_unique_movies
    assert amandas_data == clean_wave_3_data()

# @pytest.mark.skip()
def test_my_not_unique_movies():
    # Arrange
    amandas_data = clean_wave_3_data()
    amandas_data["watched"] = []

    # Act
    amandas_unique_movies = get_unique_watched(amandas_data)

    # Arrange
    assert len(amandas_unique_movies) == 0

# @pytest.mark.skip()
def test_friends_unique_movies():
    # Arrange
    amandas_data = clean_wave_3_data()

    # Act
    friends_unique_movies = get_friends_unique_watched(amandas_data)

    # Arrange
    assert len(friends_unique_movies) == 3
    assert INTRIGUE_3 in friends_unique_movies
    assert HORROR_1 in friends_unique_movies
    assert FANTASY_4 in friends_unique_movies
    assert amandas_data == clean_wave_3_data()

# @pytest.mark.skip()
def test_friends_unique_movies_not_duplicated():
    # Arrange
    amandas_data = clean_wave_3_data()
    amandas_data["friends"][0]["watched"].append(INTRIGUE_3)

    # Act
    friends_unique_movies = get_friends_unique_watched(amandas_data)

    # Arrange
    assert len(friends_unique_movies) == 3

    # *************************************************************************************************
    # ****** Add assertions here to test that the correct movies are in friends_unique_movies **********
    assert INTRIGUE_3 in friends_unique_movies
    # **************************************************************************************************

# @pytest.mark.skip()
def test_friends_not_unique_movies():
    # Arrange
    amandas_data = {
        "watched": [
            HORROR_1,
            FANTASY_1,
            INTRIGUE_1
        ],
        "friends": [
            {
                "watched": [
                    HORROR_1,
                    FANTASY_1,
                ]
            },
            {
                "watched": []
            }
        ]
    }

    # Act
    friends_unique_movies = get_friends_unique_watched(amandas_data)

    # Arrange
    assert len(friends_unique_movies) == 0


# -------------------  Test helper functions -----------------------

# Test the funtion ele_in_a_not_b
def test_list_a_unique_elements():
    #Arrange
    list_a = [1, 2, 3, 4, 5]
    list_b = [3, 4, 5]
    
    #Act
    output = ele_in_a_not_b(list_a, list_b)

    #Assert
    assert output == [1, 2]

def test_list_a_unique_elements_not_duplicated():
    #Arrange
    list_a = ['apple', 'orange', 'orange', 'orange', 'banana', 'cherry']
    list_b = ['apple', 'cherry']
    
    #Act
    output = ele_in_a_not_b(list_a, list_b)

    #Assert
    assert output == ['orange', 'banana']

def test_empty_list_a():
    #Arrange
    list_a = []
    list_b = ['apple', 'cherry']
    
    #Act
    output = ele_in_a_not_b(list_a, list_b)

    #Assert
    assert output == []

# Test the function get_friends_watched_movies
def test_friends_watched_movies():
    #Arrange
    amandas_data = clean_wave_3_data()

    #Act
    amanda_friends_watched = get_friends_watched_movies(amandas_data)

    #Assert
    assert len(amanda_friends_watched) == 8 