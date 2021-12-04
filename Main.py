import termcolor
import art
import playsound
import textgamelib as lib
import time
import sys
from pygame import mixer

lib.clearConsole()
print(termcolor.colored(art.text2art("The Recycling Quiz"), "green"))
mixer.init()
mixer.Channel(0).play(mixer.Sound('usual-music.mp3'))
mixer.Channel(1).play(mixer.Sound('epic-music.mp3'))
mixer.Channel(1).pause()


# Strip() removes spaces before and trailing spaces from the user input
name = input("Welcome to The " + termcolor.colored("Recycling", "green", attrs=["bold"]) + " Quiz, what is your name?\n> ").strip(" ")
name = name.capitalize()
printRules = input("\nHi " + name + ", would you like to see the rules? Yes or No\n> ")

if printRules.lower() == "yes":
    print("\n1. Don't " + termcolor.colored("Cheat", "red", attrs=["bold"]) + " and I will be " + termcolor.colored("Happy", "yellow", attrs=["bold"]) + "!\n2. If you get a question " + termcolor.colored("Wrong", "red", attrs=["bold"]) + " you will " + termcolor.colored("Lose", "red", attrs=["bold"]) + " one progress point!\n3. If you get " + termcolor.colored("10", "cyan", attrs=["bold"]) + " points you will win and I will be " + termcolor.colored("Happy", "yellow", attrs=["bold"]) + "!\n")

keepPlaying = input("\nAlright, type " + termcolor.colored("Happy", "yellow", attrs=["bold"]) + " to continue!\n> ")
while keepPlaying.lower() == "happy" or keepPlaying.lower() == "yes" or keepPlaying == "":
    mixer.Channel(0).play(mixer.Sound('usual-music.mp3'))
    mixer.music.pause()
    currentPoints = 0
    currentQuestion = 1
    # Questions 1 - 8
    userAnswer = ""
    while currentPoints < 8:
        lib.clearConsole()
        questionAndAnswer = lib.RandomWeightedQAndA("Questions.txt")
        userAnswer = input("\nCurrent " + termcolor.colored("Points", "yellow", attrs=["bold"]) + ": " + termcolor.colored(currentPoints, "cyan", attrs=["bold"]) + "\nQuestion " + termcolor.colored(currentQuestion, "cyan", attrs=["bold"]) + ": \n" + "Where do you think " + questionAndAnswer[0] + " should be thrown away? Recycling(r), Garbage(g) or Organic(o)" + "\n> ")
        if userAnswer.lower() == questionAndAnswer[1]:
            currentPoints += 1
            print("\n" + lib.RandomWeightedQuestion("Congratulations.txt"))
            mixer.Channel(0).pause()
            mixer.Channel(2).play(mixer.Sound("success-sound.mp3"))
            time.sleep(3)
            mixer.Channel(0).unpause()
        else:
            if currentPoints > 0:
                currentPoints -= 1
            print("\n" + lib.RandomWeightedQuestion("WrongAnswer.txt"))
            mixer.Channel(0).pause()
            mixer.Channel(2).play(mixer.Sound("fail-sound.mp3"))
            time.sleep(2)
            mixer.Channel(0).unpause()
        
        currentQuestion += 1
        input("\nPress enter to continue.")

    # Maybe Special Chance for a double point question
    while currentPoints < 10:    
        lib.clearConsole()
        isChallenge = (lib.RandomWeightedQuestion("Special.txt") == "Special")
        wantChallenge = ""
        if isChallenge:
            mixer.Channel(0).pause()
            mixer.Channel(1).unpause()
            wantChallenge = input("\n       \****__              ____                                              \n         |    *****\_      --/ 🔥\-__                                          \n         /_          (_    ./ ,/----'   🔥🔥🔥🔥🔥🔥🔥                                      \n           \__         (_./  /                                                \n              \__           \___----^__                                       \n               _/   _                  \                                      \n        |    _/  __/ )\"\ _____         *\                                    \n        |\__/   /    ^ ^       \____      )                                   \n         \___--\"                    \_____ )                                  \n                                          \"\nAhhhh! Be careful! There is a dragon here. Would you like to fight it and risk losing 2 points if you are wrong or getting 2 points if you are right? Yes or No?\n> ")
        if wantChallenge.lower() == "yes":
            questionAndAnswer = lib.RandomWeightedQAndA("HardQuestions.txt")
            userAnswer = input("\nCurrent " + termcolor.colored("Points", "yellow", attrs=["bold"]) + ": " + termcolor.colored(currentPoints, "cyan", attrs=["bold"]) + "\nQuestion " + termcolor.colored(currentQuestion, "cyan", attrs=["bold"]) + ": \n" + termcolor.colored("Where do you think " + questionAndAnswer[0] + " should be thrown away? Recycling(r), Garbage(g) or Organic(o)", "red") + "\n> ")
            if userAnswer.lower() == questionAndAnswer[1]:
                currentPoints += 2
                print("\n" + lib.RandomWeightedQuestion("SpecialCongratulations.txt"))
                mixer.Channel(1).pause()
                mixer.Channel(2).play(mixer.Sound("success-sound.mp3"))
                time.sleep(3)
            else:
                if currentPoints > 2:
                    currentPoints -= 2
                print("\n" + lib.RandomWeightedQuestion("SpecialWrongAnswer.txt"))
                #fail
                mixer.Channel(1).pause()
                mixer.Channel(2).play(mixer.Sound("fail-sound.mp3"))
                time.sleep(2)
            mixer.Channel(0).unpause()
        elif wantChallenge.lower() == "no":
            mixer.Channel(1).pause()
            mixer.Channel(0).unpause()
        else:
            questionAndAnswer = lib.RandomWeightedQAndA("Questions.txt")
            userAnswer = input("\nCurrent " + termcolor.colored("Points", "yellow", attrs=["bold"]) + ": " + termcolor.colored(currentPoints, "cyan", attrs=["bold"]) + "\nQuestion " + termcolor.colored(currentQuestion, "cyan", attrs=["bold"]) + ": \n" + "Where do you think " + questionAndAnswer[0] + " should be thrown away? Recycling(r), Garbage(g) or Organic(o)" + "\n> ")
            if userAnswer.lower() == questionAndAnswer[1]:
                currentPoints += 1
                print("\n" + lib.RandomWeightedQuestion("Congratulations.txt"))
                mixer.Channel(0).pause()
                mixer.Channel(2).play(mixer.Sound("success-sound.mp3"))
                time.sleep(3)
                mixer.Channel(0).unpause()
            else:
                if currentPoints > 0:
                    currentPoints -= 1
                print("\n" + lib.RandomWeightedQuestion("WrongAnswer.txt"))
                #fail
                mixer.Channel(0).pause()
                mixer.Channel(2).play(mixer.Sound("fail-sound.mp3"))
                time.sleep(2)
                mixer.Channel(0).unpause()
        currentQuestion += 1
        input("\nPress enter to continue.")
    
    lib.clearConsole()
    mixer.Channel(1).pause()
    mixer.Channel(0).pause()
    mixer.music.load("celeb-music.mp3")
    mixer.music.play(-1)
    print(termcolor.colored(art.text2art("Congratulations!"), "yellow", attrs=["bold"]))
    print("\nCongratulations " + name + "! You have made me happy right now.")



    keepPlaying = input("\nDo you want to keep playing? Yes or No\n> ")