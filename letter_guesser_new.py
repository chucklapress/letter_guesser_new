import random
#file = "/usr/share/dict/words"
#words = open(file).read().splitlines()
#random_word = random.choice(words)
#list(random_word)
#secret_word = (random_word)
#print(secret_word)
#for letter in secret_word:
   # print("-")

#guesses = "a,e,i,o,u"
#for letter in secret_word:
  #  if letter in guesses:
    #    print(letter),
 #   else:
     #   print("-")
#guess = input('guess a letter')
#guesses += guess
#for letter in secret_word:
    #if letter in guesses:
  #      print(letter),
 #   else:
 #       print("_")
file = "/usr/share/dict/words"
words = open(file).read().splitlines()
random_word = random.choice(words)
list(random_word)
secret_word = (random_word)
print(secret_word)
for letter in secret_word:
    print("-")

guesses = "a,e,i,o,u"

turns = 8
while turns > 0 :
    for letter in secret_word:
        if letter in guesses:
            print(letter),
        else:
            print("_")
    guess = input('guess a letter')
    guesses += guess
    turns -= 1




