import random


def get_words_from_file(filename):
    with open(filename, 'r') as f:
        words = [word.strip() for word in f.readlines()]
    return words


def get_random_sentence(length):
    words = get_words_from_file('sowpods.txt')
    sentence = ' '.join(random.choices(words, k=length)).lower()
    return sentence


def main():
    print('Welcome to the Random Sentence Generator!')
    while True:
        try:
            sentence_length = int(
                input('How long would you like your sentence to be (between 2 and 20)? '))
            if sentence_length < 2 or sentence_length > 20:
                raise ValueError
            else:
                break
        except ValueError:
            print('Invalid input. Please enter an integer between 2 and 20.')
            continue
    sentence = get_random_sentence(sentence_length)
    print(f'Your random sentence is:\n{sentence}')


main()
