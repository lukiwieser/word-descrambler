from itertools import permutations
from english_words import english_words_lower_set
from argparse import ArgumentParser


def main(args):
    scrambled_word = args.word

    perms = [''.join(p) for p in permutations(scrambled_word)]
    perms_set = set(perms)

    print("Found words:")
    found_words = perms_set.intersection(english_words_lower_set)
    for word in found_words: 
        print(word)

    print("\nFinished")


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-w', '--word', help='the word to descramble', type=str, required=True)
    args = parser.parse_args()
    main(args)

