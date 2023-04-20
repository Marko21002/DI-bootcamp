import collections


class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, word):
        count = self.text.count(word)
        if count == 0:
            return None
        else:
            return f"'{word}' appears {count} times in the text."

    def most_common_word(self):
        words = self.text.split()
        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]

    def unique_words(self):
        words = self.text.split()
        return list(set(words))


text = Text("A good book would sometimes cost as much as a good house.")
print(text.word_frequency("good"))
print(text.most_common_word())
print(text.unique_words())
