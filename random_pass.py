import random

word1 = input("Please enter a word: ").strip()
print()
word2 = input("Please enter another word: ").strip()
print()
word3 = input("Please enter one last word: ").strip()
print()
number = int(input("Please three numbers: "))
print()
print()
sentence = "{}{}{}{}".format(word1, number, word3, word2)
x = list(sentence)
x = x[:11]
random.shuffle(x)
x = "".join(x)
print("Here is your new password: {}".format(x))