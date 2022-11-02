import random

POOL_RULES = {"A":9,
              "B":2,
              "C":2,
              "D":4,
              "E":12,
              "F":2,
              "G":3,
              "H":2,
              "I":9,
              "J":1,
              "K":1,
              "L":4,
              "M":2,
              "N":6,
              "O":8,
              "P":2,
              "Q":1,
              "R":6,
              "S":4,
              "T":6,
              "U":4,
              "V":2,
              "W":2,
              "X":1,
              "Y":2,
              "Z":1}

SIZE_OF_DRAW = 10

def gen_pool_letters(pool_dict):
    my_pool = list()
    for letter,frecuency in pool_dict.items():
        for i in range(0,frecuency):
            my_pool.append(letter)

    return my_pool

#def init_game():
 #   POOL = gen_pool_letters(POOL_RULES)

def draw_letters():
    draw = list()
    my_ran_pool = gen_pool_letters(POOL_RULES)
    
    #generate random
    random.seed()
    for i in range(0,SIZE_OF_DRAW):
        ran_num = random.randint(0,len(my_ran_pool)-1)
        draw.append(my_ran_pool[ran_num])
        my_ran_pool.pop(ran_num)

    return draw

#creates a dictionary which keys are the elements on the letters array 
#and the value is their frecuency
def create_dic_repeatead_letters(letters):
    letters_dict = dict()

    for letter in letters:
        if letter in letters_dict.keys():
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1

    return letters_dict

def uses_available_letters(word, letter_bank):
    #Validate input
    if word == "" or letter_bank is None:
        return False

    #Create a dictionary with the number of each letter of the letter bank
    letter_bank_dict = create_dic_repeatead_letters(letter_bank)

    #Compare each letter of word with the dictionary and their frecuency
    for letter in word:
        up_letter = letter.upper()
        if up_letter not in letter_bank_dict.keys():
            return False
        if letter_bank_dict[up_letter]==0:
            return False  #The letter has been used more times than allowed
        else:
            letter_bank_dict[up_letter]+=-1

    return True

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass