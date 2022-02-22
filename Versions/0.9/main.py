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
from datetime import date

#VARIBLES
today = str(date.today()) #Get todays date
amtOfFish = 0
totalCost = 0.00
tempPath = tempfile.gettempdir() # Get the temp dir
colour = "\x1b[0m" #set the default colour
currentDir = os.getcwd()   # get where the file is 
venvExec =""
venvPipExec =""
chatBotLoc =""

randColor = ['\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m'] #the list of random color
fishs = ["Shark", "Flounder", "Cod", "Gurnet", "Jon Dory", "Gold Fish", "Snapper", "Pink Salmon", "Tuna", "Smoked Marlin", "Kahwai", "Dolphin","Scoop Of Chips"],[4.10,4.10,4.10,4.10,4.10,4.10,7.20,7.20,7.20,7.20,7.20,7.20,3.00]
fishs[0].append("Type 'back' To Go Back") #ADD THE BACK TEXT
fishs[1].append(0.00) #ADD THHE NULL PRICE FOR BACK
userOrder = [],[]
debugMode = ["venv","idle","DEBUG","chatBot"]#Start up Debug tags. TAGS:{idle: Allows debugging on idle} {DEBUG: Turns on debuging mode and allows acess to the debug menu} {Color: Tells the randomizer that color has been set in the debug menu} {data: Prints extra infomation} {ignoreHistory: dont write to the history file} (venv: sets that the virtaul enviroment has been setup so the other imports can work, this is becuse of pip)
customerData = [] #Format: ["name: the persons name","phone number","frozen(0) or cooked(1)","dlivery(0) or pick up(1)","adress (last becuase its optinal)"]
#FUNCTIONS

def fakeDetails():
 global customerData
 customerData.append("ORDER VIA BOT")
 customerData.append(123456789)
 customerData.append(1)
 customerData.append(1)
def fishNameToNumber(fishName):
     global fishs
     fish = fishs[0]
     fishNumber = 0
     for x in fish:
          fishNumber += 1
          if fishName == x:
             return fishNumber
     return("Not a fish")     
def customData(FilePath, fileArgs):
     file = open(FilePath, 'r+') #open the file
     current = 0 
     lines = file.readlines() #read the lines
     for x in lines:
         current += 1
         print(x+"line: "+"current")  #print lines (for debuging)
         
         if str(x) == str(fileArgs): #if it is the same return true
            current += 1 #add one to get the data below
            lineData = file[current] 
            print(lineData)
            return lineData  
               
     return arrayNum   
def howManyInArray(arrayName):
     arrayNum = 0
     for x in arrayName:
         arrayNum += 1
     return arrayNum   
def checkFish(fish, array):
    print("CHECKING FISH") 
    numFish = 0 #setup var
    printData = debugCheck("data")
    for x in array: 
       if x == fish: #if the current item is the same as the fish
          numFish = numFish + 1 #add 1 to current
          
    if printData == "data":     
         print("For "+str(fish)+", Amt ordered is: "+str(numFish))
    return numFish #return the amount of fish

def checkFile(FilePath, fileArgs):
     file = open(FilePath, 'r+') #open the file
     lines = file.readlines() #read the lines
     for x in lines:
         printData = debugCheck("data")
         if printData == True:
             print(x)
         if str(x) == str(fileArgs): #if it is the same return true
            return True  
def deleteLine(FilePath, fileArgs):
     with open(FilePath, "r") as f:
         lines = f.readlines()
     with open(FilePath, "w") as f:
      for line in lines:
        if line.strip("\n") != fileArgs:
            f.write(line)

