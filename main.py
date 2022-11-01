from imp import init_builtin
import sys
from adagrams.ui_helper import *
from adagrams.game import draw_letters, uses_available_letters, score_word, get_highest_word_score

def wave_1_run_game():
    display_welcome_message()
    game_continue = True
    while game_continue:
        print("Let's draw 10 letters from the letter pool...")
        letter_bank = draw_letters()
        display_drawn_letters(letter_bank)
    
        display_retry_instructions()
        continue_input = input()
        game_continue = continue_input == "y"
    
    display_goodbye_message()

def wave_2_run_game():
    display_welcome_message()
    game_continue = True
    while game_continue:
        print("Let's draw 10 letters from the letter pool...")
        letter_bank = draw_letters()
        display_drawn_letters(letter_bank)
        display_game_instructions()
        user_input_word = input()

        while( not uses_available_letters(user_input_word, letter_bank)):
            display_needs_valid_input_message()
            user_input_word = input()

        display_retry_instructions()
        continue_input = input()
        game_continue = continue_input == "y"
   
    display_goodbye_message()

def wave_3_run_game():
    display_welcome_message()
    game_continue = True
    while game_continue:
        print("Let's draw 10 letters from the letter pool...")
        letter_bank = draw_letters()
        display_drawn_letters(letter_bank)
        display_game_instructions()
        user_input_word = input()

        while( not uses_available_letters(user_input_word, letter_bank)):
            display_needs_valid_input_message()
            user_input_word = input()
        
        score = score_word(user_input_word)
        display_score(score)

        display_retry_instructions()
        continue_input = input()
        game_continue = continue_input == "y"
    display_goodbye_message()

def wave_4_run_game():
    display_welcome_message()
    game_continue = True
    played_words = []
    while game_continue:
        print("Let's draw 10 letters from the letter pool...")
        letter_bank = draw_letters()
        display_drawn_letters(letter_bank)
        display_game_instructions()
        user_input_word = input()

        while( not uses_available_letters(user_input_word, letter_bank)):
            display_needs_valid_input_message()
            user_input_word = input()
        
        score = score_word(user_input_word)
        display_score(score)
        played_words.append(user_input_word)

        display_retry_instructions()
        continue_input = input()
        game_continue = continue_input == "y"
    display_highest_score(get_highest_word_score(played_words))
    display_goodbye_message()

def main(wave):
    if(wave == 1):
        wave_1_run_game()
    elif(wave == 2):
        wave_2_run_game()
    elif(wave == 3):
        wave_3_run_game()
    elif(wave == 4):
        wave_4_run_game()
    else:
        print("Please input a wave number.  Valid wave numbers are 1, 2, 3, 4.")

if __name__ == "__main__":
    args = sys.argv
    if(len(args) >= 2 and args[1].isnumeric()):
        wave = int(args[1])
    else:
        wave = "ERROR"
    main(wave)