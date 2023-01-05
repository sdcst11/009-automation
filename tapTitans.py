import pyautogui as p
import time
import keyboard #requires module
'''
TapTitans autobot
'''
p.PAUSE = 0.001
gameRegion = (470,30,490,870)
upgradeRegion = (470,523, 470, 380)

upgrades = (532,830)
helpers = (647,830)
artifacts = (760,830)

def pclick(myTuple):
    p.mouseDown(myTuple)
    time.sleep(0.05)
    p.mouseUp(myTuple)

def attack():
    for i in range(30):
        pclick( (700,400) )

def upgrade():
    button = p.locateCenterOnScreen('assets/butUpgrade.png',confidence=0.9, region=upgradeRegion)
    if button:
        pclick(button)
    time.sleep(1)
    upgrade = p.locateAllOnScreen('assets/upgradeBuy.png',confidence=0.9, region=upgradeRegion)
    uList = tuple(upgrade)
    print(uList)
    maxclicks = 0
    for i in uList:
        maxclicks += 1
        if maxclicks > 10:
            break
        button = pclick(i)

def npc():
    button = p.locateCenterOnScreen('assets/buttonNPC.png',confidence=0.9, region=upgradeRegion)
    if button:
        pclick(button)
    time.sleep(1)
    upgrade = p.locateAllOnScreen('assets/npcHire.png',confidence=0.9, region=upgradeRegion)
    uList = tuple(upgrade)
    print(uList)
    maxclicks = 0
    for i in uList:
        maxclicks += 1
        if maxclicks > 10:
            break
        button = pclick(i)
    upgrade = p.locateAllOnScreen('assets/npcHire10.png',confidence=0.95, region=upgradeRegion)
    uList = tuple(upgrade)
    print(uList)
    maxclicks = 0
    for i in uList:
        maxclicks += 1
        if maxclicks > 10:
            break
        button = pclick(i)
    upgrade = p.locateAllOnScreen('assets/npcHireUnlock.png',confidence=0.9, region=upgradeRegion)
    uList = tuple(upgrade)
    print(uList)
    maxclicks = 0
    for i in uList:
        maxclicks += 1
        if maxclicks > 10:
            break
        button = pclick(i)

keyboard.add_hotkey('space',exit)
while True:

    """
    click 30 times  
    check upgrades
    check hires
    check random
    """
    
    attack()
    upgrade()
    npc()
    #ug = p.locateCenterOnScreen('assets/upgradeBuy.png', confidence=0.8, region=gameRegion)
    fightBoss = p.locateCenterOnScreen('assets/fightBoss.png', region=gameRegion)
    rndGold = p.locateCenterOnScreen('assets/randomGold.png', confidence=0.9,region=gameRegion)
    #if ug != None:
    #    pclick(ug)
    if fightBoss != None:
        pclick(fightBoss)
    if rndGold:
        pclick(rndGold)
    
    