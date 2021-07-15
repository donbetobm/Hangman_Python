from functions import *
import os

def run():
    result = False
    words_dictionary = dict_words()
    random_number = pick_random_num_word()
    random_word = return_word(words_dictionary, random_number)
    word_to_lineslist = word_to_lines_list(random_word)
    word_to_linesstr = word_to_lines_str(word_to_lineslist)
    letter = ""

    # print("word dictionary regresa: ", words_dictionary)
    # print("random number regresa: ", random_number)
    # print("random word regresa: ", random_word)
    # print("word to lines list regresa: ", word_to_lineslist)
    # print("word to lines str regresa: ", word_to_linesstr)
    # pendiente manejar error si ingresa int o len(letter) > 2


    result = guessing(random_word, letter, word_to_lineslist)


if __name__=='__main__':
    run()