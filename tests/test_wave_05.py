import pytest
from viewing_party.party import *
from tests.test_constants import *

# Wave 5 / Test 1
# Recommend movie user has not watched that friends have watched
# if movie genre matches user's favorite genre
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

# Wave 5 / Test 2
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

# Wave 5 / Test 3
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
    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    assert len(recommendations) == 0

    # *********************************************************************
    # ****** Complete the Act and Assert Portions of theis tests **********
    # *********************************************************************

@pytest.mark.skip()
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

@pytest.mark.skip()
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

@pytest.mark.skip()
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
