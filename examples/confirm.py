import pyautogui as p

while True:
    choice = p.confirm('Enter option.', buttons=['A', 'Pie', 0])
    # Note that even if you don't put in quotation marks, the number 0
    # is still input as a string
    # Note that if you choose the "X" that a None is returned instead
    print(choice)
    print( type(choice) )