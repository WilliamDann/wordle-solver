from random import choice

def load_wordlist(n=5):
    words = []

    with open('words.txt', 'r', encoding='utf16') as wordlist:
        words = wordlist.read().split('\n')
        words = filter(lambda x: len(x) == n, words)
        words = map(lambda x: x.lower(), words)

    return list(words)

def pick_word(n=5):
    return choice(load_wordlist(n))

def guess(guess: str, actual: str):
    if load_wordlist(len(actual)).index(guess) == -1:
        raise Exception('Invalid word: %s' % guess)
    if len(guess) != len(actual):
        raise Exception('len of Guess and Actual do not match!')

    solution = list('_'*len(actual))
    for i in range(len(guess)):
        # position match
        if guess[i] == actual[i]:
            solution[i] = 'x'

        # letter match
        elif guess[i] in actual:
            solution[i] = '-'

    return ''.join(solution)