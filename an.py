# WORDLE SOVER
# Willima Dann
#   Hire me! 
#     linkedin : https://www.linkedin.com/in/william-dann-a82299182/ 
#     email    : s-william.dann@lwtech.edu 

from wordle import load_wordlist
from random import choice

def guess(word):
    print('Computer Guess: %s' % word)
    inp = input('Result (x=match, -=partial, _=no match): ')

    if len(inp) == len(word):
        return inp
    return guess()

def eliminate(words, guess, result):
    for i in range(len(result)):
        if result[i] == '_':
            words = list(filter(lambda x: not guess[i] in x, words))

        if result[i] == '-':
            words = list(filter(lambda x: guess[i] in x and x[i] != guess[i], words))

        if result[i] == 'x':
            words = list(filter(lambda x: x[i] == guess[i], words))

    return words

def make_guess(words):
    word   = choice(words)
    result = guess(word)

    words = eliminate(words, word, result)

    if len(words) == 1:
        return words[0]

    return make_guess(words) 

if __name__ == "__main__":
    print(make_guess(load_wordlist(5)))
