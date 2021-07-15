from random import *
import os

def dict_words():
    word = []
    with open("./words.txt", "r", encoding="utf-8") as f:
        for line in f:
            word.append(line.rstrip('\n'))
    return (dict(enumerate(word)))

def pick_random_num_word():
    rand = 0
    dict = dict_words()
    rand = randrange(len(dict))
    return rand

def return_word(words, num):
    word = words[num]
    return word


def word_to_lines_list(word):
    _word = list(word)
    lines = ["-" for i in range(0, len(_word))]
    return lines

def word_to_lines_str(lines):
    word_line = "".join(lines)
    return word_line

def guessing(word, letter, line):
    os.system("clear")
    answer = list(word)
    while answer != line:
        os.system("clear")
        print("Welcome to x- HAGNMAN -x")
        print("\n")
        print("Guess the word!")
        lines = "".join(line)
        print(lines)
        # print("\n")
        # print(answer)
        # print(line)
        letter = input("Enter a letter: ")
        for i in range(0, len(answer)):
            if answer == line:
                break
            elif answer[i] == letter:
                line[i] = letter
    os.system("clear")
    print("You won!")
    print(f"The word is {word}")         