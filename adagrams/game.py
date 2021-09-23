
import copy

LETTER_VALUE = {
    'A': 1,
    'B': 3,
    'C': 3,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 2,
    'H': 4,
    'I': 1,
    'J': 8,
    'K': 5,
    'L': 1,
    'M': 3,
    'N': 1,
    'O': 1,
    'P': 3,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 1,
    'V': 4,
    'W': 4,
    'X': 8,
    'Y': 4,
    'Z': 10
}

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


def draw_letters():

    import random

    letters = []
    letter_pool_lst = []
    tup = ""

    for letter, numby in LETTER_POOL.items():
        tup = tuple(letter*numby)

        for t in tup:
            for x in t:
                letter_pool_lst.append(x)

    letters = random.sample(letter_pool_lst, 10)

    return letters


def uses_available_letters(word, letter_bank):
    compare_letters = copy.deepcopy(letter_bank)
    for ltr_word in word:
        if ltr_word not in compare_letters:
            return False
        else:
            compare_letters.remove(ltr_word)
    return True


def score_word(word):
    score_list = []
    bonus = 8
    if word == "":
        return 0
    else:
        for letter in word:
            score_list.append(LETTER_VALUE[letter.upper()])
            if len(score_list) >= 7:
                score = (sum(score_list) + bonus)
            else:
                score = sum(score_list)
        return score


def get_highest_word_score(word_list):
    word_score_dict = {}

    for word in word_list:
        word_score = score_word(word)
        word_score_dict[word] = word_score
    
    highest_score = 0
    highest_score_word = ""
    highest_score_dict = {}
    

    for word_name, word_score in word_score_dict.items():
        if word_score > highest_score:
            highest_score_word = word_name
            highest_score = word_score

        if word_score == highest_score and len(word_name) != len(highest_score_word):
            if len(word_name) == 10:
                highest_score_word = word_name
            elif len(word_name) < len(highest_score_word) and len(highest_score_word) != 10:
                highest_score_word = word_name
                highest_score = word_score
        
    highest_score_dict[highest_score_word] = highest_score

    highest_score_tup = highest_score_dict.items()

    return list(highest_score_tup)[0]
    
   
    
