num = int(input())
leng = int(input())
starter = num
step = num
my_li = []
for i in range(leng):
    my_li.append(starter)
    starter += step
print(my_li)

# Ex 2
user_word = input()
unique_chars = ""
for char in user_word:
    if char not in unique_chars:
        unique_chars += char
print(unique_chars)
