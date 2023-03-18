import random
def draw_letters():
    list_of_letters = []
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
   
    while len(list_of_letters) < 10:    
        letter_chosen = random.choice(list(LETTER_POOL))
        if LETTER_POOL[letter_chosen] > 0:
            list_of_letters.append(letter_chosen)
            LETTER_POOL[letter_chosen] -= 1

    return list_of_letters
        
def uses_available_letters(word, letter_bank):
    ## word is a string 
    ## letter bank is list of letters 
    #compare the word to letter bank 
    for elem in word: 
        if elem not in letter_bank:
            return False  
    return True 


def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass