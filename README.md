## SDSS Computing Studies Python Assignment
### Assignment #007 Creating a Click Bot

Objectives:
* Solve a complex problem through planning using code structures
* Make use of prebuilt modules not native to the Python basic installation
* Have programs receive automatic inputs.

Automation is becoming a huge deal, with robots replacing people doing
menial tasks every day.  Robots can be quite sophisticated, and are often
able to mimic the roles that humans once filled.

Today, we will be exploring the creation of a robot to play a simple game.
The simplest games are clicker games, although some of these can become
quite complicated.  In fact, a program can not only beat these games, but
solve more open ended games that might not appear to be simple on the surface.

To create a robot to play the game, you really need to understand the sequences
required to play the game.  There may be multiple screens; how do you navigate
between them?  There may be times that your bot becomes out of sync. How do you
detect problems and then have them fix themselves automatically?  These are
questions that we will need to address when we create our robots.

We will also be making use of 2 built in modules and 1 installed module. Some of these
modules have their oown dependencies that we will need to install manually
random
time
pyautogui
pillow (a pyautogui dependency)
opencv-python (a pyaugotui dependency)

Modules that are installed and required for a project are called **dependencies**.
Often a project may have many, many dependencies.  This can impose a security risk
if the developer is not trusted.

Pay close attention to today's example files, as they will be very important
in understanding how the code structures work.

#### How to Take Screenshots ####
* windows-I to open up your settings
* search for "print screen".  The option to have print screen to take a screenshot should be found
* open up the link and change the print screen to take a screen shot option to checked (it's a button)
* to save a screenshot to your clipboard, press print-screen button (BlueFn > Print Screen)
* it should give you the option to open snip and sketch where you can save it. You may need to open your notification center

##### Task 1: Become familiar with the time module
Open the file example1.py

##### Task 2a or Task 2b: 
Task 2a
Use Virtual Environments to add a Library
This is a very helpful resource:
https://realpython.com/python-virtual-environments-a-primer/
In this class, we are going to need to use the "command prompt" terminal rather than powershell as it allows us to create our virtual environment

Task2b
Install modules directly to your user account.
This is often not the best approach as it installs the module globally to your computer rather than to a specific project. If you were a developer, you might install specific modules for specific projects to help you keep track of the dependences.
We will use the commands
"""
py -m pip install <module_name> --user
"""


##### Task 3: Become familiar with commands in the pyautogui module.
Visit: https://pyautogui.readthedocs.io/en/latest/index.html
Follow the instructions on installing pyautogui on your computer.
You can install it once you have set up the virtual environment for your project.


##### Task 4: Planning sequences of Events
Write down the sequence of events or actions that you will need to program
into your game.  You may want to check pauses if your game needs to wait
for actions to complete. You will be submitting this document as part of
your assessment.
(5 marks)






