import random
import copy

 # Two Dimensional Array

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

# helper function to create one big list of strings

def get_one_list_of_letters():

    total_letters_list = []
    for elem in LETTER_POOL:
        for char in elem:
            total_letters_list.append(char)
    return total_letters_list

def draw_letters():

    total_letters_list = get_one_list_of_letters()

    # start with an empty hand and initialize counter at 0
    hand = []
    i = 0
    while i < 10:
        # randomize letter choice
        random_letter = total_letters_list[random.randint(0, 97)]
        # ensure that random letter choice in hand is never greater than the max amount in the letter pool
        # if less than the max amount then append to empty list which is our hand of letters
        if hand.count(random_letter) < total_letters_list.count(random_letter):
            hand.append(random_letter)
        else:
            # use continue to end this iteration and immediately start next iteration
            continue
        i += 1

    return hand    

def uses_available_letters(word, letter_bank):

    # made copy of list as to not modify the original copy
    letter_bank_copy = copy.deepcopy(letter_bank)

    # iterate through each letter in the word and make letters all uppercase
    for letter in word.upper():

        if letter in letter_bank_copy:
            # remove letter from letter bank so it can't be reused
            letter_bank_copy.remove(letter)
        else:
           return  False

    return True 

def score_word(word):
    # create dictionary to store key value pairs of letters and their corresponding value
    letter_values = {
        ('A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'): 1,
        ('D', 'G'): 2,
        ('B', 'C', 'M', 'P'): 3,
        ('F', 'H', 'V', 'W', 'Y'): 4,
        ('K'): 5,
        ('J', 'X'): 8,
        ('Q', 'Z'): 10
    }
    # initialize score at zero
    score = 0 
    # iterate through each letter of the word(uppercase)
    for letter in word.upper():
        # iterate through keys in dictionary to gain access to their values
        for key in letter_values:
            if letter in key: 
                # add score as we iterate through 
                score += letter_values[key]
    # if a word is between 7 and 10 letters, add 8 bonus points to the total
    if len(word) > 6:
        score += 8
    
    return score

def get_highest_word_score(word_list):
    # initialize a score keeper and empty list for the winning word(s)
    highest_score =  0
    winning_list = []
    # iterate through each word in the word list
    for word in word_list:
        # pull in score value from score_word function
        score = score_word(word)
        # reassign highest_score if the current score is greater than it
        if score > highest_score:
            highest_score = score
            # reassign winning_list when it's corresponding score is the highest
            winning_list = [word]
        # score is a tie to current high score, add word to winning_list
        elif score == highest_score:
            winning_list.append(word)

    # initialize letter_count at 10 letters and winning_word as empty string
    letter_count = 10
    winning_word = ''
    # if only one word in winning list, return the word and highest score
    if len(winning_list) == 1:
        return winning_list[0], highest_score
    else:
        for word in winning_list:
            # if the word has 10 letters exactly, return word and highest score
            if len(word) == 10:
                return word, highest_score
            else:
                # if the word length is less than the letter count, we want to reassign letter count with word length and winning word with the actual winning word
                if len(word) < letter_count:
                    letter_count = len(word)
                    winning_word = word
    
    return winning_word, highest_score