def addToOrder(strItemID, amt):
     printData = debugCheck("data")
     botRun = checkFile("data.txt","InABotEmulateTrue")
    
     global userOrder
     global totalCost
     global customerData
     global fishs
     foodList  = fishs[0]
     priceList = fishs[1]
     itemID = int(strItemID)#convert to into int
     if len(customerData) == 0: #check if there is the required info
          if botRun != True:
               error("Customer Info Not Entered, running the menu") 
               CustomerDetails() #this is becuase it needs to know if the order is cooked or frozen, so it can apply the discount
          else:
             return("Customer Info not entered")  
     if botRun != True:
      amt = input (colour+" How many "+foodList[itemID] +" would you like: "+'\x1b[0m') #ask how many of the item the user would like
     try:
         int(amt) #trys to convert to int
         isInt = True
     except ValueError: #if it cant the return error
      isInt = False

     if isInt == False: #if it is a error
      if printData == "data":
       print("int returned false")
      if botRun == True:
         return("NOT AN AMOUNT")  
      else:     
       error("Not an number, Re running.") #print the error
       fishMenu() #go back to the menu
     if itemID == 12: #IF ITS chips
         print(amt)
         chipsPrice = priceList[itemID]*float(amt) #convert to int times the price by the amt
         print(chipsPrice)
         if printData == "data":
          print("set chips price")
         totalCost = totalCost + chipsPrice #add the cost
         userOrder[0].append (str(amt+" scoops of chips")) #and the amount of scoops
         userOrder[1].append(chipsPrice) #add the cost to the list
         if printData == "data":
          print("appened to list")
         if botRun != True: #this just makes sure the chatgui.py program doesnt run this
          fishMenu()#go back 
     print(" The most fish you can order is 7.") # alert the user of the max     
     for x in range(int(amt)):
       amtOfFish = checkFish(foodList[itemID], userOrder[0])    
       if amtOfFish == 7:
         if botRun != True:   
          error("Max amount for "+foodList[itemID] +" has been ordered")
          fishMenu() #go back to the menu, this prevents it from running again for the remaining number of fsih tried.
         else:
          return("Added fish until reached max fish, 7")    
       else: 
        print("Added "+foodList[itemID] +": " + str(x+1)) #this is to show the user that the item actually has been added,  add one to make it count properly bc lists idex starting at 0   
        
        totalCost = totalCost + priceList[itemID]   #add to the cost
        if printData == "data":
           print("added to vars")
        fishPrice = priceList[itemID]
        if customerData[2] == "0":
           if printData == "data":
                print("Fish type: Frozen")
           totalCost = totalCost - 1.05 #take away the discount
           fishPrice = priceList[itemID] - 1.05
        userOrder[0].append(foodList[itemID])
        userOrder[1].append(fishPrice)
        if printData == "data":
           print("appened to list")
        f = open(tempPath+"\session.txt", "a")
        f.write("Item: " + foodList[itemID] + ", Price: " + str("{:.2f}".format(fishPrice)) + "\n") #add to the doc
        f.close()
        if printData == "data":
         print("wrote to file")
     if botRun != True:    
      fishMenu() #go back to the menu
     else:
      return("Done")    
def setHistory():
     printData = debugCheck("data")
     historyDoc = open("history.txt", 'a+') #open the history doc
     tempdoc = open(tempPath+"\session.txt", 'r') #open the tempdoc
     historyDoc.write(tempdoc.read()) #write the read data from the temp doc
     historyDoc.close()
     tempdoc.close()#close them both
     if printData == "data":
      print("wrote sesson.txt to history.txt")
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
def printDualMenu(multiArray):
    printThis = multiArray[0]
    priceThis = multiArray[1]
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

