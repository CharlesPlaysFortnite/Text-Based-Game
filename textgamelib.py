import random
import termcolor
import time
import sys
import os

#L. Yearwood
#November 9, 2020
#Prints an ASCII Art Frog

#parameters: none
#preconditions:previous print ended with a newline
#result: output to the terminal
#return value: none
def printFrog():
    print("            _   _")
    print("           (.)_(.)")
    print("        _ (   _   ) _")
    print("       / \/`-----'\/ \\")
    print("     __\ ( (     ) ) /__")
    print("     )   /\ \._./ /\   (")
    print("      )_/ /|\   /|\ \_(")

##################################################
#Andrew Young
#November 11, 2021
#Prints a variety of commands to help/guide player when invalid commands are entered.

#parameters: # of attempts
#precondition: Number of incorrect tries must be kept track and set as a numeric variable. 
#result: The chosen message outputs to the terminal.
#return value: None.
#helper function for printHelp
def checkAttempt(attempt):
    return attempt <= 3

#main function
def printHelp(attempt):
    help = checkAttempt(attempt)
    rand=random.randint(1,3)
    text = "help"
    printString = termcolor.colored(text, 'red', attrs = ['blink'])
    if help and rand == 1: 
        print ("That command is not valid.")
    elif help and rand == 2:
        print ("Unrecognized command, please try again.")
    elif help and rand == 3:
        print ("Invalid command.")
    elif not help and rand == 1:
        print (f"Type \"{printString}\" for a list of available commands.")
    elif not help and rand == 2:
        print (f"Enter \"{printString}\" if you need any help!")
    elif not help and rand == 3:
        print (f"Are you having trouble? Try typing \"{printString}\" in the console!")

##################################################
#M. Chen
#November 11th, 2021
#Generates a random name for a character in your game, whether or not a last name is printed and gender can be controlled.

#perameters: 2 - Formatted: nameGenerator("yes/no","boy/girl")
#printLast - controls whether or not a last name will be printed: "yes/no"
#gender - controls the gender of the name printed: "boy/girl"
#i.e. nameGenerator("yes","boy") will generate a boy's name with a first name and a last name.

#preconditions: random library is imported (import random); variable for a character name is available, i.e. charName1 = nameGenerator("yes","boy")

#return value: no.

def nameGenerator(printLast,gender):

    if gender.lower() == "boy":
        getName("firstNamesBoy.txt","lastNamesBoy.txt",printLast)

    elif gender.lower() == "girl":
        getName("firstNamesGirl.txt","lastNamesGirl.txt",printLast)

#Helper function to read the files where the lists of names are stored.
def fileReader(file,list):
    myList = list
    fileIn = open(file)
    line = fileIn.readline()
    while line != "":
        myList.append(line.strip())
        line=fileIn.readline()

#Helper function to check for printLast and to put the read files into lists.
def getName(fileName,lastFileName,printLast):
    firstList = []
    lastList = []

    fileReader(fileName,firstList)
    fileReader(lastFileName,lastList)

    if printLast.lower() == "no":
        firstName = random.choice(firstList)
        print(firstName)
    else:
        firstName = random.choice(firstList)
        lastName = random.choice(lastList)
        print(firstName, lastName)

##################################################
#A. Chen
#Nov 16 2021
#Returns a copy of 2 variables as 0, 0. However keeps the orginal variables the same

#Parameters - a tuple variable that holds 2 values within
#Preconditions - 2 or # of variables existing
#Results - returns the variables within the tuple as 0's
#Return Value - your 2 values, both in 0
#e.g. score = 545678 
#     hp = 100 
#     gameinfo = ((score, hp)) 
def refresh(gameinfo):
    score = gameinfo[0] 
    hp = gameinfo[1] 
    hp = 0 
    score = 0 

    return((score, hp)) 

##################################################
#Made by: JT Borba
#Wednesday November 11th
#Prints a list of interactable objects in a room.

#Parameters: A list of objects in the room into the code corresponding with the proper room.
#Preconditions: Must have created a list of items.
#Result: Output to the terminal.
#Return Value: None

def printObjectList(objects):
    import random
    import termcolor
    red = printString = termcolor.colored(objects,'red')
    green = printString = termcolor.colored(objects,'green')
    yellow = printString = termcolor.colored(objects,'yellow')
    cyan = printString = termcolor.colored(objects,'cyan')
    colours = random.randint(1,5)
    if colours == 2:
        print (red)
    if colours == 3:
        print (green)
    if colours == 4:
        print (yellow)
    if colours == 5:
        print (cyan)

