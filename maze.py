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
        ConfigureMaze()

    elif selectedOption == "0":
        Exit()
    
    else:
        ErrorMessage()

#######################################D#######I########A#########N######### ConfigureMenu ####I#############Z##############Z################A##############T#############I########
def configuremenu():
    menulist = ["[1] Create Wall", \
            "[2] Create Passageway", \
            "[3] Create start point", \
            "[4] Create end point", \
            "[5] Exit to main menu"]
    
    for i in range(len(menulist)):
        print(menulist[i]) #print menulist using loop
        
#going back to main menu from configure manu
def menu(mainmenulist):
    print("MAIN MENU")
    print("="*9)
    
    for i in range(len(mainmenulist)):
        print(mainmenulist[i])

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

def correct_maze(): #print out maze in memory
    for line in dataInFile:
        print(line)

        
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
#def maze():
#    for i in Maze:
#        print(i)

def ConfigureMaze():

    print('='*41) #print = 41 times
    print()
    correct_maze()
    menuoption = None #define no value at all
    coordinate = None #define no value at all

    if dataInFile == []:
        print('Please load or create a new maze before configuring') #to check if the user have load the maze
        print()
    else:
        while menuoption != 5 and coordinate != 'M':
            print()
            print('Configuration Menu')
            print('='*16) #print = 16 times
            configuremenu()
            print()
            menuoption = int(input('Enter your options: '))
            if menuoption < 0 or menuoption > 5: #validate if menuoption within 1 to 5
                print('Please enter a valid option from 1 to 5')
                print()
                correct_maze()
                print()
                
            else:
                print()
                while True:
                    if menuoption == 1: #create a wall
                        print()
                        
                        while True: #this is to validate if the number entered is within maze range
                            print("Enter the coordinate of the item you wish to change E.g Row,Column")
                            print("'B' to return to Configure menu.")
                            coordinate = input("'M' to return to Main Menu: ").upper()
                            
                            if mazesize(coordinate.split(',')) == True:
                            
                                break
                            correct_maze()
                            
                            print('Please enter a valid coordinate within the maze')
                            print()
                             
                        if coordinate != "B" and coordinate != "M":
                            coordinate = coordinate.split(",")
                            y = int(coordinate[0])
                            x = int(coordinate[1])
                            if dataInFile[y-1][x-1] != "A" and dataInFile[y-1][x-1] != "B":
                                dataInFile[y-1][x-1] = "X"
                            else:
                                print("Please enter a valid input")
                        elif coordinate == "M":
                            break
                        elif coordinate == "B":
                            correct_maze()
                            break

                    if menuoption == 2:
                        print()
                        while True: #this is to validate if the number entered is within maze range
                            print("Enter the coordinate of the item you wish to change E.g Row,Column")
                            print("'B' to return to Configure menu.")
                            coordinate = input("'M' to return to Main Menu: ").upper()
                            
                            if mazesize(coordinate.split(',')) == True:
                            
                                break
                            correct_maze()
                            print('Please enter a valid coordinate within the maze')
                            print()
                        if coordinate != "B" and coordinate != "M": 
                            coordinate = coordinate.split(",")
                            y = int(coordinate[0])
                            x = int(coordinate[1])
                            if dataInFile[y-1][x-1] != "A" and dataInFile[y-1][x-1] != "B":
                                dataInFile[y-1][x-1] = "O"
                            else:
                                print("Please Enter A Valid Input")
                        elif coordinate == "M":
                            break
                        elif coordinate == "B":
                            correct_maze()
                            break

                    if menuoption == 3:
                        while True: #this is to validate if the number entered is within maze range
                            print("Enter the coordinate of the item you wish to change E.g Row,Column")
                            print("'B' to return to Configure menu.")
                            coordinate = input("'M' to return to Main Menu: ").upper()
                            
                            if mazesize(coordinate.split(',')) == True:
                            
                                break
                            correct_maze()
                            print('Please enter a valid coordinate within the maze')
                            print()
                            
                        if coordinate != "B" and coordinate != "M":
                            coordinate = coordinate.split(",")
                            y = int(coordinate[0])
                            x = int(coordinate[1])
                            ya, xa = findaxisa()
                            if ya != -1 and xa != -1:
                                if dataInFile[y-1][x-1] != "A" and dataInFile[y-1][x-1] != "B":
                                    dataInFile[xa][ya] = "X"
                                    dataInFile[y-1][x-1] = "A"
                                else:
                                    break
                            else:
                                dataInFile[y-1][x-1] = "A"
                                
                        elif coordinate == "M":
                            break
                        elif coordinate == "B":
                            correct_maze()
                            break



                    if menuoption == 4:
                        while True: #this is to validate if the number entered is within maze range
                            print("Enter the coordinate of the item you wish to change E.g Row,Column")
                            print("'B' to return to Configure menu.")
                            coordinate = input("'M' to return to Main Menu: ").upper()
                            
                            if mazesize(coordinate.split(',')) == True:
                            
                                break
                            correct_maze()
                            print('Please enter a valid coordinate within the maze')
                            print()
                            
                        if coordinate != "B" and coordinate != "M":
                            coordinate = coordinate.split(",")
                            y = int(coordinate[0])
                            x = int(coordinate[1])
                            yb, xb = findaxisb()
                            if yb != -1 and xb != -1:
                                if dataInFile[y-1][x-1] != "A" and dataInFile[y-1][x-1] != "B":
                                    dataInFile[xb][yb] = "X"
                                    dataInFile[y-1][x-1] = "B"
                                else:
                                    break
                            else:
                                dataInFile[y-1][x-1] = "B"
                                
                        elif coordinate == "M":
                            break
                        elif coordinate == "B":
                            correct_maze()
                            break

                    if menuoption == 5:
                        break

                    correct_maze()


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

                
            



        
        
