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
    #always make string 'word' be uppercase 
    word = word.upper()
    #generating a dictionary to keep track of how many each letter occurs in letter bank 
    letter_frequency = {}
    for letter in letter_bank:
        if letter in letter_frequency:
            letter_frequency[letter] += 1
        else:
            letter_frequency[letter] = 1    
    #compare each letter in word to the key in letter frequency dictionary 
    for elem in word: # loop through each letter in the word 
        if elem in letter_frequency.keys(): 
            if letter_frequency[elem] > 0:
                letter_frequency[elem] -= 1
            else: 
                return False 
        else:    
            return False  
    return True 


def score_word(word):
    letter_score = {
        "A" : 1,
        "E" : 1, 
        "I" : 1, 
        "O" : 1,
        "U" : 1, 
        "L" : 1, 
        "N" : 1, 
        "R" : 1,
        "S" : 1,
        "T" : 1,
        "D" : 2,
        "G" : 2,
        "B" : 3, 
        "C" : 3, 
        "M" : 3,
        "P" : 3,
        "F" : 4,
        "H" : 4,
        "V" : 4,
        "W" : 4,
        "Y" : 4,
        "K" : 5,
        "J" : 8, 
        "X" : 8,
        "Q" : 10, 
        "Z" : 10
    }
    total_score = 0 
    #turn every letter in the word to upper case 
    word = word.upper()
    # loop through each letter in the string "word"
    for letter in word: 
    # add the value of the letter to a variable called total_score
        total_score += letter_score[letter]
    # check if the word length is >=7 and if it is then add 8 to the total_score 
    if len(word) >= 7: 
        total_score += 8
    # return the score 
    return total_score 

def get_highest_word_score(word_list):
    highest_scoring_word = ""
    highest_score = 0
    for new_word in word_list:
        # find each score for word in the word_list 
        score_for_one_word = score_word(new_word)
        #decide on tie breaker first 
        if score_for_one_word == highest_score:
            # length of 10 letters trumps any word that is shorter 
            if len(new_word) == 10 and len(highest_scoring_word)!= 10:
                highest_scoring_word = new_word
            # having fewer letters is a tie breaker as long as the current stored word's length is not 10
            elif len(highest_scoring_word) > len(new_word) and len(highest_scoring_word) != 10:
               highest_scoring_word = new_word
        #Look for word with highest score 
        elif score_for_one_word > highest_score: 
            highest_score = score_for_one_word 
            highest_scoring_word = new_word        
                
    return highest_scoring_word, highest_score 
