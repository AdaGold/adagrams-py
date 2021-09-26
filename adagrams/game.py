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

def uses_available_letters(word, letter_bank):
    for letter in word: 
        if word.count(letter) > letter_bank.count(letter):
            return False 
    return True

def score_word(word): 
    word = word.upper() 
    score = 0
    for letter in word:
        if letter in ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T']:
            score += 1 
        elif letter in ['D', 'G']:
            score += 2
        elif letter in ['B', 'C', 'M', 'P']:
            score += 3
        elif letter in ['F', 'H', 'V', 'W', 'Y']:
            score += 4
        elif letter in ['K']:
            score += 5
        elif letter in ['J', 'X']:
            score += 8
        elif letter in ['Q', 'Z']:
            score += 10 
    
    if len(word) >= 7 and len(word) <= 10:
        score += 8 
    
    return score

def get_highest_word_score(word_list):
    max_tuple = ("placeholder", 0)

    for word in word_list: 
        word_tuple = (word, score_word(word)) 
        if word_tuple[1] > max_tuple[1]: 
            max_tuple = word_tuple
        elif word_tuple[1] == max_tuple[1]: 
            if len(max_tuple[0]) == 10:
                pass
            elif len(word_tuple[0]) == 10:
                max_tuple = word_tuple
            elif len(word_tuple[0]) < len(max_tuple[0]):
                max_tuple = word_tuple

    return max_tuple 