#MAIN FUNCTIONS
def venv():
 global venvExec
 global venvPipExec
 global chatBotLoc
 global currentDir
 venvCheck = debugCheck("venv")#Check if virtual
 printData = debugCheck("data")
 if venvCheck == "venv":  
  f = open("venv.txt", "a")     
  f.write("") # Creates the file if not there
  f.close()
  f = open("data.txt", "a")     
  f.write("") # Creates the file if not there
  f.close()
  print("Made files")
  #CHECKING THE VENV  
  venvData = checkFile("data.txt","venvMadeTrue") #wanted to but cant use venv.txt becuase the file gets reset a lot
  if venvData == True: #if the user has made the virtual enviroment before
   if printData == "data":  
    print("VENV DATA TRUE")
   setCustomData = checkFile("data.txt","CustomEnviroment")
   if setCustomData == True:
    path = customData("data.txt","CustomEnviroment")
    print("Got custom data")
    venvExec = path+"\Scripts\python.exe"
    venvPipExec = path+"\Scripts\pip.exe"
   else:  
       venvExec = os.getcwd()+"\VIRTUAL\Scripts\python.exe"
       venvPipExec = os.getcwd()+"\VIRTUAL\Scripts\pip.exe"
   chatBotLoc = os.getcwd()+"/../ChatBot"
   pythonExists = os.path.isfile(venvExec) #Checks if python exists
   pipExists = os.path.isfile(venvPipExec) #Checks if pip exists
   if pipExists != True:
    f = open("data.txt","r+")
    f.truncate(0) #RESETS IT
    if debug == "data":
     print("Python doesnt exist, reset the venv made document")
    f.close()
   if pythonExists != True:
    f = open("data.txt","r+")
    f.truncate(0) #RESETS IT
    if debug == "data":
     print("Python doesnt exist, reset the venv made document")
    f.close() 
  elif venvData != True: #if the user has NOT made the virtual enviroment before
        print("WARNING: DO NOT CLOSE THE CURRENT WINDOW")  
        print("Installing Packages") 
        os.system("py -m venv "+currentDir+"/VIRTUAL/")
        venvExec = currentDir+"/VIRTUAL/Scripts/python.exe"
        venvPipExec = currentDir+"/VIRTUAL/Scripts/pip.exe"
        f = open("data.txt", "a")
        f.write("\nvenvMadeTrue") #write that its been started
        if debug == "data":
             print("set file")
        f.close()
        requirmenets = ["Keyboard"] #Yes i know that there is only one in the list but that is to make this script more scalable.
        for x in requirmenets:
           os.system(venvPipExec +' install '+x)   

#Starting the program
  if debug == "data":
   print(currentDir)
   print("venvExec: "+venvExec)
   print("venvPipExec: "+venvPipExec)
  programLoc = currentDir+"\main.py"
  processStarted = checkFile("venv.txt","processVenvTrue")
  if processStarted == True: #check if a cmd process with venv has started
    f = open("venv.txt","r+")
    f.truncate(0) #reset it
    if debug == "data":
     print("Reset file")
    f.close()#Clear the file, this makes sure that when closed down a new one will open next run 
    import keyboard
    print("Imported Virtual Packages")
    keyboard.press('f11') #makes it fullscreen
  elif processStarted != True:
    f = open("venv.txt", "a")
    
    f.write("processVenvTrue") #write that its been started
    if debug == "data":
     print("set file")
    f.close()
    if debug == "data":
     print("started process")
    os.system(venvExec +' '+programLoc) #start the process    
    print("FINISHED IN VIRTUAL ENV")
    quit() 
def runInIdle():
 user = 999
 logo()        #Print the logo
 print("NOTE: Running in Idle can make the user experience worse (Console wont clear and ANSI colors dont work.)")
 idle_printSingleMenu = ["Continue (RECOMENDED)","Run in idle","Exit"]
 printSingleMenu(idle_printSingleMenu) #Print printSingleMenu
 user = input (colour+" Please make a choice via number and then press enter to confirm: "+'\x1b[0m')
 if user == "0":
    print("Running In CMD")
    os.system('python main.py')
    print("Session finished")
    quit() #makes sure that when the user closes the cmd window then idle window will close aswell
 elif user == "1":
    print("Running In Idle")
    main()
 elif user == "2":
      print("Exiting")
      if ignoreHistory != "ignoreHistory":
       setHistory()    
       f = open("history.txt", "a")     
       f.write("Ran In Idle, Not finished"+ "\n")
       f.close()
      quit()
 else:
    error("Not AN Option, defaulting to option 0")  
    print("Running In CMD")
    os.system('python main.py')
    print("Session finished")
    quit()
     
