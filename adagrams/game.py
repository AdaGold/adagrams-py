def draw_letters():
    pass

def uses_available_letters(word, letter_bank):
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    score_list = [(word, score_word(word)) for word in word_list]

    highest_scoring = []
    highest_scoring.append(score_list[0])

    for word in score_list[1:]:
        if word[1] == highest_scoring[0][1]:
            highest_scoring.append(word)
        elif word[1] > highest_scoring[0][1]:
            highest_scoring.clear()
            highest_scoring.append(word)

    if len(highest_scoring) == 1:
        return highest_scoring[0]

    highest_scoring.sort(key=lambda word: len(word[0]))

    if len(highest_scoring[-1][0]) == 10:
        highest_scoring.sort(key=lambda word: len(word[0]), reverse=True)

    return highest_scoring[0]