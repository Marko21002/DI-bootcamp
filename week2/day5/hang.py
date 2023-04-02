import random
import re
import sys

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive',
             'interference', 'complete', 'share', 'credit card', 'rush', 'south']
parts = ['head', 'left arm', 'right arm', 'body', 'left leg', 'right leg']
guessed = []

word = random.choice(wordslist)
separation = ''
new_word = re.sub(".", "*", word)
checked = list(new_word)
checked_str = ' '
checked_str1 = ' '
print(new_word)


def try_1():
    global checked_str
    try0 = input('Guess the letter: ')
    if try0 in guessed:
        print("already said this letter")
        try_1()
    else:
        guessed.append(try0)
        for i in range(len(word)):
            if word[i] == try0:
                checked[i] = try0
                checked_str = separation.join(checked)
                print(checked_str)


def body_check():
    global checked_str
    global checked_str1
    if len(parts) == 0:
        print('u lost all')
        sys.exit()
    elif checked_str == checked_str1:
        print('you lost your part')
        lost = random.choice(parts)
        print('I am taking your ', lost)
        parts.remove(lost)
        print('Still have', parts)

    else:
        checked_str1 = checked_str
    if len(parts) == 0:
        print('u lost all')
        sys.exit()
    if "*" not in checked_str:
        print("YOU WON!")
        sys.exit()


try_1()
body_check()
try_1()
body_check()
try_1()
body_check()
try_1()
body_check()
try_1()
body_check()
try_1()
body_check()
try_1()
body_check()
try_1()
body_check()
try_1()
body_check()
try_1()
body_check()
try_1()
body_check()
try_1()
body_check()
try_1()
body_check()
try_1()
body_check()
try_1()
body_check()
