import pytest

from adagrams.game import draw_letters

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def test_draw_letters_draws_ten():
    # Arrange/Act
    letters = draw_letters()

    # Assert
    assert len(letters) == 10

def test_draw_letters_is_list_of_letter_strings():
    # Arrange/Act
    letters = draw_letters()

    # Assert
    assert len(letters) == 10

    for elem in letters:
        assert type(elem) == str
        assert len(elem) == 1

def test_letter_not_selected_too_many_times():

    for i in range(1000):
        # Arrange/Act
        letters = draw_letters()

        letter_freq = {}
        for letter in letters:
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1
        
        # Assert
        for letter in letters:
            assert letter_freq[letter] <= LETTER_POOL[letter]

def test_draw_letters_returns_different_hands():
    # Arrange/Act
    hand1 = draw_letters()
    hand2 = draw_letters()
    hand3 = draw_letters()

    # Assert
    assert hand1 != hand2 or hand2 != hand3