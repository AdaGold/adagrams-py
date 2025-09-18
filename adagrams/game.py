from random import randint

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

SCORE_CHART = {
    1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
    2: ["D", "G"],
    3: ["B", "C", "M", "P"],
    4: ["F", "H", "V", "W", "Y"],
    5: ["K"],
    8: ["J","X"],
    10: ["Q","Z"]  
}

# SCORE_CHART_A = {
#     "AEIOULNRST": 1,
#     "DG": 2,
#     "BCMP": 3,
#     "FHVWY": 4,
#     "K": 5,
#     "JX": 8,
#     "QZ":10
# }

def get_draw_pool():
    draw_pool = []

    for letter, num in LETTER_POOL.items():
        while num > 0:
            draw_pool.append(letter)
            num -= 1
            # print(num)
    return draw_pool

# print(get_draw_pool())


def draw_letters():
    get_letter = []
    draw_pool = get_draw_pool()

    for _ in range(10):
        r = randint(0, len(draw_pool)-1)
        get_letter.append(draw_pool[r])
        draw_pool.pop(r)
        
    return get_letter



def uses_available_letters(word, letter_bank):
    pool = letter_bank[:] 
    # for i in letter_bank:
    #     pool.append(i)

    for cha in word.upper():
        # cha = chara.capitalize()
        if cha in pool:
            pool.remove(cha)
        else:
            return False
    
    return True

def score_word(word):
    the_score = 0
    for cha in word.upper():
        for score, k in SCORE_CHART.items():
            if cha in k:
                the_score += score
    
    if 7 <= len(word) <= 10:
        the_score += 8

    return the_score


def get_highest_word_score(word_list):
    pass