##################################################
#Charles Wang
#Tuesday, November 16th 
#This function returns weighted questions out of a file. The chance of a question being chosen is its weight.

#The user will input a file containing the questions and the weights of those questions
#The user should separate the question and the weight with a '|'
#The function will return a string which is the question that was chosen.
import random

def RandomWeightedQuestion(filename):
    possibilitiesAndWeight = open(filename)
    possibilities = []
    weights = []
    rightWeightBarrier = []

    line = possibilitiesAndWeight.readline()
    while line != "":
        possibilities.append(line.split('|')[0])
        weights.append(int(line.split("|")[1]))
        line = possibilitiesAndWeight.readline()

    sumOfWeights = 0
    i = 0
    while i < len(weights):
        sumOfWeights += weights[i]
        rightWeightBarrier.append(sumOfWeights)
        i += 1 

    randomGenNum = random.randint(0, sumOfWeights-1)
    i = 0
    while i < len(weights) and randomGenNum >= rightWeightBarrier[i]:
        i += 1
    if i < len(weights):
        return possibilities[i]

##################################################
#Function by Brian Chang
#Submission Date November 12, 2021
#Prints a divider to make the sections of the game divided and help the aesthetic of the game.

#Parameters: 2 - printDivider("Symbol", Amount) Input for symbol is whatever symbol is wanted to be printed. Input for Amount is the number of times "Symbol" is printed.
#Symbol should be a valid Unicode character. Amount should be no more that 40.
#The character is printed the amount of times wanted
#No return value
def printDivider(symbol, amount):
    print(symbol * amount)

##################################################
#Conall Yoon
#November 22
#This Funtion allows you to typw out a string letter by letter

#parameters: Inorder for the funtion to work the user must put their string inside the brackets. Simular to a print statement.
#pre conditions:time and sys must be imported.
#result: The chosen message outputs to the terminal.
#return value: none 
def typewrite(y):
    for x in y:
        sys.stdout.write(x)
        sys.stdout.flush()
        #To change the delay change 0.10
        time.sleep(0.10)

##################################################
#G. Wu
#November 10, 2021
#Collects info from the player and stores them in a list
#parameters: none
#precondition: none
#result: saves info in a list and returns the list, you can take any info from the list using the index.
#return value: none

def getUserInfo():
    userName = input(str("What is your name? "))
    userAge = input("How old are you? ")
    favColour = input(str("What is your favorite colour? ")) #input Marius wants for his game
    favAnimal = input(str("What is your favorite animal? ")) #input Marius wants for his game
    infoList = [userName, userAge, favColour, favAnimal]
    return infoList

##################################################
#Charles Wang
#Monday, November 22th 
#This function returns weighted questions out of a file. The chance of a question being chosen is its weight.

#The user will input a file containing the questions, the weights and the answer of those questions
#The user should separate the question, the weight and the answer with a '|'
#The function will return a list which contains the question and the answer that was chosen.
import random

def RandomWeightedQAndA(filename):
    possibilitiesWeightAndAnswers = open(filename)
    possibilities = []
    weights = []
    rightWeightBarrier = []
    answers = []
    output = []

    line = possibilitiesWeightAndAnswers.readline()
    while line != "":
        possibilities.append(line.split("|")[0])
        weights.append(int(line.split("|")[1]))
        answers.append(line.split("|")[2].strip("\n"))
        line = possibilitiesWeightAndAnswers.readline()

    sumOfWeights = 0
    i = 0
    while i < len(weights):
        sumOfWeights += weights[i]
        rightWeightBarrier.append(sumOfWeights)
        i += 1 

    randomGenNum = random.randint(0, sumOfWeights-1)
    i = 0
    while i < len(weights) and randomGenNum >= rightWeightBarrier[i]:
        i += 1
    if i < len(weights):
        output.append(possibilities[i])
        output.append(answers[i])
        return output

##################################################
#M. Chen
#November 23rd, 2021
#Clears the console. 
#It's recommended to use this function at the beginning of a program once to clear the two lines of output that appear each time a program is ran.

#perameters: 0
#preconditions: os library is imported. (import os)
#return value: no.

def clearConsole():
    clear = lambda: os.system('clear')
    clear()

##################################################

