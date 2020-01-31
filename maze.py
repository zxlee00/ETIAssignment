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

    elif selectedOption == "4":
        print()
        print('Option 4: ' + SelectionMenu[3])

    elif selectedOption == "0":
        Exit()
    
    else:
        ErrorMessage()

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

                
            



        
        