def runAgain():
 printData = debugCheck("data")    
 global colour
 global userOrder
 global amtOfFish
 global totalCost
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
    if printData == "data":
      print("Reset the file") 
    #clear the lists
    userOrder[0].clear()
    userOrder[1].clear()
    customerData.clear()
    if printData == "data":
      print("reset the array/lists")
    amtOfFish = 0 #reset the fish
    totalCost = 0.00 # zero out the price
    if printData == "data":
      print("cleared the vars")
    main()
 elif user == "1":
      print("1")
      quit()
 else:
     error("Not a option")
     runAgain()
def finish():
 printData = debugCheck("data")
 global colour
 global userOrder
 global totalCost
 global customerData
 clear()   
 user = 999
 logo() #Print the logo
 if len(customerData) == 0 or len(userOrder) == 0: #check if there is the required info 
     error("Customer Info Not Entered")
     main()
 if printData == "data":
      print("Checked customer info")    
 print("---ITEMS---")
 printDualMenu(userOrder)#print the user  listss

 print("---TYPES---")
 if customerData[3] == "0": #if its delivery
  print("Order Type: "+"Delivery")
  totalCost = totalCost + 5.00 #add the delivery charge
  if printData == "data":
      print("Added dilivery charge")
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
  if printData == "data":
      print("IS dilivery so printing adress")    
  print("Adress: "+str(customerData[4]))
  
 print ("##################################################################################################################")
 print("---COST---")
 print("Price: $"+"{:.2f}".format(totalCost)) #format the cost becuase python does maths wrong with memory errors so it  will look like 41.0000000000006 instead og 41.00
 print ("##################################################################################################################")
 setHistory()    
 f = open("history.txt", "a")     
 f.write("Finished"+ "\n")
 f.close()
 if printData == "data":
      print("Write to doc")
 input("Press enter to continue \n")
 runAgain()
