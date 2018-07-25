import itertools
import json
import os

# config = json.loads(open('./config.json').read())
# NOTE: uncomment if you want just a word list


def LeetWords(word):
    REPLACE = {'o': '0', 'l': '1', 'i': '1', 'z': '2', 'e': '3',
               'a': '4', 's': '5', 'g': '6', 't': '7', 'b': '8', 'g': '9'}
    possibles = []
    for l in word.lower():
        ll = REPLACE.get(l, l)
        possibles.append((l,) if ll == l else (l, ll))
    return [''.join(t) for t in itertools.product(*possibles)]


def Capitalise(s):
    return list(map(''.join, itertools.product(*(sorted(set((c.upper(), c.lower()))) for c in s))))


def WordList(config):
    wl = []

    givenWord = config['word']

    for word in LeetWords(givenWord):
        wl += Capitalise(word)

    FILE = open("WordList.csv", "w")
    os.remove("createWordList.pyc")

    FILE.write('value1\n')
    # NOTE: if multiple then FILE.write('value1, value2\n')

    for word in wl:
        FILE.write(word + '\n')
        # NOTE: if multiple then FILE.write(word ',' + <word 2> + '\n')

    FILE.close()
    print ('WordList Complete...')


# NOTE: uncomment if you want just a word list
# WordList(config)
