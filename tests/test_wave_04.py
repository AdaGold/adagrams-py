import pytest

from adagrams.game import score_word, get_highest_word_score

def test_get_highest_word_score_accurate():
    # Arrange
    words = ["X", "XX", "XXX", "XXXX"]

    # Act
    best_word = get_highest_word_score(words)
    # NOTE: best_word can be a tuple or a list

    # Assert
    assert best_word[0] == "XXXX"
    assert best_word[1] == 32

def test_get_highest_word_score_accurate_unsorted_list():
    # Arrange
    words = ["XXX", "XXXX", "XX", "X"]

    # Act
    best_word = get_highest_word_score(words)

    # Assert
    assert best_word[0] == "XXXX"
    assert best_word[1] == 32

def test_get_highest_word_tie_prefers_shorter_word():
    # Arrange
    words = ["MMMM", "WWW"]

    # Act
    best_word = get_highest_word_score(words)

    # Assert
    assert score_word(words[0]) == 12
    assert score_word(words[1]) == 12
    assert best_word[0] == "WWW"
    assert best_word[1] == 12

def test_get_highest_word_tie_prefers_shorter_word_unsorted_list():
    # Arrange
    words = ["WWW", "MMMM"]

    # Act
    best_word = get_highest_word_score(words)

    # Assert
    assert score_word(words[0]) == 12
    assert score_word(words[1]) == 12
    assert best_word[0] == "WWW"
    assert best_word[1] == 12

def test_get_highest_word_tie_prefers_ten_letters():
    # Arrange
    words = ["AAAAAAAAAA", "BBBBBB"]

    # Act
    best_word = get_highest_word_score(words)

    # Assert
    assert best_word[0] == "AAAAAAAAAA"
    assert best_word[1] == 18

def test_get_highest_word_tie_prefers_ten_letters_unsorted_list():
    # Arrange
    words = ["BBBBBB", "AAAAAAAAAA"]

    # Act
    best_word = get_highest_word_score(words)

    # Assert
    assert best_word[0] == "AAAAAAAAAA"
    assert best_word[1] == 18

def test_get_highest_word_tie_same_length_prefers_first():
    # Arrange
    words = ["AAAAAAAAAA", "EEEEEEEEEE"]

    # Act
    best_word = get_highest_word_score(words)

    # Assert
    assert score_word(words[0]) == 18
    assert score_word(words[1]) == 18
    assert best_word[0] == words[0]
    assert best_word[1] == 18

def test_get_highest_word_many_ties_pick_first_ten_letters():
    # Arrange
    words = ["JQ", "FHQ", "AAAAAAAAAA", "BBBBBB", "TTTTTTTTTT"]

    # Act
    best_word = get_highest_word_score(words)

    # Assert
    assert best_word[0] == "AAAAAAAAAA"
    assert best_word[1] == 18

def test_get_highest_word_many_ties_pick_shortest():
    # Arrange
    words = ["BBBBBB", "AAAAAAAAD", "JQ", "KFHK"]

    # Act
    best_word = get_highest_word_score(words)

    # Assert
    assert best_word[0] == "JQ"
    assert best_word[1] == 18

def test_get_highest_word_does_not_return_early_after_first_tiebreaker():
    # Arrange
    words = ["WWW", "MMMM", "BBBBBB", "AAAAAAAAD", "JQ", "KFHK"]

    # Act
    best_word = get_highest_word_score(words)

    # Assert
    assert best_word[0] == "JQ"
    assert best_word[1] == 18
