# my_fyle = open('example.txt')
# print(my_fyle.read())

# 'r' means read i can change it to 'w' to write or 'r+' to do both
with open('test.txt', mode='r+') as my_fyle:
    text = my_fyle.write(':)')
    print(text)
