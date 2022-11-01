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

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass