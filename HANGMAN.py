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
    print("Woordkiezer, Kies een woord: ")
    woordKiezer = input().upper()
    woord = list(woordKiezer)
    return woord

#We maken er een list van en zetten de game op true met een fouten op 0

print("Welkom bij galgje !")
time.sleep(0.5)
print("--------------------")
print("Je hebt max 10 fouten")
time.sleep(0.5)
print("Let op: er is een woordkiezer en een woordrader !")
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
    print("Kies een letter :")
    letter = input().upper()
    char = letter
    if letter in woord:
        goed += 1
        print("Je hebt " + str(goed) + " goed!")
        for index, letter in enumerate(woord):
            if letter == char:
                leegwoord[index] = letter
        if leegwoord == woord:
            print("Gefeliciteerd, je hebt de game gewonnen !")
            game = False
    else:
        fout += 1
        print("FOUT ! Je hebt " + str(fout) + " fouten .")
        print(HANGMAN[fout])
