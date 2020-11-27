# !/usr/bin/env python3
# coding:utf-8
"""
Name       : __init__.py
Author     : Kuldeep Singh Sidhu
Time       : 27-11-2020 02:58 PM
GitHub     : https://github.com/singhsidhukuldeep
Description: The main module that is used for triggering stay-awake
"""

print('>> Starting')

userName = "singhsidhukuldeep"
repoName = "stay-awake"
linkedIn = "https://www.linkedin.com/in/singhsidhukuldeep/"
website = "http://kuldeepsinghsidhu.com"
githubLink = f"https://github.com/{userName}"
name = "Kuldeep Singh Sidhu"
license = "agpl-3.0"
repoLink = f"{githubLink}/{repoName}"
errorMessage = f">> Report any issues at {repoLink}"

print(f"\n\n>> *-* Thank You for using Stay-Awake, please STAR this repo at {repoLink} ! *-* <<\n\n")

# print(errorMessage)

print('>> Importing Libraries')
try:
    import pyautogui
    import time
    import sys
    from datetime import datetime
    from random import randint
    from tqdm import tqdm
except Exception as exp:
    print (f'>><< Error: {exp}')
    print(errorMessage)
    exit()
print('>> Libraries Imported')

print('>> Setting Up')
try:
    pyautogui.FAILSAFE = False
    waitTime = 1
    try:
        waitTime = max(1, int(sys.argv[-1]))
    except Exception as exp:
        pass
    prevousLocation = None
    print(f'>> Wait time set to: {waitTime} minutes')
except Exception as exp:
    print (f'>><< Error: {exp}')
    print(errorMessage)
    exit()
print(f'>> Setup Complete')

def hasMoved(currentLocation):
    try:
        time.sleep(randint(0,2))
        if pyautogui.position() == currentLocation:
            return False
        else:
            print('>> Input detected, interrupting stay-awake')
            return True
    except Exception as exp:
        print(f'>><< Error: {exp}')
        print(errorMessage)
        exit()

def doMove(currentLocation):
    try:
        print(f'>> Moving at {currentLocation}')
        for n_move in range(1, randint(2,4)):
            if hasMoved(currentLocation):break
            pyautogui.moveTo(currentLocation[0] + n_move, currentLocation[1] + n_move)
            pyautogui.moveTo(currentLocation)
            if hasMoved(currentLocation): break
            pyautogui.moveTo(currentLocation[0] - n_move, currentLocation[1] - n_move)
            pyautogui.moveTo(currentLocation)
            if hasMoved(currentLocation): break
            pyautogui.moveTo(currentLocation[0] - n_move, currentLocation[1] + n_move)
            pyautogui.moveTo(currentLocation)
            if hasMoved(currentLocation): break
            pyautogui.moveTo(currentLocation[0] + n_move, currentLocation[1] - n_move)
            pyautogui.moveTo(currentLocation)
        print(f'>> Made movement at {datetime.now().time()}')
    except Exception as exp:
        print(f'>><< Error: {exp}')
        print(errorMessage)
        exit()

try:
    while (True):
        print('>> Checking')
        if prevousLocation == None:
            prevousLocation = pyautogui.position()
            print('>> Testing Stay-Awake')
            doMove(prevousLocation)
        elif prevousLocation == pyautogui.position():
            print(">> No manual movement detected >> Triggering stay-awake")
            doMove(prevousLocation)
        else:
            currentLocation = pyautogui.position()
            print(f'>> Mouse manually moved from {prevousLocation} to {currentLocation} >> No stay-awake triggered')
            prevousLocation = currentLocation
        for _ in tqdm(range(waitTime * 60), desc = f'>> Waiting for {waitTime*60} seconds'):
            time.sleep(1)
except Exception as exp:
    print(f'>><< Error: {exp}')
    print(errorMessage)
    exit()