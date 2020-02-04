#ETI Assignment Maze!

#-----------------------Disclaimer!--------------------#
#Need to access Option 1 before accessing Option 2 & 5 #
#------------------------------------------------------#

import csv
import datetime
from datetime import datetime
import time
from time import strptime
import sys
import os.path
import copy
import numpy

#######################################D#######I########A#########N######### SelectionMenu ####I#############Z##############Z################A##############T#############I########
#listing the menu in a list
SelectionMenu = ['Read and load maze from file', 
              'View maze', 
              'Play maze game',
              'Configure current maze',
             'Exit Maze']
Maze = []
dataInFile = []
exitGame = False
backToMenu = False

def menusOfMaze(SelectionMenu):
    menuString = "\nMAIN MENU\n==========\n"
    for i in range(0,4):
        menuString += '[{}] {}'.format(i+1, SelectionMenu[i]) + '\n'
            
    menuString += '\n'
    
    for k in range(-1,0):
        menuString += '[{}] {}'.format(k+1, SelectionMenu[k]) + '\n\n'
    return menuString

def displayMainMenu():
    print(menusOfMaze(SelectionMenu))
    selection = (input('Enter your option: '))
    mainMenuSelection(selection)
    if exitGame == False:
        displayMainMenu()
    else:
        sys.exit()

def displayGamePlayMenu(playmaze):
    outputString = ""
    startLocation = ""
    endLocation = ""
    if (playmaze != []):
        outputString = ViewMaze(playmaze)
        row = 0
        while row < len(playmaze):
            col = 0
            while col < len(playmaze[row]):
                if (playmaze[row][col] == "A"):
                    startLocation = "(Row " + str(row + 1) + ", Column " + str(col + 1) + ")"
                if (playmaze[row][col] == "B"):
                    endLocation = "(Row " + str(row + 1) + ", Column " + str(col + 1) + ")"
                col += 1
            row += 1
            
        outputString += "\nLocation of Start (A) = " + startLocation
        outputString += "\nLocation of End (B) = " + endLocation + "\n"

    else:
        outputString = "\nPlease load a maze first!"

    return outputString

def playMazeMovementPrompt(playmaze):
    gameMenuOutputString = displayGamePlayMenu(playmaze)
    print(gameMenuOutputString)
    if gameMenuOutputString != "\nPlease load a maze first!":
        movementKey = str(input("Press 'W' for UP, 'A' for LEFT, 'S' for DOWN, 'D' for RIGHT, 'M' for MAIN MENU: "))
        outputString, playmaze = movementKeySelection(playmaze, movementKey.upper())
            
    else:
        displayMainMenu()

    return outputString, playmaze

def playMazeMovementPrompt(playMaze):
    gameMenuOutputString = displayGamePlayMenu(playMaze)
    print(gameMenuOutputString)
    if gameMenuOutputString != "\nPlease load a maze first!":
        movementKey = str(input("Press 'W' for UP, 'A' for LEFT, 'S' for DOWN, 'D' for RIGHT, 'M' for MAIN MENU: "))
        outputString, playMaze = movementKeySelection(playMaze, movementKey.upper())
            
    else:
        displayMainMenu()
        
    return outputString, playMaze

def mainMenuSelection(selectedOption):
    if selectedOption == "1":
        print()
        print('Option 1: ', SelectionMenu[0])

        fileName = str(input('Enter the name of the data file: '))
        global dataInFile
        dataInFile, totalLineNo, outputString = ReadMazeInfoFromFile(fileName)
        print(outputString)

    elif selectedOption == "2":
        print()
        print('Option 2: ' + SelectionMenu[1])
        outputString = ViewMaze(dataInFile)
        print(outputString)

    elif selectedOption == "3":
        print()
        print('Option 3: ' + SelectionMenu[2])
        playMaze = copy.deepcopy(dataInFile)
        global completedGame
        completedGame = False
        while completedGame == False:
            outputString, playMaze = playMazeMovementPrompt(playMaze)
            print(outputString)
        if completedGame == True:
            print("You have completed the maze successfully!")

    elif selectedOption == "4":
        print()
        print('Option 4: ' + SelectionMenu[3])
        
        ConfigureMazeInput()

    elif selectedOption == "0":
        Exit()
    
    else:
        ErrorMessage()

def configuremenu():
    menulist = ["[1] Create Wall", \
            "[2] Create Passageway", \
            "[3] Create start point", \
            "[4] Create end point", \
            "\n[0] Exit to main menu"]
    
    for i in range(len(menulist)):
        print(menulist[i]) #print menulist using loop

    print()
    menuoption = input('Enter your options: ')
    return menuoption

#check for Startpoint
def findaxisa():
    firstya = -1 #is to validate if theres "A"
    firstxa = -1
    for row in range(len(dataInFile)): #left to right
        for col in range(len(dataInFile)): #up to down
            if dataInFile[row][col] == "A":
                firstya = row
                firstxa = col
                
    return firstxa,firstya

#check for Endpoint
def findaxisb():
    firstyb = -1 #is to validate if theres "B"
    firstxb = -1
    for row in range(len(dataInFile)):#left to right
        for col in range(len(dataInFile)):#up to down
            if dataInFile[row][col] == "B":
                firstyb = row
                firstxb = col
                
    return firstxb,firstyb

#check for range
def mazesize(coordinate): #check if configuremaze is within range of the maze size
    if coordinate[0].isalpha(): #it wont work if its a number and follow by a letter e.g 0m,2m
        return True
    elif int(coordinate[1]) > len(dataInFile[0]):
        return False
    elif int(coordinate[0]) > len(dataInFile):
        return False
    else:
        return True

#######################################D#######I########A#########N######### GamePlay Menu ####I#############Z##############Z################A##############T#############I##############
def movementKeySelection(playmaze, movementKey):
    outputString = ""
    if movementKey == "W" or movementKey == "A" or movementKey == "S" or movementKey == "D":
        row = 0
        startLocation = []
        endLocation = []
        moveLocation = []
        while row < len(playmaze):
            col = 0
            while col < len(playmaze[row]):
                if (playmaze[row][col] == "A"):
                    startLocation = [row, col]
                if (playmaze[row][col] == "B"):
                    endLocation = [row, col]
                col += 1
            row += 1

        direction = ""
            
        if movementKey == "W":
            direction = "up"
            moveLocation = [startLocation[0] - 1, startLocation[1]]
        elif movementKey == "A":
            direction = "left"
            moveLocation = [startLocation[0], startLocation[1] - 1]
        elif movementKey == "S":
            direction = "down"
            moveLocation = [startLocation[0] + 1, startLocation[1]]
        elif movementKey == "D":
            direction = "right"
            moveLocation = [startLocation[0], startLocation[1] + 1]

        if moveLocation[0] < 0 or moveLocation[0] > (len(playmaze)-1) or moveLocation[1] < 0 or moveLocation[1] > (len(playmaze[0])-1):
            outputString = "\nInvalid movement. Please try again.\n"
        else:
            moveTo = playmaze[moveLocation[0]][moveLocation[1]]
            
            if moveTo == "X":
                outputString = "\nInvalid movement. Please try again.\n"
            elif moveTo == "B":
                outputString = "\nYou have moved " + direction + ".\n"
                playmaze[moveLocation[0]][moveLocation[1]] = "A"
                playmaze[startLocation[0]][startLocation[1]] = "O"
                global completedGame
                completedGame = True
            elif moveTo == "O":
                outputString = "\nYou have moved " + direction + ".\n"
                playmaze[moveLocation[0]][moveLocation[1]] = "A"
                playmaze[startLocation[0]][startLocation[1]] = "O"
            
    elif movementKey == "M":
        displayMainMenu()
    else:
         outputString = "\nInvalid input. Please try again.\n"

    return outputString, playmaze

#######################################D#######I########A#########N######### Option 1 ####I#############Z##############Z################A##############T#############I##############
def ReadMazeInfoFromFile(fileName): 

    #need: Read the total number of lines in
    os.path.isfile("./")
    #print (filepath)

    count = 0
    dataInFile = []
    totalLineNo = 0
    if os.path.exists(fileName):
         with open(fileName, 'r') as csvfile:
            for theNoOfLine in csvfile:
                firstLine = theNoOfLine.strip('\n')
                read = firstLine.split(',')
                dataInFile.append(read)
                count = count + 1
            
                totalLineNo = count
                outputString = "Number of lines read: {}".format(totalLineNo)
        
            csvfile.close()
        
    else:
        outputString = "The <" + fileName + ">" + " file name is not found, please enter again."
        
    return dataInFile, totalLineNo, outputString

