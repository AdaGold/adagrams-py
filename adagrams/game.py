#from tests.test_wave_01 import LETTER_POOL
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

SCORE_DICT = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z'],
}

def draw_letters():
    # generate list containing all letters
    # in corresponding frequency
    all_letters = []
    for letter,frequency in LETTER_POOL.items():
        for i in range(frequency):
            all_letters.append(letter)
    
    hand = []
    for i in range(10):
        this_letter = random.choice(all_letters)
        hand.append(this_letter)
        all_letters.remove(this_letter)

    return hand

def uses_available_letters(word, letter_bank):
    word_bank = copy.deepcopy(letter_bank)
    caps_word = word.upper()
    for letter in caps_word:
        if letter not in word_bank:
            return False    
        else: 
            word_bank.remove(letter)    
    else:
        return True



def score_word(word):
    total = 0

    for letter in word.upper():
        for value, letter_list in SCORE_DICT.items():
            if letter in letter_list:
                total += value

    if len(word) >= 7:
        total += 8
    return total


def get_highest_dict(word_list):
    score_word_dict = {}
    
    for word in word_list:
        score = score_word(word)        
        if score not in score_word_dict.keys():
            score_word_dict[score] = []        
        score_word_dict[score].append(word)
    
    return score_word_dict


def get_highest_word_score(word_list):
    score_word_dict = get_highest_dict(word_list)
    
    max_score = max(score_word_dict.keys())
    max_words = score_word_dict[max_score]
    
    if len(max_words) == 1:
        winner_word = max_words[0]
        return winner_word, max_score
    
    else:
        num_letters = []
        for word in max_words:
            if len(word) == 10:
                winner_word = word
                return winner_word, max_score
            
            else:
                num_letters.append(len(word))
        
        min_length = min(num_letters)
        for word in max_words:
            if len(word) == min_length:
                winner_word = word
                return winner_word, max_score
