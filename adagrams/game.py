
# |Letter                        | Value|
# |:----------------------------:|:----:|
# |A, E, I, O, U, L, N, R, S, T  |   1  |
# |D, G                          |   2  |
# |B, C, M, P                    |   3  |
# |F, H, V, W, Y                 |   4  |
# |K                             |   5  |
# |J, X                          |   8  |
# |Q, Z                          |   10 |

LETTER_POOL = {
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


def draw_letters():
    pass


def uses_available_letters(word, letter_bank):
    pass


def score_word(word):
    score_list = []
    bonus = 8
    if word == "":
        return 0
    else:
        for letter in word:
            print(letter)
            score_list.append(LETTER_POOL[letter.upper()])
            if len(score_list) >= 7:
                score = (sum(score_list) + bonus)
            else:
                score = sum(score_list)
        print(bonus)
        print(score_list)
        print(score)
        return score


def get_highest_word_score(word_list):
    pass
