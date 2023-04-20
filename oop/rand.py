import random
import string
from datetime import datetime


def guess_number():
    num = int(input())
    rand_num = random.randint(1, 100)
    if num == rand_num:
        print("Success! The random number was", rand_num)
    else:
        print("Sorry, the random number was", rand_num)


# Пример вызова функции с числом 50
guess_number()


def generate_random_string(length):
    letters = string.ascii_letters
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


print(generate_random_string(5))

now = datetime.now()
print("Текущая дата:", now.date())
