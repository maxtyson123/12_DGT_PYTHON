#FREDDYS FAST FISH BY MAX TYSON FOR YR 12DGT PYTHON
#RUN ON CMD (NOT IDLE) FOR BEST EXPERIENCE

#VER 5.0
#DEPENDICES
import os
import os.path
import sys
import time
import random
import tempfile
import tkinter as tk
from datetime import date

#VARIBLES
today = str(date.today()) #Get todays date
amtOfFish = 0
totalCost = 0.00
tempPath = tempfile.gettempdir() # Get the temp dir
colour = "\x1b[0m"


randColor = ['\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m']
userOrder = []
userOrderPrice = []
debugMode = ["idle","windows","DEBUG","data"]#Start up Debug tags. TAGS:{idle: Allows debugging on idle} {windows: Sets the platform to be windows} {DEBUG: Turns on debuging mode and allows acess to the debug printSingleMenu} {Color: Tells the randomizer that color has been set in the debug printSingleMenu} {data: Prints extra infomation} {ignoreHistory: dont write to the history file}
customerData = [] #Format: ["name: the persons name","phone number","frozen(0) or cooked(1)","dlivery(0) or pick up(1)","adress (last becuase its optinal)"]
#FUNCTIONS
def addToOrder(strItemID, foodList, priceList):
     global userOrder
     global userOrderPrice
     global amtOfFish #Global becuase it is called later on
     global totalCost
     global customerData
     itemID = int(strItemID)
     print("Max fish is 7")
     amt = input (colour+" How many "+foodList[itemID] +" would you like: "+'\x1b[0m')
     try:
         int(amt) #trys to convert to int
         isInt = True
     except ValueError: #if it cant the return error
      isInt = False

     if isInt == False: #if it is a error
          
      error("Not an number, Re running.") #print the error
      fishMenu() #go back to the menu
     if itemID == 12: #IF ITS chips
         print(amt)
         chipsPrice = priceList[itemID]*float(amt) #convert to int times the price by the amt
         print(chipsPrice)
         totalCost = totalCost + chipsPrice #add the cost
         userOrder.append (str(amt+" scoops of chips"))
         userOrderPrice.append(chipsPrice)
         fishMenu()#go back 
     for x in range(int(amt)):
       if amtOfFish == 7:
         error("Max amount for "+foodList[itemID] +" has been ordered")
         fishMenu() #go back to the menu, this prevents it from running again for the remaining number of fsih tried.
       else: 
        print("Added "+foodList[itemID] +": " + str(x+1)) #this is to show the user that the item actually has been added,  add one to make it count properly bc lists idex starting at 0   
        amtOfFish = amtOfFish + 1   #add to the max
        totalCost = totalCost + priceList[itemID]   #add to the cost
        fishPrice = priceList[itemID]
        if customerData[2] == "0":
           print("Fish Type: "+"Frozen")
           totalCost = totalCost - 1.05 #take away the discount
           fishPrice = priceList[itemID] - 1.05
        userOrder.append(foodList[itemID])
        userOrderPrice.append(fishPrice)
        f = open(tempPath+"\session.txt", "a")
        f.write("Item: " + foodList[itemID] + ", Price: " + str("{:.2f}".format(fishPrice)) + "\n") #add to the doc
        f.close()
     fishMenu() #go back to the menu
def setHistory():
     historyDoc = open("history.txt", 'a+') #open the history doc
     tempdoc = open(tempPath+"\session.txt", 'r') #open the tempdoc
     historyDoc.write(tempdoc.read()) #write the read data from the temp doc
     historyDoc.close()
     tempdoc.close()#close them both
def printAFile(filepath):
     file = open(filepath, "r").read() #open the file in readmode
     print(file) #print the file
def reset():
     global tempPath 
     fileExists = os.path.isfile(tempPath+"\session.txt") #Check if it exists
     if fileExists == True: #if it doesnt exist no need to clear it becuase it will be created later on
          f = open(tempPath+"\session.txt","r+")
          f.truncate(0) #reset it
          f.close()
     debug = debugCheck("data") #Checks if color has been set in debug mode
     if debug == "data":
          print("fileExists: " + str(fileExists))
          print("tempPath: " + tempPath+"\session.txt")
     
def in_idle():
    try:
        return sys.stdin.__module__.startswith('idlelib') #check the processes for idle
    except AttributeError:
        return True #return tru

