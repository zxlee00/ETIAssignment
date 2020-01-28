import pytest

from maze import *

def test_displayingMainMenu(capfd):
    assert "MAIN MENU" in menusOfMaze(SelectionMenu)

def test_validMainMenuOptionAccepted(capfd):
    mainMenuSelection("0")
    out, err = capfd.readouterr()
    assert 'You have exited the maze!' in out

def test_invalidMainMenuOptionTriggersValidation(capfd):
    mainMenuSelection("5")
    out, err = capfd.readouterr()
    assert 'Invalid input, please select the correct selection.' in out
    
    

