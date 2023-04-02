my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_string = 'on ystal ya ystal'
my_sum = [1, 5, 4, 2]


def integrate(list):
    index = int(input('index: '))
    item = input('item: ')
    list[index] = item
    print(list)


def count_space(string) -> str:
    count = 0
    for i in range(len(string)):
        if string[i] == ' ':
            count += 1
    print("spaces in string =", count)


def up_low_case(string) -> str:
    up = 0
    low = 0
    non_alpha = 0
    for i in range(len(string)):
        if string[i].isupper():
            up += 1
        elif string[i].islower():
            low += 1
        else:
            non_alpha += 1
    print("lower -", low, "upper -", up, "non alpha characters -", non_alpha)


def my_summ(list):
    my_summ = sum(list)
    print(my_summ)


def factorial(num) -> int:
    result = 1
    for i in range(1, num+1):
        result *= i
    print(result)


def find_max(list):
    count = list[0]
    for i in range(len(list)):
        if count < list[i]:
            count = list[i]
    print("biggest number is -", count)


def is_palidrome():
    x = input()
    x_reverse = "".join(reversed(x))
    if x == x_reverse:
        print("YES")
    else:
        print("NO")


integrate(my_list)
count_space(my_string)
up_low_case(my_string)
my_summ(my_sum)
factorial(4)
find_max(my_sum)
is_palidrome()
