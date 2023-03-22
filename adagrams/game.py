import random
import copy

LETTER_POOL = [
	['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
	['B', 'B'], 
	['C', 'C'], 
	['D','D','D','D'],
	['E','E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E'], 
	['F', 'F'], 
	['G', 'G', 'G'], 
	['H', 'H'], 
	['I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I'], 
	['J'], 
	['K'], 
	['L', 'L', 'L', 'L'], 
	['M', 'M'],
	['N', 'N', 'N', 'N', 'N', 'N'],
	['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], 
	['P', 'P'], 
	['Q'], 
	['R', 'R', 'R', 'R', 'R', 'R'], 
	['S', 'S', 'S', 'S'], 
	['T', 'T', 'T', 'T', 'T', 'T'], 
	['U', 'U', 'U', 'U'], 
	['V', 'V'], 
	['W', 'W'], 
	['X'], 
	['Y', 'Y'],
	['Z']
]


def get_one_list_of_letters():

    total_letters_list = []
    for elem in LETTER_POOL:
        for char in elem:
            total_letters_list.append(char)
    return total_letters_list

def draw_letters():

    total_letters_list = get_one_list_of_letters()

    hand = []
    i = 0
    while i < 10:
        random_letter = total_letters_list[random.randint(0, 97)]
        if hand.count(random_letter) < total_letters_list.count(random_letter):
            hand.append(random_letter)
        else:
            continue
        i += 1

    return hand

    # new_list = []
    # for elem in LETTER_POOL:
    #     for char in elem:
    #         new_list.append(char)
    # total_letters_list = get_one_total_list_of_letters()
    # hand = []
    # i = 0
    

def uses_available_letters(word, letter_bank):
    #made copy of list to not change original copy
    letter_bank_copy = copy.deepcopy(letter_bank)
# iterating thruogh letters in word
    for letter in word.upper():

        if letter in letter_bank_copy:
            #remove letter from letter bank so it can't be reused
            letter_bank_copy.remove(letter)
        else:
           return  False

    return True 

    # return all(letter in letter_bank for letter in word))


def score_word(word):

    letter_values = {
        ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
        ('D', 'G'): 2,
        ('B', 'C', 'M', 'P'): 3,
        ('F', 'H', 'V', 'W', 'Y'): 4,
        ('K'): 5,
        ('J', 'X'): 8,
        ('Q', 'Z'): 10
    }

    score = 0 

    for letter in word.upper():
        for key in letter_values:
            if letter in key: 
                score += letter_values[key]
    
    if len(word) > 6:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    pass