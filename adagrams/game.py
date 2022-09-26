import random
import copy

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


# create a helper function to create the list
# def build_list():
#     new_list = []
#     for key, value in LETTER_POOL.items():
#         new_value = [key] * value
#         new_list += new_value  
#     print(new_list)

# build_list()

def draw_letters():
    # build a hand of 10 letters for user
    # return array of ten strings (each string should contain one letter)
    # return looks like ["A", "B", etc]
    # OPTION 1
    # make a copy of letter_pool 
    # multiply key by value and create new list
    # OPTION 2
    # make a deep copy of the letter_pool -----> I actually thik it can be a shallow copy since no items are mutable
    # create a new list from all the keys
    # Radomnly choose a letter from the new list
    # if the letter key exists , add to user list, subract one from value of that letter
    # when letter value == 0 - remove from list
    letters_for_user = []
    fresh_copy = copy.copy(LETTER_POOL)
    while len(letters_for_user) < 10:
        letter = random.choice(list(fresh_copy.keys()))
        value = fresh_copy[letter]
        if value > 0:
            letters_for_user.append(letter)
            fresh_copy[letter] -= 1
    return letters_for_user
    # print(letters_for_user)
    # print(fresh_copy)
    # print(LETTER_POOL)


def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.copy(letter_bank)
    word = word.upper()
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True

uses_available_letters('bEd', ['A', 'B', 'C', 'D', 'E', 'F'])

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass