#FREDDYS FAST FISH BY MAX TYSON FOR YR 12DGT PYTHON
#RUN ON CMD (NOT IDLE) FOR BEST EXPERIENCE

#DEPENDICES
import os
import time
import random
import tkinter as tk
#VARIBLES
randColor = ['\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']
debugColor = 0
#FUNCTIONS

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
    global debugColor
    if debugColor == "1":
        random.choice(randColor)
    print(randColo + """
    
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
 clear()   
 user = 999
 logo() #Print the logo
 main_menu = ["Customer Details","Fish and Chip Orders","Pickup or Delivery","Exit"]
 menu(main_menu) #Print menu
 user = input ("Please make a choice via number and then press enter to confirm: ")
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
 clear()   
 user = 999
 logo() #Print the logo
 debug_menu = ["Select Menu Color","Exit"]
 menu(debug_menu) #Print menu
 user = input ("Please make a choice via number and then press enter to confirm: ")
 if user == "0":
    print("0")
    main()
 elif user == "1":
      print("1")
      main()   
#PROGRAM
print ("##################################################################################################################")
main()
