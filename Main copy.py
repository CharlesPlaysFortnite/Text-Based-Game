import termcolor
import playsound
import art
import textgamelib as lib

print(termcolor.colored(art.text2art("The Recycling Quiz"), "green"))

# Strip() removes spaces before and trailing spaces from the user input
name = input("Welcome to The Recycling Quiz, what is your name?\n> ").strip(" ")
name = name.capitalize()
printRules = input("\nHi " + name + ", would you like to see the rules? Yes or No\n> ")

if printRules.lower() == "yes":
    print("\n1. Don't " + termcolor.colored("Cheat", "red", attrs=["bold"]) + " and I will be " + termcolor.colored("Happy", "yellow", attrs=["bold"]) + "!\n2. If you get a question " + termcolor.colored("Wrong", "red", attrs=["bold"]) + " you will " + termcolor.colored("Lose", "red", attrs=["bold"]) + " one progress point!\n3. If you get " + termcolor.colored("10", "cyan", attrs=["bold"]) + " points you will win and I will be " + termcolor.colored("Happy", "yellow", attrs=["bold"]) + "!\n")

keepPlaying = input("\nAlright, type " + termcolor.colored("Happy", "yellow", attrs=["bold"]) + " to continue!\n> ")
while keepPlaying.lower() == "happy" or keepPlaying.lower() == "yes":
    currentPoints = 0
    currentQuestion = 1
    # Questions 1 - 8
    userAnswer = ""
    while currentPoints < 8:
        questionAndAnswer = lib.RandomWeightedQAndA("Questions.txt")
        userAnswer = input("\nCurrent " + termcolor.colored("Points", "yellow", attrs=["bold"]) + ": " + termcolor.colored(currentPoints, "cyan", attrs=["bold"]) + "\nQuestion " + termcolor.colored(currentQuestion, "cyan", attrs=["bold"]) + ": \n" + questionAndAnswer[0] + "\n> ")
        if userAnswer == questionAndAnswer[1]:
            currentPoints += 1
            print(lib.RandomWeightedQuestion("Congratulations.txt"))
        elif userAnswer.lower() == "quit":
            exit()
        else:
            if currentPoints > 0:
                currentPoints -= 1
            print(lib.RandomWeightedQuestion("WrongAnswer.txt"))
        
        currentQuestion += 1

    # Maybe Special Chance for a double point question
    
    keepPlaying = input("Do you want to keep playing? Yes or No\n> ")