def ConfigureMazeInput():
    print('='*41) #print = 41 times
    print()
    outputString = ViewMaze(dataInFile)
    print(outputString)

    if outputString != "Please load a maze first!":
        print()
        print('Configuration Menu')
        print('='*16) #print = 16 times
        menuoption = configuremenu()
        if menuoption == "0":
            displayMainMenu()
        elif menuoption == "1" or menuoption == "2" or menuoption == "3" or menuoption == "4":
            print()
            checkConfigureMenuSelection(menuoption)
            ConfigureMazeInput()
        else:
            print("\nPlease enter a valid menu option.\n")
            ConfigureMazeInput()
    else:
        displayMainMenu()

def checkConfigureMenuSelection(menuoption):
    print("Enter the coordinate of the item you wish to change E.g Row,Column")
    print("'B' to return to Configure menu.")
    coordinate = input("'M' to return to Main Menu: ").upper()
    if coordinate == "M":
        displayMainMenu()
    elif coordinate == "B":
        print()
        ConfigureMazeInput()
    else:
        coordinate = coordinate.split(",")
        if (len(coordinate)) != 2 or (coordinate[1] == ""):
            print("\nPlease enter a valid coordinate!\n")
            checkConfigureMenuSelection(menuoption)
        else:       
            y = int(coordinate[0])
            x = int(coordinate[1])
            if (y < 0 or y > len(dataInFile) or x < 0 or x > len(dataInFile[0])):
                print("\nPlease enter a valid coordinate!\n")
                checkConfigureMenuSelection(menuoption)
            else:
                configuredMaze = ConfigureMaze(dataInFile, menuoption, y, x)

#######################################Z#######H########I################### Option 2 ##################X##############U################A##############N############################
def ViewMaze(maze):
    outputString = ""
    if (maze != []):
        for i in maze:
            outputString += str(i) + "\n"  
    else:
        outputString = "Please load a maze first!"
        
    return outputString

def ConfigureMaze(maze, menuoption, y, x):
                 
    if menuoption == "1":
        if maze[y-1][x-1] != "A" and maze[y-1][x-1] != "B":
            maze[y-1][x-1] = "X"
        else:
            print("\nThe coordinate you have entered is a start point or end point.")
            print("Please choose another coordinate or set the start point or end point to another location first.\n")
            checkConfigureMenuSelection(menuoption)

    if menuoption == "2":
        if maze[y-1][x-1] != "A" and maze[y-1][x-1] != "B":
            maze[y-1][x-1] = "O"
        else:
            print("\nThe coordinate you have entered is a start point or end point.")
            print("Please choose another coordinate or set the start point or end point to another location first.\n")
            checkConfigureMenuSelection(menuoption)

    if menuoption == "3":
        ya, xa = findaxisa()
        if ya != -1 and xa != -1:
            if maze[y-1][x-1] != "A" and maze[y-1][x-1] != "B":
                maze[xa][ya] = "O"
                maze[y-1][x-1] = "A"
        else:
            maze[y-1][x-1] = "A"

    if menuoption == "4":
        yb, xb = findaxisb()
        if yb != -1 and xb != -1:
            if maze[y-1][x-1] != "A" and maze[y-1][x-1] != "B":
                maze[xb][yb] = "O"
                maze[y-1][x-1] = "B"
        else:
            maze[y-1][x-1] = "B"

    a = numpy.asarray(maze)
    numpy.savetxt("mazeconfigured.csv", a, delimiter=",", fmt='%s')
    print("\nSaved to 'mazeconfigured.csv'!\n")

    return maze

#######################################D#######I########A#########N######### Option 0 ####I#############Z##############Z################A##############T#############I##############
def Exit():
    print()
    print('You have exited the maze!')
    global exitGame
    exitGame = True

#######################################D#######I########A#########N######### No Option ####I#############Z##############Z################A##############T#############I##############
def ErrorMessage():
    print()
    print('Invalid input, please select the correct selection.')

if __name__ == '__main__':
    displayMainMenu()

                
            



        
        
