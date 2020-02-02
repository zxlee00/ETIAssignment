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
                    startLocation = "(Row " + str(row) + ", Column " + str(col) + ")"
                if (playmaze[row][col] == "B"):
                    endLocation = "(Row " + str(row) + ", Column " + str(col) + ")"
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

    elif selectedOption == "0":
        Exit()
    
    else:
        ErrorMessage()

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

#######################################Z#######H########I################### Option 2 ##################X##############U################A##############N############################
def ViewMaze(maze):
    outputString = ""
    if (maze != []):
        for i in maze:
            outputString += str(i) + "\n"  
    else:
        outputString = "Please load a maze first!"
        
    return outputString

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

                
            



        
        
