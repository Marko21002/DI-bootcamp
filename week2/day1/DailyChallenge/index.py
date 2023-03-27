import random
import string_utils

x = input()
y = len(x)
output = ''
print(y)
if y > 10:
    print('To much')
elif y < 10:
    print('Not enough')
else:
    print(x[0])
    print(x[9])

for z in range(len(x)):
    output += str(x[z])
    print(output)

string_list = list(x)
random.shuffle(string_list)
shuffled_string = "".join(string_list)
print(shuffled_string)
