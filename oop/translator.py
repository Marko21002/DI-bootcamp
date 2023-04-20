from googletrans import Translator
translator = Translator()
french_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
translated_words = []
for i, word in enumerate(french_words):
    translated_words.append(translator.translate(
        text=word, dest='en').text)
print(translated_words)
my_dict = dict(zip(french_words, translated_words))
print(my_dict)
