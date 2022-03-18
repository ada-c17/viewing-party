import pytest
from viewing_party.party import *
from tests.test_constants import *

# @pytest.mark.skip()
def test_new_genre_rec():
    # Arrange
    sonyas_data = clean_wave_5_data()

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    for rec in recommendations:
        assert rec not in sonyas_data["watched"]
    assert len(recommendations) == 1
    assert FANTASY_4b in recommendations
    assert sonyas_data == clean_wave_5_data()

# @pytest.mark.skip()
def test_new_genre_rec_from_empty_watched():
    # Arrange
    sonyas_data = {
        "watched": [],
        "friends": [
            {
                "watched": [INTRIGUE_1b]
            },
            {
                "watched": [INTRIGUE_2b,HORROR_1b]
            }
        ]
    }

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    assert len(recommendations) == 0

# @pytest.mark.skip()
def test_new_genre_rec_from_empty_friends():
    # Arrange
    sonyas_data = {
        "watched": [INTRIGUE_1b],
        "friends": [
            {
                "watched": []
            },
            {
                "watched": []
            }
        ]
    }
    
    recommendations = get_new_rec_by_genre(sonyas_data)
    assert recommendations == []

    # *********************************************************************
    # ****** Complete the Act and Assert Portions of theis tests **********
    # *********************************************************************

# @pytest.mark.skip()
def test_unique_rec_from_favorites():
    # Arrange
    sonyas_data = clean_wave_5_data()

    # Act
    recommendations = get_rec_from_favorites(sonyas_data)

    # Assert
    assert len(recommendations) == 2
    assert FANTASY_2b in recommendations
    assert INTRIGUE_2b in recommendations
    assert sonyas_data == clean_wave_5_data()

# @pytest.mark.skip()
def test_unique_from_empty_favorites():
    # Arrange
    sonyas_data = {
        "watched": [],
        "friends": [
            {
                "watched": [INTRIGUE_1b]
            },
            {
                "watched": [INTRIGUE_2b,HORROR_1b]
            }
        ]
    }

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    assert len(recommendations) == 0

# @pytest.mark.skip()
def test_new_rec_from_empty_friends():
    # Arrange              
    sonyas_data = {
        "watched": [INTRIGUE_1b],
        "friends": [
            {
                "watched": []
            },
            {
                "watched": []
            }
        ]
    }

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    assert len(recommendations) == 0


#*************************************************************#
#Added another test here. The "test_new_rec_from_empty_friends"
#Tested if BOTH of the friends lists were empty, this just makes
#Sure it runs if only ONE of the friends lists is empty

def test_new_rec_from_one_empty_friend():
    # Arrange              
    sonyas_data = full_but_one_watched

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    assert len(recommendations) == 1


full_but_one_watched = {
	"subscriptions" : ["netflix", "hulu"],
	"favorites" : [
		FANTASY_1b, 
		FANTASY_2b, 
        INTRIGUE_1b,
		INTRIGUE_2b,
        ACTION_1b
		],
    "watched": [
        FANTASY_1b, 
        FANTASY_2b, 
        FANTASY_3b, 
        ACTION_1b, 
        INTRIGUE_1b, 
        INTRIGUE_2b
        ],  
    "friends":  [
        {
            "watched": [
            ]
        },
        {
            "watched": [
                FANTASY_1b,
                ACTION_3b,
                INTRIGUE_1b,
                INTRIGUE_3b,
            ]
        }  
    ]
}