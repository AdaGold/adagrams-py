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

SCORE_CHART = {
        1: ["A", "E", "I", "O", "U", "N", "R", "S", "T"],
        2: ["D", "G"],
        3: ["B", "C", "M", "P"],
        4: ["F", "H", "V", "W", "Y"],
        5: ["K"],
        8: ["J", "X"],
        10: ["Q", "Z"]
    }



def draw_letters():
    letters_for_user = []
    fresh_copy = copy.copy(LETTER_POOL)
    while len(letters_for_user) < 10:
        letter = random.choice(list(fresh_copy.keys()))
        value = fresh_copy[letter]
        if value > 0:
            letters_for_user.append(letter)
            fresh_copy[letter] -= 1
    return letters_for_user


def uses_available_letters(word, letter_bank):
    letter_bank_copy = copy.copy(letter_bank)
    word = word.upper()
    for letter in word:
        if letter in letter_bank_copy:
            letter_bank_copy.remove(letter)
        else:
            return False
    return True



def score_word(word):
    score = 0
    word = word.upper()
    for letter in word: 
        for key, value in SCORE_CHART.items():
            if letter in value:
                score += key
    if len(word) in range(7, 11):
        score += 8
    return score

def get_highest_word_score(word_list):

    max_score_word_1 = max(word_list, key = score_word)
    max_score = score_word(max_score_word_1)
    highest_score_words = [word for word in word_list if score_word(word) == max_score]
 
    if len(highest_score_words) == 1:
        return max_score_word_1, max_score

    for word in highest_score_words:
        if len(word) == 10:
            return word, max_score

    min_length_word = min(highest_score_words, key = len)
    return min_length_word, max_score


