import random
# Ex1


def display_message():
    print('we learn pyhon')


display_message()
# Ex2


def favorite_book(title) -> str:
    print('my fav book ', title)


favorite_book(input())
# Ex 3


def describe_city(city, country):
    print(f"{city} is in {country}")


describe_city("los angeles", "Argentina")
# Ex 4


def random_num(num1) -> int:
    if num1 < 101:
        num2 = random.randint(1, 100)
        if num1 == num2:
            print("goal")
        else:
            print('no goal')
            print('num2 is ', num2)
    else:
        print("you need num beetwen 1 and 1000")


random_num(20)

# Ex 5


def make_shirt(size="large", text="I love Python") -> str:
    print(f"{size} size t-shrit with print text - {text}")


make_shirt()
# Ex 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


def show_magicians(mages):
    for mage in mages:
        print(mage)


def make_great(mages):
    for i in range(len(mages)):
        mages[i] = "the Great " + mages[i]


make_great(magician_names)
show_magicians(magician_names)

# Ex 7


def get_random_temp(season):
    if season == 'summer':
        return random.randint(20, 40)
    elif season == 'autumn' or season == 'fall':
        return random.randint(5, 25)
    elif season == 'winter':
        return random.randint(-10, 16)
    elif season == 'spring':
        return random.randint(10, 30)
    else:
        print('here is no season like that or you typed with upercase')
        return -9999


def main():
    season = input()
    temp = get_random_temp(season)
    print(f"{temp} degrees Celsius.")


main()
