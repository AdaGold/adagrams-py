import random 

LETTER_KEY = {
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

# Wave 1 
def draw_letters():
    letter_pool = []
    for letter, frequency in LETTER_KEY.items():
        for number in range(frequency):
            letter_pool.append(letter)
    
    user_hand = []
    while len(user_hand) < 10:
        letter_to_add = random.choice(letter_pool)
        if user_hand.count(letter_to_add) < LETTER_KEY[letter_to_add]:
            user_hand.append(letter_to_add)
    
    return user_hand 

# Wave 2 
# Approach 
# iterate over each letter in the word...
#   count the # of times this letter occurs in the word
#   count the # of times this letter occurs in the letter_bank (the user's 
#   hand) 
#   -if the the # of times a letter occurs in the word is HIGHER than the number
#      of times it occurs in the user's available letter bank...
#      -return False (because that'd mean it's not a valid word)

#  If in the end, false was never returned (which means every letter was 
#  looked at and determined to exist in the user's letter bank AND not occur 
#  too many times), return True. 

def uses_available_letters(word, letter_bank):
    for letter in word:
        if word.count(letter) > letter_bank.count(letter):
            return False 
    return True

# Wave 3 
def score_word(word):
    pass 

# Wave 4 
def get_highest_word_score(word_list):
    pass