def fishMenu():
 global colour
 printData = debugCheck("data")
 clear()   
 user = 999
 logo() #Print the logo
 global fishs

 printDualMenu(fishs) #Print printDualMenu
 user = input (colour+" Please make a choice via number and then press enter to confirm: "+'\x1b[0m')   
 try:
   int(user) #trys to convert to int
   isInt = True
   if printData == "data":
      print("Input is an int") 
 except ValueError: #if it cant then return error
      isInt = False
      
 if isInt != False: #if it is not a error
  fishRange = howManyInArray(fishs[0])
  fishRange -= 1
  if int(user) in range(fishRange): 
     addToOrder(user, 0)
  else: #if it is an int but not in the range then return an error
        error("Not an option")
        fishMenu()  
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

 clear()   
 user = 999
 allowDebug = debugCheck("DEBUG")
 logo() #Print the logo
 main_printSingleMenu = ["Customer Details","Fish and Chip Orders","Finish","Cancel Current"]
 main_printSingleMenu.append("Exit")
 exit1 = howManyInArray(main_printSingleMenu)  #get its place for the input
 exit1 = exit1 - 1 #take away 1 becuase the array starts at 0 but the counter starts at 1
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
      userOrder[0].clear()
      userOrder[1].clear()
      customerData.clear()
      amtOfFish = 0 #reset the fish
      totalCost = 0.00 # zero out the price
      main()
 elif user == str(exit1):
      print(exit1)
      print(user)
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
 global totalCost
 global venvExec
 global venvPipExec
 global chatBotLoc
 clear()   
 user = 999
 userColor = 0
 
 logo() #Print the logo
 debug_printSingleMenu = ["Select Theme Color","Temp File Location","Print Data While running","Print User Data","Print TempFile","History","Print Total Cost","Print User Items","Add a debug tag","Print debug tags","Get current dir"]
 venvCheck = debugCheck("venv")#Check if virtual
 if venvCheck == "venv":
  
   debug_printSingleMenu.append("Install a python package")#Add venv required options
   venvOp1 = howManyInArray(debug_printSingleMenu)  #check how many in array, this is used later
   venvOp1 = venvOp1 - 1
   debug_printSingleMenu.append("Execute a python file in a venv")
   venvOp2 = howManyInArray(debug_printSingleMenu)  #check how many in array, this is used later
   venvOp2 = venvOp2 - 1
 chatBotCheck = debugCheck("chatBot")  
 if chatBotCheck == "chatBot":
  
   debug_printSingleMenu.append("Run the bot")#Add venv required options
   chatBotOp1 = howManyInArray(debug_printSingleMenu)  #check how many in array, this is used later
   chatBotOp1 = chatBotOp1 - 1
   debug_printSingleMenu.append("Train the bot")
   chatBotOp2 = howManyInArray(debug_printSingleMenu)  #check how many in array, this is used later
   chatBotOp2 = chatBotOp2 - 1
   debug_printSingleMenu.append("Add bot data")
   chatBotOp3 = howManyInArray(debug_printSingleMenu)  #check how many in array, this is used later
   chatBotOp3 = chatBotOp3 - 1
   debug_printSingleMenu.append("Install required packages")
   chatBotOp4 = howManyInArray(debug_printSingleMenu)  #check how many in array, this is used later
   chatBotOp4 = chatBotOp4 - 1  
 debug_printSingleMenu.append("Exit") #Add exit so its always last
 exit1 = howManyInArray(debug_printSingleMenu)  #get its place for the input
 exit1 = exit1 - 1 
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
       printDualMenu(userOrder)
       input("press enter to finish \n")
       DEBUG()
 elif user == "8":   
     tag = input("Tag name:")
     debugMode.append(tag) 
     DEBUG()
 elif user == "9":   
     printSingleMenu(debugMode)
     input("press enter to finish \n")
     DEBUG()  
 elif user == "10":   
     print(os.getcwd())
     time.sleep(1.5)
     DEBUG()      
 elif venvCheck == "venv" and user == str(venvOp1):
      package = input("Package name: ")
      os.system(venvPipExec +' install '+package)
      DEBUG()
 elif venvCheck == "venv" and user == str(venvOp2):
      programLoc = input("Program location: ")
      os.system(venvExec +' '+programLoc)     
      DEBUG()
 elif chatBotCheck == "chatBot" and user == str(chatBotOp1):
      f = open("data.txt", "a")
      f.write("\n") 
      f.write("InABotEmulateTrue") 
      f.close()     
      os.system(venvExec +' '+chatBotLoc+"/chatgui.py")
     
      time.sleep(1)
      deleteLine("data.txt", "InABotEmulateTrue")
      DEBUG()
      
 elif chatBotCheck == "chatBot" and user == str(chatBotOp2):
      os.system(venvExec +' '+chatBotLoc+"/train_chatbot.py")
      time.sleep(3)
      DEBUG()
 elif chatBotCheck == "chatBot" and user == str(chatBotOp3):
      os.system(venvExec +' '+chatBotLoc+"/intents.py")
      time.sleep(1)
      DEBUG()
      DEBUG()
 elif chatBotCheck == "chatBot" and user == str(chatBotOp4):
      print("DONT CLOSE ANY WINDOWS")
      time.sleep(1)
      requirmenets = ["numPy","Flask","nltk","tensorflow"] #these arent installed in main startup becuase they can be big and are optional 
      for x in requirmenets:
           os.system(venvPipExec +' install '+x)   
      DEBUG()     
 elif user == str(exit1):
      main()     
 else:
        error("Not an option")
        main()
#PROGRAM
botRun = checkFile("data.txt","InABotEmulateTrue")
if botRun != True:
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
     venv()  
     if idleCheck == True: #IF it is then run the next check
             if idleDebug == "idle": #if the debug tag is set to idle then alert that it is and continue
                   if debug == "data":
                     print("idle debug tag set, dont show warning menu") 
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
