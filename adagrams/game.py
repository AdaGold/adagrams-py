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

print(draw_letters())


# def uses_available_letters(word, letter_bank):
#     def helper_function():

# def score_word(word):
#     pass

# def get_highest_word_score(word_list):
#     pass