def debugCheck(debugID):
     global debugMode
     for i in debugMode: #for everything in the array:
        if(i == debugID) : #check if the debugID is in the array
            return(i) #return the value
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'): #if in windows
        command = 'cls'
    os.system(command)
def error(message):
    print(" ")
    print('\033[31m' + 'Error: ' + message + '\x1b[0m') #Print the message in red
    time.sleep(3)#Pause for time to read the message
def printSingleMenu(printThis):
    print ("##################################################################################################################")
    for x in range(len(printThis)): #for everything in the array print it plus its number
        print ("["+str(x)+"] "+printThis[x])
    print ("##################################################################################################################")
def printDualMenu(printThis,priceThis):
    repeat = 0
    print ("##################################################################################################################")
    for x in range(len(printThis)): #for everything in the array print it plus its number 
        priceTag = "#"+"$"+str("{:.2f}".format(priceThis[x]))+"#" #this is to make the whole output is formated with ljust
        numbering ="["+str(x)+"] "      #if it wasnt like this then we would have to calculate and add a ljust for everything in the print function
        print (numbering.ljust(5)[:5]+printThis[x].ljust(102)[:102]+priceTag.ljust(8)[:8])
        
    print ("##################################################################################################################")

def logo():
 global colour
 global randColor  
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
                                                                                                                 

    """ + '\x1b[0m')#sets it back to white
def runInIdle():
 user = 999
 logo() #Print the logo
 print("NOTE: Running in Idle can make the user experience worse (Console wont clear and ANSI colors dont work.)")
 idle_printSingleMenu = ["Continue","Exit"]
 printSingleMenu(idle_printSingleMenu) #Print printSingleMenu
 user = input (colour+" Please make a choice via number and then press enter to confirm: "+'\x1b[0m')
 if user == "0":
    print("Running In Idle")
    main()
 elif user == "1":
      print("Exiting")
      if ignoreHistory != "ignoreHistory":
       setHistory()    
       f = open("history.txt", "a")     
       f.write("Ran In Idle, Not finished"+ "\n")
       f.close()
      quit()
      quit()   
    
#MAIN FUNCTIONS
def runAgain():
 global colour
 global userOrder
 global userOrderPrice
 global amtOfFish
 clear()   
 user = 999
 allowDebug = debugCheck("DEBUG")
 logo() #Print the logo
 main_printSingleMenu = ["Take another order","Exit"]
 printSingleMenu(main_printSingleMenu) #Print printSingleMenu
 user = input (colour+" Please make a choice via number and then press enter to confirm: "+'\x1b[0m')
 if user == "0":
    print("0")
    reset() #Rest the file
    
    userOrder.clear()
    userOrderPrice.clear()
    customerData.clear()
    amtOfFish = 0 #reset the fish
    totalCost = 0.00 # zero out the price
    main()
 elif user == "1":
      print("1")
      quit()   
def finish():
 global colour
 global userOrder
 global userOrderPrice
 global totalCost
 global customerData
 clear()   
 user = 999
 logo() #Print the logo
 if len(customerData) == 0 or len(userOrder) == 0:
     error("Customer Info Not Entered")
     main()
 print("---ITEMS---")
 printDualMenu(userOrder, userOrderPrice)

 print("---TYPES---")
 if customerData[3] == "0":
  print("Order Type: "+"Delivery")
  totalCost = totalCost + 5.00
 else:
  print("Order Type: "+"Pick Up")
 if customerData[2] == "0":
  print("Order Type: "+"Frozen")
 else:
  print("Order Type: "+"Cooked")
 print ("##################################################################################################################")
 print("---CUSTOMER INFO---")
 print("Name: "+str(customerData[0]))
 print("Phonenumber: "+str(customerData[1]))
 if customerData[3] == "0":
  print("Adress: "+str(customerData[4]))
 print ("##################################################################################################################")
 print("---COST---")
 print("Price: $"+"{:.2f}".format(totalCost))
 print ("##################################################################################################################")
 setHistory()    
 f = open("history.txt", "a")     
 f.write("Finished"+ "\n")
 f.close()
 input("Press enter to continue")
 runAgain()
def fishMenu():
 global colour

 clear()   
 user = 999
 logo() #Print the logo
 item = ["Shark", "Flounder", "Cod", "Gurnet", "Jon Dory", "Gold Fish", "Snapper", "Pink Salmon", "Tuna", "Smoked Marlin", "Kahwai", "Dolphin","Scoop Of Chips","Type 'back' To Go Back"]
 price = [4.10,4.10,4.10,4.10,4.10,4.10,7.20,7.20,7.20,7.20,7.20,7.20,3.00,0.00]
 printDualMenu(item, price) #Print printDualMenu
 user = input (colour+" Please make a choice via number and then press enter to confirm: "+'\x1b[0m')   
 try:
   int(user) #trys to convert to int
   isInt = True
 except ValueError: #if it cant then return error
      isInt = False

 if isInt != False: #if it is not a error    
  if int(user) in range(0,13): 
     addToOrder(user,item,price)

 elif user == "back": #the range wont let 13 blah blah
     main()   
 else:
        error("Not an option")
        fishMenu()     
def CustomerDetails():   
 global colour
 global customerData
 global tempPath
 clear()   
 user = 999
 printData = debugCheck("data")
 logo() #Print the logo
 print ("##################################################################################################################")
 f = open(tempPath+"\session.txt", "a") #Doc used for history
 if len(customerData) != 0:
    customerData.clear() # resets the user data  
    if printData == "data":
      print("Reseting file")      
 name = input (colour+"Please enter your name: "+'\x1b[0m') #Yes i know it allows a number but thats  bc what if your named prince harry the 3rd? 
 f.write("Customer Name: "+name+"\n")
 customerData.append(name)
 if printData == "data":
      print("Got and Set Name")   
 phoneNumber = input (colour+"Please enter your phone number: "+'\x1b[0m')
 phoneisNumber = phoneNumber    
 try:
    int(phoneNumber) #trys to convert to int
    phoneisNumber = True
 except ValueError: #if it cant the return error
    phoneisNumber = False

 if phoneisNumber == False:
   error("Not an number, Re running ")
   customerData.clear() # resets the user data
   CustomerDetails()
 f.write("Customer Phone Number: "+phoneNumber+"\n")
 customerData.append(phoneNumber)
 if printData == "data":
      print("Got phone number")   
 print("")

 frozenOrCooked = ["Frozen","Cooked"]

 printSingleMenu(frozenOrCooked) #Print printSingleMenu
 pickFrozenOrCooked = input (colour+"Please choose an option: "+'\x1b[0m')
 if pickFrozenOrCooked == "0":
       f.write("Pick Frozen Or Cooked: "+pickFrozenOrCooked+"\n")
       customerData.append(pickFrozenOrCooked)
 elif pickFrozenOrCooked == "1":
        customerData.append(pickFrozenOrCooked)
        f.write("Pick Frozen Or Cooked: "+pickFrozenOrCooked+"\n")
        
 else:
   error("Not an option, Re running ")
   customerData.clear() # resets the user data
   CustomerDetails()
 print("")
 if printData == "data":
      print("Got Frozen Or Cooked number")   
 pickUpOrDelivery = ["Delivery","PickUp"]
 printSingleMenu(pickUpOrDelivery)
 pickPickUpOrDelivery = input (colour+"Please choose an option: "+'\x1b[0m')
 if pickPickUpOrDelivery == "0":
       f.write("PickUp Or Delivery: "+pickPickUpOrDelivery+"\n")
       customerData.append(pickPickUpOrDelivery)
 elif pickPickUpOrDelivery == "1":
        customerData.append(pickPickUpOrDelivery)
        f.write("PickUp Or Delivery: "+pickPickUpOrDelivery+"\n")
 else:
   error("Not an option, Re running ")
   customerData.clear() # resets the user data
   CustomerDetails()
 if printData == "data":
      print("Got Pick Up Or Delivery number")     
 if customerData[3] == "0":
  adress = input (colour+"Please enter your adress: "+'\x1b[0m')
  customerData.append(adress)
  f.write("Adress: "+adress+"\n")
 f.close()
 print("All details entered")
 time.sleep(.5)
 main()
     
def main():
 global colour
 global userOrder
 global userOrderPrice
 clear()   
 user = 999
 allowDebug = debugCheck("DEBUG")
 logo() #Print the logo
 main_printSingleMenu = ["Customer Details","Fish and Chip Orders","Finish","Cancel Current","Exit"]
 printSingleMenu(main_printSingleMenu) #Print printSingleMenu
 user = input (colour+" Please make a choice via number and then press enter to confirm: "+'\x1b[0m')
 if user == "0":
    print("0")
    CustomerDetails()
 elif user == "1":
      print("1")
      fishMenu()   
 elif user == "2":
      print("2")
      finish()
 elif user == "3":
      print("3")
      setHistory()    
      f = open("history.txt", "a")     
      f.write("Canceled, Not finished"+ "\n") #Used to know why the order was canceled in history file
      f.close()
      reset() #Rest the file
      userOrder.clear()
      userOrderPrice.clear()
      customerData.clear()
      amtOfFish = 0 #reset the fish
      totalCost = 0.00 # zero out the price
      main()
 elif user == "4":
      print("4")
      if ignoreHistory != "ignoreHistory":
       setHistory()    
       f = open("history.txt", "a")     
       f.write("Exited, Not finished"+ "\n") #Used to know why the order was canceled in history file 
       f.close()
      quit() 
 elif user == "DEBUG" and allowDebug == "DEBUG":      
      print("DEBUG MODE")
      DEBUG()    
 else:
        error("Not an option")
        main()
#DEBUG
def DEBUG():
 global colour
 global debugMode
 global customerData
 global tempPath
 global userOrder
 global userOrderPrice
 global totalCost
 clear()   
 user = 999
 userColor = 0
 logo() #Print the logo
 debug_printSingleMenu = ["Select Theme Color","Temp File Location","Print Data While running","Print User Data","Print TempFile","History","Print Total Cost","Print User Items","Exit"]
 printSingleMenu(debug_printSingleMenu) #Print printSingleMenu
 user = input ("Please make a choice via number and then press enter to confirm: ")
 if user == "0":
      
    print(str("Colors:"))
    debug_printSingleMenu = ["Black","Red","DarkGreen","DarkYellow"]
    printSingleMenu(debug_printSingleMenu) 
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
      printSingleMenu(customerData)
      time.sleep(1.5)
      DEBUG()
 elif user == "4":
      printAFile(tempPath+"\session.txt")
      time.sleep(1.5)
      DEBUG()
 elif user == "5":
      printAFile("history.txt")
      input("press enter to finish \n")
      DEBUG()
 elif user == "6":
      print(str("{:.2f}".format(totalCost)))

      input("press enter to finish \n")
      DEBUG()
 elif user == "7":
       printDualMenu(userOrder, userOrderPrice)
       input("press enter to finish \n")
       DEBUG()
 elif user == "8":
      main()
 else:
        error("Not an option")
        main()
#PROGRAM
debug = debugCheck("data") #Checks if data has been set in debug mode
ignoreHistory = debugCheck("ignoreHistory") #Checks if ignoreHistory has been set in debug mode, this is just so Im not creating loads of entrys into the file while testing
if debug == "data":
 print("Defined Functions, Set vars, Imported dependices")
 reset()
if debug == "data":
 print("Reset files")
if ignoreHistory != "ignoreHistory":
     f = open("history.txt", "a")     
     f.write("\n") # Creates a newline for a new order, this also creates the history file if its not there
     f.close() 
print ("##################################################################################################################")
f = open(tempPath+"\session.txt", "a")
f.write("----------------" + "\n") #Header the doc (used to indecate a break between sessions in the history)
f.write("Today's date:"+ today + "\n") #Used to know when the order was started 
f.close()
if debug == "data":
 print("Opened File, Set file header")        
idleCheck = "idlelib" in sys.modules # NOT PLACED IN VARIBLES BECUASE THEN in_idle() WOULD BE DEFIEND AFTER BEIGN CALLED WHICH RESULTS IN AN ERROR
idleDebug = debugCheck("idle")#SAME HERE
if debug == "data":
 print("Checked for idle and for idle debug tag")
 print("idleCheck: "+str(idleCheck))
 print("idleDebug: "+idleDebug)


if idleCheck == True: #IF it is then run the next check
        if idleDebug == "idle": #if the debug tag is set to idle then alert that it is and continue
              if debug == "data":
                print("idle debug tag set, dont show warning printSingleMenu") 
              error("Runnning in idle with debug mode")
              main()
        else: #else show the idle printSingleMenu
             if debug == "data":
               print("idle debug tag not set, showing warning")
             runInIdle()
else:
     if debug == "data":
      print("idle check returned false, running as normal")
     main()   
