from random import sample
def draw_letters():
    hand = sample(['A','B','C','D','E','F','G','H','I','J','K','L',\
                   'M','N','O','P','Q','R','S','T','U','V','W','X',\
                   'Y','Z'], counts = [9,2,2,4,12,2,3,2,9,1,1,4,2,6,\
                                       8,2,1,6,4,6,4,2,2,1,2,1], k = 10)
    return hand

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass