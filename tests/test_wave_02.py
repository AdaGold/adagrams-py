import pytest

from adagrams.game import uses_available_letters


def test_uses_available_letters_true_word_in_letter_bank():
    # Arrange
    letters = ["D", "O", "G", "X", "X", "X", "X", "X", "X", "X"]
    word = "DOG"
    
    # Act
    is_valid = uses_available_letters(word, letters)

    # Assert
    assert is_valid == True


def test_uses_available_letters_false_word_in_letter_bank():
    # Arrange
    letters = ["D", "O", "X", "X", "X", "X", "X", "X", "X", "X"]
    word = "DOG"
    
    # Act
    is_valid = uses_available_letters(word, letters)

    # Assert
    assert is_valid == False


def test_uses_available_letters_false_word_overuses_letter():
    # Arrange
    letters = ["A", "X", "X", "X", "X", "X", "X", "X", "X", "X"]
    word = "AAA"
    
    # Act
    is_valid = uses_available_letters(word, letters)

    # Assert
    assert is_valid == False


def test_uses_available_letters_does_not_change_letter_bank():
    # Arrange
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    letters_copy = letters[:]
    word = "ABCD"

    # ACT
    is_valid = uses_available_letters(word, letters)

    # Assert
    assert is_valid == True
    assert letters == letters_copy, "pass this difficult test"


def test_uses_available_letters_ignores_case():
    # Arrange
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

    # Act/Assert
    assert uses_available_letters("bEd", letters), "Test1"
    assert uses_available_letters("fad", letters),"Test2"
    assert uses_available_letters("a", letters), "Test3"
    assert not uses_available_letters("aA", letters), "Test4"

