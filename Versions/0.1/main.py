#FREDDYS FAST FISH BY MAX TYSON FOR YR 12DGT PYTHON
#RUN ON CMD (NOT IDLE) FOR BEST EXPERIENCE

#DEPENDICES
import os
import time
import random
import tkinter as tk
#VARIBLES
randColor = ['\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']
colour = "\x1b[0m"
debugMode = ["idle","windows"]
#FUNCTIONS
def debugCheck(debugID):
     global debugMode
     for i in debugMode:
        if(i == debugID) :
            return(i)
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)
def error(message):
    print(" ")
    print('\033[31m' + 'Error: ' + message + '\x1b[0m')
    time.sleep(3)
def menu(printThis):
    repeat = 0
    print ("##################################################################################################################")
    for x in range(len(printThis)): #for everything in the array print it plus its number
        print ("["+str(x)+"] "+printThis[x])
    print ("##################################################################################################################")

def logo():
    
    global randColor
    global colour
    
    debug = debugCheck("Color") #Checks if color has been set in debug mode
    if debug != ("Color"): #if it isnt then run the randomizer
      colour = random.choice(randColor) #this stops the randomizer running even if you have set a colur  
    print(colour + """
    
 _____  ____     ___  ___    ___    __ __  __  _____     _____   ____  _____ ______      _____  ____ _____ __ __ 
|     ||    \   /  _]|   \  |   \  |  |  ||  |/ ___/    |     | /    |/ ___/|      |    |     ||    / ___/|  |  |
|   __||  D  ) /  [_ |    \ |    \ |  |  ||_ (   \_     |   __||  o  (   \_ |      |    |   __| |  (   \_ |  |  |
|  |_  |    / |    _]|  D  ||  D  ||  ~  |  \|\__  |    |  |_  |     |\__  ||_|  |_|    |  |_   |  |\__  ||  _  |
|   _] |    \ |   [_ |     ||     ||___, |    /  \ |    |   _] |  _  |/  \ |  |  |      |   _]  |  |/  \ ||  |  |
|  |   |  .  \|     ||     ||     ||     |    \    |    |  |   |  |  |\    |  |  |      |  |    |  |\    ||  |  |
|__|   |__|\_||_____||_____||_____||____/      \___|    |__|   |__|__| \___|  |__|      |__|   |____|\___||__|__|
                                                                                                                 

    """ + '\x1b[0m')
    
#MAIN FUNCTIONS
def main():
 global colour
 clear()   
 user = 999
 logo() #Print the logo
 main_menu = ["Customer Details","Fish and Chip Orders","Pickup or Delivery","Exit"]
 menu(main_menu) #Print menu
 user = input (colour+" Please make a choice via number and then press enter to confirm: "+'\x1b[0m')
 if user == "0":
    print("0")
    main()
 elif user == "1":
      print("1")
      main()   
 elif user == "2":
      print("2")
      main()
 elif user == "3":
      print("3")
      main()
 elif user == "4":
      print("4")
      quit() 
 elif user == "DEBUG":
      print("DEBUG MODE")
      DEBUG()    
 else:
        error("Not an option")
        main()
#DEBUG
def DEBUG():
 global colour
 global debugMode
 clear()   
 user = 999
 userColor = 0
 logo() #Print the logo
 debug_menu = ["Select Theme Color","Exit"]
 menu(debug_menu) #Print menu
 user = input ("Please make a choice via number and then press enter to confirm: ")
 if user == "0":
    print(str("Example Colors: Black: '\033[30m', Red: '\033[31m', DarkGreen: '\033[32m', DarkYellow: '\033[33m'")) # THIS IS FOR DEBUGGING PURPOSES ONLY SO THATS WHY IT HASNT BE SIMPLIFIED
    newcolour = input("[MUST BE A NUMBER OR WONT WORK] SELECT COLOR:")
    
    print(newcolour)
    print("EXAMPLE TEXT")
    print('\x1b[0m')
    colour = str(newcolour)
    time.sleep(1)
    debugMode.append("Color") 
    DEBUG()
 elif user == "1":
      print("1")
      main()
 else:
        error("Not an option")
        main()
#PROGRAM
print ("##################################################################################################################")
main()
