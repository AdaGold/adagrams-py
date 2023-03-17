import random
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
    
    # create a new pool of letters (every letter is there as many times as the value of the dic indicates)
    letters = []
    for k, v in LETTER_POOL.items():
        letter_times = k * v
        letters.append(letter_times)
    big_string = ''.join(letters)
    
    # select letters (random)
    selected_letters = []
    
    for i in range(0,10):
        letter_for_list = random.choice(big_string)
        selected_letters.append(letter_for_list)
        index = big_string.index(letter_for_list)
        big_string = big_string[:index]+ big_string[index+1:]
    
    return selected_letters

# hand = ['Y', 'V', 'B', 'U', 'A', 'P', 'E', 'R', 'K', 'R']


def uses_available_letters(word, letter_bank):
    # hay que contar cuantas veces la usa también (analizar el letter bank)
    # tiene que ver que no sea igual que el letter bank
    # hay que pasar el input a mayusculas 

    # correct input
    new = word.upper()
    # check for new letters in bank and check doesnt copy letter bank
    for letter in new:
        if letter not in letter_bank:
            return False
    count_letters_in_bank = {}
    for letter in letter_bank:
        if letter not in count_letters_in_bank:
            count_letters_in_bank[letter] = 1
        else:
            count_letters_in_bank[letter] += 1
    count_letters_in_new = {}
    for letter in new:
        if letter not in count_letters_in_new:
            count_letters_in_new[letter] = 1
        else:
            count_letters_in_new[letter] += 1
    for k, v in count_letters_in_new.items():
        for key, value in count_letters_in_bank.items():
            if k == key:
                if v <= value:

                    return True
                else:
                    return False
    



# def score_word(word):
#     pass

# def get_highest_word_score(word_list):
#     pass