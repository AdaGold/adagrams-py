import random

# Dictionary of the letters with their quantities
LETTER_POOL = {
    "A": 9,
    "B": 2,
    "C": 2,
    "D": 4,
    "E": 12,
    "F": 2,
    "G": 3,
    "H": 2,
    "I": 9,
    "J": 1,
    "K": 1,
    "L": 4,
    "M": 2,
    "N": 6,
    "O": 8,
    "P": 2,
    "Q": 1,
    "R": 6,
    "S": 4,
    "T": 6,
    "U": 4,
    "V": 2,
    "W": 2,
    "X": 1,
    "Y": 2,
    "Z": 1,
}

# Dictionary assigning point values to the letters
LETTERS_VALUE = {
    "A": 1,
    "B": 3,
    "C": 3,
    "D": 2,
    "E": 1,
    "F": 4,
    "G": 2,
    "H": 4,
    "I": 1,
    "J": 8,
    "K": 5,
    "L": 1,
    "M": 3,
    "N": 1,
    "O": 1,
    "P": 3,
    "Q": 10,
    "R": 1,
    "S": 1,
    "T": 1,
    "U": 1,
    "V": 4,
    "W": 4,
    "X": 8,
    "Y": 4,
    "Z": 10,
}


def draw_letters():

    # Draw 10 letters randomly, considering the quantity limits
    letter_list = list(LETTER_POOL.keys())
    tiles = {}  # Dictionary with letter and count to avoid nested loops
    letter_bank = [] 

    while len(letter_bank) < 10:
        random_number = random.randint(0, len(letter_list) - 1)
        random_letter = letter_list[random_number]

        if random_letter in tiles:
            if tiles[random_letter] >= LETTER_POOL[random_letter]:
                continue
            tiles[random_letter] += 1
        else:
            tiles[random_letter] = 1
            
        letter_bank.append(random_letter)

    return letter_bank


# Count occurrences of a letter in an iterable
def count_items(item, iterable):
    count = 0
    for x in iterable:
        if x == item:
            count += 1
    return count


def uses_available_letters(word, letter_bank):
    capital_word = word.upper()

    for letter in set(capital_word):
        if letter not in letter_bank or count_items(letter, capital_word) > count_items(
            letter, letter_bank
        ):
            return False
    return True


def score_word(word):
    # Calculate score
    score = 0
    for letter in word.upper():
        score += LETTERS_VALUE[letter]

    # Add bonus points for words of length 7-10
    if len(word) >= 7 and len(word) <= 10:
        score += 8
    return score


# Function to find the maximum value in a list of numbers
def calculate_max(iterable):
    max = 0
    for value in iterable:
        if value > max:
            max = value
    return max


# Function to find the minimum length of words in a list
def calculate_min_length(list_of_words):
    if not list_of_words:
        return None

    min_length = len(list_of_words[0])
    for word in list_of_words:
        if len(word) < min_length:
            min_length = len(word)
    return min_length


def get_highest_word_score(word_list):
    # Calculate scores of each word
    word_score = {}
    for word in word_list:
        score = score_word(word)
        word_score[word] = score

    # Calculate max score
    max_score = calculate_max(word_score.values())

    # Find all candidate words with max scores
    candidates = []
    for word, score in word_score.items():
        if score == max_score:
            candidates.append(word)

    # Find minimum length in candidates
    min_length = calculate_min_length(candidates)

    # Determine a winner considering rules
    current_winner = ""
    for word in candidates:
        if len(word) == 10:
            current_winner = word
            break
        if len(word) == min_length and not current_winner:
            current_winner = word

    return current_winner, word_score[current_winner]
