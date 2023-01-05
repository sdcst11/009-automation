import pyautogui as p

"""
LocateCenterOnScreen
This finds the first location that the image can be found.  If there are
multiple instances, only the first is found.

"""
'''Basic Search
    Finds the first time an image appears and returns the location of the
    center of the image as a Tuple (x,y).
    If the image can't be found, it returns a value of None
    There must be an exact match, pixel for pixel'''
img = p.locateCenterOnScreen('assets/gimp.png')
print(img)

'''Confidence
    Adding an optional parameter of confidence accepts slight differences.
    The match must be a % match given as a decimal (0-1)
    This example is looking for a 92% match'''
img = p.locateCenterOnScreen('assets/gimp.png',confidence=0.92)
print(img)

'''Region
    You can limit the region that you are going to search in using
    the region parameter. Region is a tuple of 4 elements:
    (leftX, topY, boxWidth, boxHeight)
    For example:
    (10,20,200,100) will search a box that is 200 pixels wide
    100 pixels tall starting at coordinate(10,20), so it goes from
    10-209 pixels horizontally and from 20-119 pixels vertically'''
img = p.locateCenterOnScreen("assets/gimp.py", region=(10,20,300,300) )



