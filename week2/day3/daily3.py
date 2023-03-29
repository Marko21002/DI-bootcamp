word = input("Please enter a word: ")
dictionary = {}

for index, letter in enumerate(word):
    if letter not in dictionary:
        dictionary[letter] = [index]
    else:
        dictionary[letter].append(index)

print(dictionary)

# Ex 2
items_purchase = {"Water": "$1", "Bread": "$3",
                  "TV": "$1,000", "Fertilizer": "$20"}

wallet = "$300"
wallet_num = int(wallet[1:])

affordable_items = []

for item, price in items_purchase.items():
    price_num = int(price[1:].replace(',', ''))
    if price_num <= wallet_num:
        affordable_items.append(item)

if len(affordable_items) > 0:
    affordable_items.sort()
    print(affordable_items)
else:
    print("Nothing")
