#FREDDYS FAST FISH BY MAX TYSON FOR YR 12DGT PYTHON
#RUN ON CMD (NOT IDLE) FOR BEST EXPERIENCE

#DEPENDICES
import os
import sys
import time
import random
import tkinter as tk
#VARIBLES
tempPath = "E:/"
randColor = ['\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']
colour = "\x1b[0m"
debugMode = ["idle","windows","DEBUG"] # {idle: Allows debugging on idle} {windows: Sets the platform to be windows} {DEBUG: Turns on debuging mode and allows acess to the debug menu}
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
    print("" + colour + """
    
 _____  ____     ___  ___    ___    __ __  __  _____     _____   ____  _____ ______      _____  ____ _____ __ __ 
|     ||    \   /  _]|   \  |   \  |  |  ||  |/ ___/    |     | /    |/ ___/|      |    |     ||    / ___/|  |  |
|   __||  D  ) /  [_ |    \ |    \ |  |  ||_ (   \_     |   __||  o  (   \_ |      |    |   __| |  (   \_ |  |  |
|  |_  |    / |    _]|  D  ||  D  ||  ~  |  \|\__  |    |  |_  |     |\__  ||_|  |_|    |  |_   |  |\__  ||  _  |
|   _] |    \ |   [_ |     ||     ||___, |    /  \ |    |   _] |  _  |/  \ |  |  |      |   _]  |  |/  \ ||  |  |
|  |   |  .  \|     ||     ||     ||     |    \    |    |  |   |  |  |\    |  |  |      |  |    |  |\    ||  |  |
|__|   |__|\_||_____||_____||_____||____/      \___|    |__|   |__|__| \___|  |__|      |__|   |____|\___||__|__|
                                                                                                                 

    """ + '\x1b[0m')
def runInIdle():
 user = 999
 logo() #Print the logo
 print("NOTE: Running in Idle can make the user experience worse (Console wont clear and ANSI colors dont work.)")
 idle_menu = ["Continue","Exit"]
 menu(idle_menu) #Print menu
 user = input (colour+" Please make a choice via number and then press enter to confirm: "+'\x1b[0m')
 if user == "0":
    print("Running In Idle")
    main()
 elif user == "1":
      print("Exiting")
      quit()   
    
#MAIN FUNCTIONS
def CustomerDetails():   
 global colour
 global tempPath
 clear()   
 user = 999
 allowDebug = debugCheck("DEBUG")
 logo() #Print the logo
 print ("##################################################################################################################")
 f = open(tempPath+"session.txt", "a")
 name = input (colour+"Please enter your name: "+'\x1b[0m')
 f.write("Customer Name: "+name)
 print("")
 CustomerDetails = ["Delivery","Pick Up"]
 menu(CustomerDetails) #Print menu
 pickUpOrDelivery = input (colour+"Please choose an option"+'\x1b[0m')
 if pickUpOrDelivery == "0":
      #Deliver Code
      print("DELIVERY")
 f.write("Order Type: "+pickUpOrDelivery)
 CustomerDetails = ["Frozen","Cooked"]
 menu(CustomerDetails) #Print menu
 
 frozenOrCooked = input (colour+"Please choose an option"+'\x1b[0m')
 f.write("Order Type: "+frozenOrCooked)
 f.close()

def main():
 global colour
 clear()   
 user = 999
 allowDebug = debugCheck("DEBUG")
 logo() #Print the logo
 main_menu = ["Customer Details","Fish and Chip Orders","Pickup or Delivery","Exit"]
 menu(main_menu) #Print menu
 user = input (colour+" Please make a choice via number and then press enter to confirm: "+'\x1b[0m')
 if user == "0":
    print("0")
    CustomerDetails()
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
 elif user and allowDebug == "DEBUG":
      
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
      
    print(str("Colors:"))
    debug_menu = ["Black","Red","DarkGreen","DarkYellow"]
    menu(debug_menu) 
    debugcol = input("SELECT COLOR:")
    if debugcol == "0":
         newcolour = "\033[30m"
    elif  debugcol == "1":
         newcolour = "\033[31m"
    elif  debugcol == "2":
         newcolour = "\033[32m"
    elif  debugcol == "3":
         newcolour = "\033[33m"           
    print(newcolour)
    print("EXAMPLE TEXT")
    print('\x1b[0m')
    colour = newcolour
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
idleDebug = debugCheck("idle")
idleCheck = 'Running IDLE' if 'idlelib.run' in sys.modules else 'Out of IDLE'
f = open(tempPath+"session.txt", "a")
f.write("----------------")
f.close()

if idleDebug != "idle":
     main()
elif idleCheck != "Out of IDLE":
        if idleDebug == "idle":
              print("Runnning in idle with debug mode")
              main()
        else:
              runInIdle()
