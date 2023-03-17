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


def uses_available_letters(word, letter_bank):

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
                    print(f"value {value}")
                    return True
                else:
                    return False
    

def score_word(word):
    score_values = {
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
    word_upper = word.upper()
    lenght_of_word = len(word)
    total_score = 0
    for letter in word_upper:
        if letter in score_values:
            total_score += score_values[letter]
    if lenght_of_word > 6:
        total_score += 8
    
    return total_score

# def get_highest_word_score(word_list):
#     pass