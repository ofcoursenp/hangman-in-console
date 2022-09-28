from PyDictionary import PyDictionary
from hangman import HANGMAN
from words import words
dictionary = PyDictionary()
import random
HANGMANPICS = HANGMAN

r = random.randint(1,2643)

b = words[r]

defination = dictionary.meaning(b)
print(defination)


splitword = [*b]
lenword = len(splitword)
dash = []

for i in range(1,lenword+1):
    dash.append("_")



guessword_str = ''.join(dash)
i = 0
guessed_words = []
while guessword_str != dash:
    n = input("Enter a word for the guess : ")
    guessed_words.append(n)
    print(f"you have already gussed {guessed_words}")
    for idx,w in enumerate(splitword):
        if w == n:
            dash.insert(idx,w)
            dash.pop(idx+1)
            i -=1

    print("__________________________")
    print(dash)
    print("__________________________")
    i +=1
    if i == 1:
        print(HANGMANPICS[i-1])
    if i == 2:
        print(HANGMANPICS[i-1])
    if i == 3:
        print(HANGMANPICS[i-1])
    if i == 4:
        print(HANGMANPICS[i-1])
    if i == 5:
        print(HANGMANPICS[i-1])
    if i == 6:
        print(HANGMANPICS[i-1])
    if i == 7:
        print(HANGMANPICS[i-1])
        print(f"U failed to guess the word , the actuall word was {b}")
        break

    guessword_str = ''.join(dash)
    if guessword_str == b:
        print("Wow u did it")


# I know this code is clusterd but im too lazy to think of a solution