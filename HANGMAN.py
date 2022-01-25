import time
import os
HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  | |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-+-\
|   |
|   |
|  | |
|  | |
|
--------
""")
# Console clearen voor de woord rader
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

#Functie voor degene die het woord kiest
def kiesWoord():
    print("Wordchooser, Choose a word: ")
    woordKiezer = input().upper()
    woord = list(woordKiezer)
    return woord

#We maken er een list van en zetten de game op true met een fouten op 0

print("Welcome to hangman !")
time.sleep(0.5)
print("--------------------")
print("Max mistakes you can make is 10")
time.sleep(0.5)
print("Attention ! : There is a word chooser and a word guesser !")
woord = list(kiesWoord())

clearConsole()
game = True
fout = -1
goed = 0
leegwoord = list("")

for i in range(len(woord)):
    leegwoord = list(leegwoord);
    leegwoord.append("_")
#Galgje MAIN
while game and fout < 10:
    print(leegwoord)
    print("Choose a letter :")
    letter = input().upper()
    char = letter
    if letter in woord:
        goed += 1
        print("You have " + str(goed) + " points !")
        for index, letter in enumerate(woord):
            if letter == char:
                leegwoord[index] = letter
        if leegwoord == woord:
            print("congratulations, you won the game !")
            game = False
    else:
        fout += 1
        print("MISTAKE : You have " + str(fout) + " mistakes .")
        print(HANGMAN[fout])
