import random
import re


def listToString(s):
   str1 = " "
   return (str1.join(s))

def checkWin(s):
   return s.find("_") != -1

count = 0
with open("C:\\Users\\yoghu\\Downloads\\PythonHangman_Harrison\\wordlist.txt", "r") as file: 
    allText = file.read() 
    words = list(map(str, allText.split())) 
hidWord = random.choice(words)

print(hidWord)
underscoreWord = re.sub("[a-zA-Z]", "_", hidWord)
temp = list(underscoreWord)
incorrect = []
#print(underscoreWord)

while count <= 6:
   if checkWin(listToString(temp)):
       print(listToString(temp))
       print("Guesses " + str(count) + "/6")
       print("Wrong Letters: " + listToString(incorrect))
       rahh = input("give me a letter: ")
       if hidWord.find(rahh) != -1:
           for i in range(len(hidWord)):
               if hidWord[i] == rahh:
                   temp[i] = rahh
       else:
            incorrect.append(rahh)
            count += 1
   else:
       break
if count > 6 :
    print("YOU SUCK!!!")
    print("Correct Word: " + hidWord)
else:
    print("you won nerd!")
    print("Correct Word: " + hidWord)




