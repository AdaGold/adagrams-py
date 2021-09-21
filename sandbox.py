## WAVE 1

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
    letters=[]
    letter_pool_lst=[]
    tup=""

    for letter, numby in LETTER_POOL.items():
        tup= tuple(letter*numby)

        for t in tup:
            for x in t:
                letter_pool_lst.append(x)

    letters = random.sample(letter_pool_lst, 10)

    print(letters)
    return letters

    #draws_ten
    #is_list_of_letter_strings
    #letter_not_selected_too_many_times
    pass


## WAVE 2

def uses_available_letters(word, letters):
    # true_word_in_letter_bank
    # false_word_in_letter_bank
    # false_word_overuses_letter
    # does_not_change_letter_bank
    pass


## WAVE 3

def test_score(score_word):
    score_list = []
    score = sum(score_list)
    if score_word == "":
        return 0
    else:
        for letter in score_word:
            score_list.append(LETTER_POOL[letter.upper()])
        #if len(score_word) >= 7:
            #
       
    # word_accurate
    # word_accurate_ignores_case
    # zero_for_empty
    # extra_points_for_seven_or_longer
           
   


## WAVE 4

def get_highest_word_score(words):
    # accurate
    # accurate_unsorted_list
    # tie_prefers_shorter_word
    # tie_prefers_shorter_word_unsorted_list
    # tie_prefers_ten_letters
    # tie_same_length_prefers_first
    pass



