#FREDDYS FAST FISH BY MAX TYSON FOR YR 12DGT PYTHON
#RUN ON CMD (NOT IDLE) FOR BEST EXPERIENCE

#DEPENDICES
import os
import os.path
import sys
import time
import random
import tempfile
import tkinter as tk
#VARIBLES

tempPath = tempfile.gettempdir() 

randColor = ['\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']
colour = "\x1b[0m"
debugMode = ["idle","windows","DEBUG","data"]#Start up Debug tags. TAGS:{idle: Allows debugging on idle} {windows: Sets the platform to be windows} {DEBUG: Turns on debuging mode and allows acess to the debug menu} {Color: Tells the randomizer that color has been set in the debug menu} {data: Prints extra infomation} 
#FUNCTIONS
def reset():
     fileExists = os.path.isfile(tempPath+"\session.txt") #Check if it exists
     debug = debugCheck("data") #Checks if color has been set in debug mode
     if debug == "data":
          print("fileExists: " + str(fileExists))
          print("tempPath: " + tempPath+"\session.txt")
     
def in_idle():
    try:
        return sys.stdin.__module__.startswith('idlelib')
    except AttributeError:
        return True

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
 f = open(tempPath+"\session.txt", "a")
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
 debug_menu = ["Select Theme Color","Temp File Location","Print Data While running","Exit"]
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
     print(tempfile.gettempdir())
     time.sleep(1.5)
     DEBUG()
 elif user == "2":
      debugMode.append("data")
      DEBUG()
 elif user == "3":
      main()
 else:
        error("Not an option")
        main()
#PROGRAM
debug = debugCheck("data") #Checks if data has been set in debug mode
if debug == "data":
 print("Defined Functions, Set vars, Imported dependices")        
print ("##################################################################################################################")
f = open(tempPath+"\session.txt", "a")
f.write("----------------") #Header the doc (used to indecate a break between sessions in the history)
f.close()
if debug == "data":
 print("Opened File, Set file header")        
idleCheck = "idlelib" in sys.modules # NOT PLACED IN VARIBLES BECUASE THEN in_idle() WOULD BE DEFIEND AFTER BEIGN CALLED WHICH RESULTS IN AN ERROR
idleDebug = debugCheck("idle")#SAME HERE
if debug == "data":
 print("Checked for idle and for idle debug tag")
 print("idleCheck: "+str(idleCheck))
 print("idleDebug: "+idleDebug)
reset()
if debug == "data":
 print("Reset files")

if idleCheck == True: #IF it is then run the next check
        if idleDebug == "idle": #if the debug tag is set to idle then alert that it is and continue
              if debug == "data":
                print("idle debug tag set, dont show warning menu") 
              error("Runnning in idle with debug mode")
              main()
        else: #else show the idle menu
             if debug == "data":
               print("idle debug tag not set, showing warning")
             runInIdle()
else:
     if debug == "data":
      print("idle check returned false, running as normal")
     main()   
