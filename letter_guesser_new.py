import random
word_file = "/usr/share/dict/words"
words = open(word_file).read().splitlines()
random_word = random.choice(words)
list(random_word)
secret_word = (list(random_word))
print(secret_word)
for character in secret_word:
    print("_")





