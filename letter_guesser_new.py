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
random_word = random.choice(words).lower()
list(random_word)
secret_word = (random_word)
print(secret_word)
guesses = "a,e,i,o,u"
#guesses = []
turns = 8
while turns > 0 :
    missed = 0
    for letter in secret_word:
        if letter in guesses:
            print(letter),
        else:
            print("_")
            missed += 1
            print(missed)
    if missed == 0:
        print('winner')
        break
    guess = input('guess a letter')
    guesses += guess
    if guess not in secret_word:
        turns -= 1
        print('letter not in word')
        if turns == 0:
            print(secret_word)





