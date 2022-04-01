# FREDDYS FAST FISH BY MAX TYSON FOR YR 12DGT PYTHON
# RUN ON CMD (NOT IDLE) FOR BEST EXPERIENCE
# VERSION CONTROL AT https://github.com/maxtyson123/12_DGT_PYTHON/

# VER 61


# DEPENDICES
import os
import os.path
import sys
import time
import random
import tempfile
import tkinter as tk
from datetime import date

# VARIBLES
today = str(date.today())  # Get todays date
amt_of_fish = 0
total_cost = 0.00
temp_path = tempfile.gettempdir()  # Get the temp dir
colour = "\x1b[0m"  # set the default colour
current_dir = os.getcwd()  # get where the file is
venv_exec = ""
venv_pip_exec = ""
chat_bot_loc = ""

fishs = [
    "Shark",
    "Flounder",
    "Cod",
    "Gurnet",
    "Jon Dory",
    "Gold Fish",
    "Snapper",
    "Pink Salmon",
    "Tuna",
    "Smoked Marlin",
    "Kahwai",
    "Dolphin",
    "Scoop Of Chips",
],[
    4.10, 
    4.10, 
    4.10,
    4.10,
    4.10, 
    4.10,
    7.20,
    7.20,
    7.20,
    7.20,
    7.20,
    7.20,
    3.00
]
fishs[0].append("Type 'back' To Go Back")  # ADD THE BACK TEXT
fishs[1].append(0.00)  # ADD THHE NULL PRICE FOR BACK
user_order = [], []
debug_mode = [
    "debug"
]  # Start up debug tags. TAGS:{idle: Allows debugging on idle} {debug: Turns on debuging mode and allows acess to the debug menu} {Color: Tells the randomizer that color has been set in the debug menu} {data: Prints extra infomation} {ignore_history: dont write to the history file} (venv: sets that the virtaul enviroment has been setup so the other imports can work, this is becuse of pip, ver 69 onwards there are errors)
customer_data = [
    "DEFAULT",
    "PHONENUMBER",
    "FROZEN/COOKED",
    "DELIVERY",
    "N/A",
]  # Format: ["name: the persons name","phone number","frozen(0) or cooked(1)","dlivery(0) or pick up(1)","adress (last becuase its optinal)"]

# FUNCTIONS
def find_user_data(file_path, name):
    line_num = []
    file = open(file_path, "r+")  # open the file
    lines = file.readlines()  # read the lines
    current = 0  # reset counter 1
    for x in lines:
        current += 1
        if name in x:
            line_num.append(current)
    return line_num


def delete_portion(file_path, start_line, end_line):

    file = open(file_path, "r+")  # open the file (read)
    lines = file.readlines()  # store as lines
    file = open(file_path, "w+")  # open the file (write)
    for number, line in enumerate(lines):  # convert lines to number
        if number not in range(
            start_line, end_line
        ):  # if its not in the selected range then print as normal
            file.write(line)
        else:
            file.write("Data DELETED \n")  # if is then write data deleted
    file.close()  # close the file


def read_portion(file_path, start_line, end_line):
    file = open(file_path, "r+")  # open the file (read)
    lines = file.readlines()  # store as lines
    for number, line in enumerate(lines):  # convert lines to number
        try:
            if number in range(
                start_line, end_line
            ):  # if its not in the selected range then print as normal
                print(line)
        except:
            return
    file.close()  # close the file


def get_end_line(file_path, start_line, end_indicator):
    file = open(file_path, "r+")  # open the file
    current = 0  # reset counter 1
    current2 = 0  # same with 2
    lines = file.readlines()  # read the lines
    begin_counter_2 = False  # counter state
    for x in lines:
        current += 1
        if int(current) == int(
            start_line
        ):  # if the current line is same as the one specified
            current2 = current  # update second counter to the started
            begin_counter_2 = True  # set that the start line has been found
        elif (
            begin_counter_2 == True
        ):  # this is so that it will find the relvent end tag rathern then first one it finds
            current2 += 1  # star coutning
            if end_indicator in x:  # now if it finds the end tag
                return current2  # return the value


def check_two_lines(file_path, file_args_1, file_args_2):
    file = open(file_path, "r+")  # open the file
    current = 0
    lines = file.readlines()  # read the lines
    for x in lines:
        current += 1
        if file_args_1 in x and file_args_2 in x:  # if both strings are on one line

            return current  # return counter
    return False


def fake_details():  # used to skip menus when debug
    
    customer_data[0] = "ORDER VIA BOT"  # fake name
    customer_data[1] = "123456789"  # fake phone numer
    customer_data[2] = 1  # cooked
    customer_data[3] = 1  # pick up


def fish_name_to_number(fish_name):  # not used, but was going to be
    
    fish = fishs[0]
    fish_number = 0
    for x in fish:  # for everything
        fish_number += 1  # count + 1
        if fish_name == x:
            return fish_number  # return fish number
    return "Not a fish"


def custom_data(file_path, file_args):
    file = open(file_path, "r+")  # open the file
    current = 0
    lines = file.readlines()  # read the lines
    for x in lines:
        current += 1
        print(x + "line: " + "current")  # print lines (for debuging)

        if str(x) == str(file_args):  # if it is the same return true
            current += 1  # add one to get the data below
            lineData = file[current]
            print(lineData)
            return lineData
    





def check_fish(fish, array):

    num_fish = 0  # setup var
    print_data = debug_check("data")
    for x in array:
        if x == fish:  # if the current item is the same as the fish
            num_fish = num_fish + 1  # add 1 to current
    if print_data == "data":
        print("For " + str(fish) + ", Amt ordered is: " + str(num_fish))
    return num_fish  # return the amount of fish


def check_file(file_path, file_args):
    file = open(file_path, "r+")  # open the file
    lines = file.readlines()  # read the lines
    for x in lines:
        print_data = debug_check("data")
        if print_data == True:
            print(x)
        if str(x) == str(file_args):  # if it is the same return true
            return True


def delete_line(file_path, file_args):
    f = open(file_path, "r")  # open in read mode
    lines = f.readlines()
    f = open(file_path, "w")  # open in write mode
    for line in lines:
        if line.strip("\n") != file_args:
            f.write(line)


def add_to_order(stritem_id, amt):
    print_data = debug_check("data")
    bot_run = check_file("data.txt", "InABotEmulateTrue")
    
    global total_cost
    
    
    food_list = fishs[0]
    priceList = fishs[1]
    item_id = int(stritem_id)  # convert to into int
    chip_counter = 0  # makes the menu more flexible, can now add fish items to any spot in the array
    for x in food_list:
        chip_counter += 1
        if x == "Scoop Of Chips":
            chip_counter -= 1
            chip_id = chip_counter
    if customer_data[0] == "DEFAULT":  # check if there is the required info
        if bot_run != True:
            error("Customer Info Not Entered, running the menu")
            customer_details(
                "run"
            )  # this is becuase it needs to know if the order is cooked or frozen, so it can apply the discount
        else:
            return "Customer Info not entered"
    if bot_run != True:
        amt_of_fish = check_fish(food_list[item_id], user_order[0])
        if (
            item_id != chip_id
        ):  # if the program isnt adding chips, show tha max amount of fish and how many the user has ordered
            print(
                " You have ordered: "
                + str(amt_of_fish)
                + " "
                + food_list[item_id]
                + ", the most you can order is 7."
            )  # alert the user of the max
        amt = input(
            colour + " How many " + food_list[item_id] + " would you like: " + "\x1b[0m"
        )  # ask how many of the item the user would like
    try:
        int(amt)  # trys to convert to int
        is_int = True
    except ValueError:  # if it cant the return error
        is_int = False
    if is_int == False:  # if it is a error
        if print_data == "data":
            print("int returned false")
        if bot_run == True:
            return "NOT AN AMOUNT"
        else:
            error("Not an number, Re running.")  # print the error
            fish_menu()  # go back to the menu
    if item_id == chip_id:  # IF ITS chips
        print(amt)
        chipsPrice = priceList[item_id] * float(
            amt
        )  # convert to int times the price by the amt
        print(chipsPrice)
        if print_data == "data":
            print("set chips price")
        total_cost = total_cost + chipsPrice  # add the cost
        user_order[0].append(str(amt + " scoops of chips"))  # and the amount of scoops
        user_order[1].append(chipsPrice)  # add the cost to the list
        if print_data == "data":
            print("appened to list")
        if (
            bot_run != True
        ):  # this just makes sure the chatgui.py program doesnt run this
            fish_menu()  # go back
    for x in range(int(amt)):
        amt_of_fish = check_fish(food_list[item_id], user_order[0])
        if amt_of_fish == 7:
            if bot_run != True:
                error("Max amount for " + food_list[item_id] + " has been ordered")
                fish_menu()  # go back to the menu, this prevents it from running again for the remaining number of fsih tried.
            else:
                return "Added fish until reached max fish, 7"
        else:
            print(
                "Added " + food_list[item_id] + ": " + str(x + 1)
            )  # this is to show the user that the item actually has been added,  add one to make it count properly bc lists idex starting at 0

            total_cost = total_cost + priceList[item_id]  # add to the cost
            if print_data == "data":
                print("added to vars")
            fishPrice = priceList[item_id]
            if customer_data[2] == "0":
                if print_data == "data":
                    print("Fish type: Frozen")
                total_cost = total_cost - 1.05  # take away the discount
                fishPrice = priceList[item_id] - 1.05
                user_order[0].append(food_list[item_id])
            else:
                user_order[0].append(food_list[item_id])
            user_order[1].append(fishPrice)
            if print_data == "data":
                print("appened to list")
            f = open(temp_path + "\session.txt", "a")
            f.write(
                "Item: "
                + food_list[item_id]
                + ", Price: "
                + str("{:.2f}".format(fishPrice))
                + "\n"
            )  # add to the doc
            f.close()
            if print_data == "data":
                print("wrote to file")
    if bot_run != True:
        fish_menu()  # go back to the menu
    else:
        return "Done"


def set_history():
    print_data = debug_check("data")
    history_doc = open("history.txt", "a+")  # open the history doc
    tempdoc = open(temp_path + "\session.txt", "r")  # open the tempdoc
    history_doc.write(tempdoc.read())  # write the read data from the temp doc
    history_doc.close()
    tempdoc.close()  # close them both
    if print_data == "data":
        print("wrote sesson.txt to history.txt")


def print_a_file(file_path):
    file = open(file_path, "r").read()  # open the file in readmode
    print(file)  # print the file


def reset():
    global user_order
    global customer_data
    global total_cost
    file_exists = os.path.isfile(temp_path + "\session.txt")  # Check if it exists
    if (
        file_exists == True
    ):  # if it doesnt exist no need to clear it becuase it will be created later on
        f = open(temp_path + "\session.txt", "r+")
        f.truncate(0)  # reset it
        f.close()
    debug = debug_check("data")  # Checks if color has been set in debug mode
    print_data = debug_check("data")  # Checks if color has been set in debug mode
    if debug == "data":
        print("file_exists: " + str(file_exists))
        print("temp_path: " + temp_path + "\session.txt")
    f = open(temp_path + "\session.txt", "a")
    f.write(
        "----------------"
    )  # Header the doc (used to indecate a break between sessions in the history)
    f.write("\n")
    f.write("Today's date:" + today + "\n")  # Used to know when the order was started
    f.close()
    user_order[0].clear()
    user_order[1].clear()
    customer_data = [
        "DEFAULT",
        "PHONENUMBER",
        "FROZEN/COOKED",
        "DELIVERY",
        "N/A",
    ]  # set the default customer info
    if print_data == "data":
        print("reset the array/lists")
    amt_of_fish = 0  # reset the fish
    total_cost = 0.00  # zero out the price
    if print_data == "data":
        print("cleared the vars")


def in_idle():
    try:
        return sys.stdin.__module__.startswith(
            "idlelib"
        )  # check the processes for idle
    except AttributeError:
        return True  # return true


def debug_check(debug_id):
    global debug_mode
    for i in debug_mode:  # for everything in the array:
        if i == debug_id:  # check if the debug_id is in the array
            return i  # return the value


def clear():
    command = "clear"
    if os.name in ("nt", "dos"):  # if in windows
        command = "cls"
    os.system(command)


def error(message):
    print(" ")
    print("\033[31m" + "Error: " + message + "\x1b[0m")  # Print the message in red
    time.sleep(3)  # Pause for time to read the message


def print_single_menu(print_this):
    print(
        "##################################################################################################################"
    )
    for x in range(
        len(print_this)
    ):  # for everything in the array print it plus its number
        print("[" + str(x) + "] " + print_this[x])
    print(
        "##################################################################################################################"
    )


def print_dual_menu(multi_array):
    print_this = multi_array[0]
    price_this = multi_array[1]
    print(
        "##################################################################################################################"
    )
    for x in range(
        len(print_this)
    ):  # for everything in the array print it plus its number
        price = str("{:.2f}".format(price_this[x]))
        price_tag = (
            "#" + "$" + price.ljust(4)[:4] + "#"
        )  # this is to make the whole output is formated with ljust
        numbering = (
            "[" + str(x) + "] "
        )  # if it wasnt like this then we would have to calculate and add a ljust for everything in the print function
        print(
            numbering.ljust(8)[:8] + print_this[x].ljust(99)[:99] + price_tag.ljust(8)[:8]
        )
    print(
        "##################################################################################################################"
    )


def logo():
    
    
    rand_color = [
        "\033[32m",
        "\033[33m",
        "\033[34m",
        "\033[35m",
        "\033[36m",
        "\033[37m",
    ]  # the list of random colors
    debug = debug_check("Color")  # Checks if color has been set in debug mode
    if debug != ("Color"):  # if it isnt then run the randomizer
        colour = random.choice(
            rand_color
        )  # this stops the randomizer running even if you have set a colur
    print(
        ""
        + colour
        + """
    
 _____  ____     ___  ___    ___    __ __  __  _____     _____   ____  _____ ______      _____  ____ _____ __ __ 
|     ||    \   /  _]|   \  |   \  |  |  ||  |/ ___/    |     | /    |/ ___/|      |    |     ||    / ___/|  |  |
|   __||  D  ) /  [_ |    \ |    \ |  |  ||_ (   \_     |   __||  o  (   \_ |      |    |   __| |  (   \_ |  |  |
|  |_  |    / |    _]|  D  ||  D  ||  ~  |  \|\__  |    |  |_  |     |\__  ||_|  |_|    |  |_   |  |\__  ||  _  |
|   _] |    \ |   [_ |     ||     ||___, |    /  \ |    |   _] |  _  |/  \ |  |  |      |   _]  |  |/  \ ||  |  |
|  |   |  .  \|     ||     ||     ||     |    \    |    |  |   |  |  |\    |  |  |      |  |    |  |\    ||  |  |
|__|   |__|\_||_____||_____||_____||____/      \___|    |__|   |__|__| \___|  |__|      |__|   |____|\___||__|__|
                                                                                                                 

    """
        + "\x1b[0m"
    )  # sets it back to white


# MAIN FUNCTIONS
def venv():
    
    
    
    
    venv_check = debug_check("venv")  # Check if virtual
    print_data = debug_check("data")
    if venv_check == "venv":
        f = open("venv.txt", "a")
        f.write("")  # Creates the file if not there
        f.close()
        f = open("data.txt", "a")
        f.write("")  # Creates the file if not there
        f.close()
        print("Made files")
        # CHECKING THE VENV
        venv_data = check_file(
            "data.txt", "venvMadeTrue"
        ) 
        if venv_data == True:  # if the user has made the virtual enviroment before
            if print_data == "data":
                print("VENV DATA TRUE")
            set_custom_data = check_file("data.txt", "CustomEnviroment")
            if set_custom_data == True:
                path = custom_data("data.txt", "CustomEnviroment")
                print("Got custom data")
                venv_exec = path + "\Scripts\python.exe"
                venv_pip_exec = path + "\Scripts\pip.exe"
            else:
                venv_exec = os.getcwd() + "\VIRTUAL\Scripts\python.exe"
                venv_pip_exec = os.getcwd() + "\VIRTUAL\Scripts\pip.exe"
            chat_bot_loc = os.getcwd() + "/../ChatBot"
            python_exists = os.path.isfile(venv_exec)  # Checks if python exists
            pip_exists = os.path.isfile(venv_pip_exec)  # Checks if pip exists
            if pip_exists != True:
                f = open("data.txt", "r+")
                f.truncate(0)  # RESETS IT
                if debug == "data":
                    print("Python doesnt exist, reset the venv made document")
                f.close()
            if python_exists != True:
                f = open("data.txt", "r+")
                f.truncate(0)  # RESETS IT
                if debug == "data":
                    print("Python doesnt exist, reset the venv made document")
                f.close()
        elif venv_data != True:  # if the user has NOT made the virtual enviroment before
            print("WARNING: DO NOT CLOSE THE CURRENT WINDOW")
            print("Installing Packages")
            os.system("py -m venv " + current_dir + "/VIRTUAL/")
            venv_exec = current_dir + "/VIRTUAL/Scripts/python.exe"
            venv_pip_exec = current_dir + "/VIRTUAL/Scripts/pip.exe"
            f = open("data.txt", "a")
            f.write("\n")
            f.write("venvMadeTrue")  # write that its been started
            if debug == "data":
                print("set file")
            f.close()
            requirmenets = [
                "Keyboard"
            ]  # Yes i know that there is only one in the list but that is to make this script more scalable.
            for x in requirmenets:
                os.system(venv_pip_exec + " install " + x)
        # Starting the program
        if debug == "data":
            print(current_dir)
            print("venv_exec: " + venv_exec)
            print("venv_pip_exec: " + venv_pip_exec)
        program_loc = current_dir + "\main.py"
        process_started = check_file("venv.txt", "processVenvTrue")
        if process_started == True:  # check if a cmd process with venv has started
            f = open("venv.txt", "r+")
            f.truncate(0)  # reset it
            if debug == "data":
                print("Reset file")
            f.close()  # Clear the file, this makes sure that when closed down a new one will open next run
            import keyboard

            print("Imported Virtual Packages")
            keyboard.press("f11")  # makes it fullscreen
        elif process_started != True:
            f = open("venv.txt", "a")

            f.write("processVenvTrue")  # write that its been started
            if debug == "data":
                print("set file")
            f.close()
            if debug == "data":
                print("started process")
            os.system(venv_exec + " " + program_loc)  # start the process
            print("FINISHED IN VIRTUAL ENV")
            if ignore_history != "ignore_history":
                set_history()
                f = open("history.txt", "a")
                f.write(
                    "Ran in virtual enviroment" + "\n"
                )  # Used to know why the order was canceled in history file
                f.close()
            quit()


def remove_item():
    clear()
    
    global total_cost
    order = []  # Setup the duplcate array
    back_id = len(user_order[0])  # count where the "back" string is placed
    back = {"b", "back", "bk", "bck", "backk", "bcak"}  # multiple ways of saying "back"
    back.add(str(back_id))  # add the back Id
    if (
        back_id == 0
    ):  # if there is nothing in the user order array then there is nothing to remove
        main()  # go back to the menu
    for x in user_order[0]:
        order.append(x)  # add everything from the order to the duplicate array
    order.append(
        "Type 'back' To Go Back"
    )  # add back text to duplicate array, this way "back" text is not added to their order
    user = 999
    logo()  # Print the logo
    print_single_menu(order)  # Print print_single_menu
    user = input(
        colour
        + " Please make a choice via number and then press enter to confirm: "
        + "\x1b[0m"
    )
    for x in back:
        user = (
            user.lower()
        )  # make the input lowercase, this makes less combinations of "back"
        if user == x:
            user = "back"  # correct the input to back
    try:
        int(user)  # trys to convert to int
        is_int = True
    except ValueError:  # if it cant then return error
        is_int = False
    if is_int != False:  # if it is not a error
        orderRange = len(order)
        if int(user) in range(orderRange):
            del user_order[0][int(user)]  # Delete the item from their order
            total_cost -= user_order[1][
                int(user)
            ]  # Take away the price from the total cost
            del user_order[1][int(user)]  # delete the cost from their order
            remove_item()
        else:  # if it is an int but not in the range then return an error
            error("Not an option")
            remove_item()
    elif user == "back":
        main()
    else:
        error("'" + user + "' is not a option")
        remove_item()


def run_in_idle():
    user = 999
    logo()  # Print the logo
    print(
        "NOTE: Running in Idle can make the user experience worse (Console wont clear and ANSI colors dont work.)"
    )
    idle_print_single_menu = ["Continue (RECOMENDED)", "Run in idle", "Exit"]
    print_single_menu(idle_print_single_menu)  # Print print_single_menu
    user = input(
        colour
        + " Please make a choice via number and then press enter to confirm: "
        + "\x1b[0m"
    )
    if user == "0":
        print("Running In CMD")
        os.system("python main.py")
        print("Session finished")
        if ignore_history != "ignore_history":
            set_history()
            f = open("history.txt", "a")
            f.write(
                "Ran in CMD via Idle" + "\n"
            )  # Used to know why the order was canceled in history file
            f.close()
        quit()  # makes sure that when the user closes the cmd window then idle window will close aswell
    elif user == "1":
        error(
            "IF YOU RUN IN IDLE, PLEASE EXIT USING THE OPTIONS ON THE SCRIPT, OTHERWISE HISTORY CAN BE MESSED UP"
        )
        main()
    elif user == "2":
        print("Exiting")
        if ignore_history != "ignore_history":
            set_history()
            f = open("history.txt", "a")
            f.write("Ran In Idle, Not finished" + "\n")
            f.close()
        quit()
    else:
        error("Not AN Option, defaulting to option 0")
        print("Running In CMD")
        os.system("python main.py")
        print("Session finished")
        if ignore_history != "ignore_history":
            set_history()
            f = open("history.txt", "a")
            f.write(
                "Exited, Not finished" + "\n"
            )  # Used to know why the order was canceled in history file
            f.close()
        quit()


def run_again():
    print_data = debug_check("data")
    
    
    
    global total_cost
    clear()
    user = 999
    allowdebug = debug_check("debug")
    logo()  # Print the logo
    main_print_single_menu = ["Take another order", "Exit"]
    print_single_menu(main_print_single_menu)  # Print print_single_menu
    user = input(
        colour
        + " Please make a choice via number and then press enter to confirm: "
        + "\x1b[0m"
    )
    if user == "0":
        reset()
        main()
    elif user == "1":
        print("1")

        quit()
    else:
        error(user + " is not a option")
        run_again()


def finish():
    print_data = debug_check("data")
    global total_cost
    clear()
    user = 999
    logo()  # Print the logo
    if (
        customer_data[0] == "DEFAULT" or len(user_order[0]) == 0
    ):  # check if there is the required info
        error("Customer Info Not Entered")
        main()
    if print_data == "data":
        print("Checked customer info")
    print(colour + "---ITEMS---" + "\x1b[0m")
    print_dual_menu(user_order)  # print the user  listss

    print(colour + "---TYPES---" + "\x1b[0m")
    if customer_data[3] == "0":  # if its delivery
        print("Order Type: " + "Delivery")
        total_cost = total_cost + 5.00  # add the delivery charge
        if print_data == "data":
            print("Added dilivery charge")
    else:
        print("Order Type: " + "Pick Up")
    if customer_data[2] == "0":
        print("Order Type: " + "Frozen")
    else:
        print("Order Type: " + "Cooked")
    print(
        "##################################################################################################################"
    )
    print(colour + "---CUSTOMER INFO---" + "\x1b[0m")
    print("Name: " + str(customer_data[0]))
    print("Phonenumber: " + str(customer_data[1]))
    if customer_data[3] == "0":
        if print_data == "data":
            print("IS dilivery so printing adress")
        print("Adress: " + str(customer_data[4]))
    print(
        "##################################################################################################################"
    )
    print(colour + "---COST---" + "\x1b[0m")
    print(
        "Price: $" + "{:.2f}".format(total_cost)
    )  # format the cost becuase python does maths wrong with memory errors so it  will look like 41.0000000000006 instead og 41.00
    print(
        "##################################################################################################################"
    )
    set_history()
    f = open("history.txt", "a")
    f.write("Finished" + "\n")
    f.close()
    if print_data == "data":
        print("Write to doc")
    input("Press enter to continue \n")
    run_again()


def fish_menu():
    
    
    print_data = debug_check("data")
    clear()
    user = 999
    fishRange = len(fishs[0])
    fishRange -= 1
    back = {"b", "back", "bk", "bck", "backk", "bcak"}
    back.add(str(fishRange))
    logo()  # Print the logo

    print_dual_menu(fishs)  # Print print_dual_menu
    user = input(
        colour
        + " Please make a choice via number and then press enter to confirm: "
        + "\x1b[0m"
    )
    for x in back:
        user = user.lower()
        if user == x:
            user = "back"
            break
    try:
        int(user)  # trys to convert to int
        is_int = True
        if print_data == "data":
            print("Input is an int")
    except ValueError:  # if it cant then return error
        is_int = False
    if is_int != False:  # if it is not a error

        if int(user) in range(fishRange):
            add_to_order(user, 0)
        else:  # if it is an int but not in the range then return an error
            error("Not an option")
            fish_menu()
    elif user == "back":  # the range wont let 13 blah blah
        main()
    else:
        error("'" + user + "' is not a option")
        fish_menu()


def edit_details():
    clear()
    
    userData = []
    froz = 0
    current = 0
    for x in customer_data:
        
        if x == "0" and current != 0:
            if froz == 0:
                userData.append("Type: Frozen")
                froz = 1
            else:
                userData.append("Type: Delivery")
        elif x == "1"  and current != 0:
            if froz == 0:
                userData.append("Type: Cooked")
                froz = 1
            else:
                userData.append("Type: PickUp")
        elif x == "N/A"  and current == 4:
            print("")
        else:
            userData.append(str(x))
        current += 1

    userData.append("Type 'back' To Go Back")
    back_id = len(userData)
    back_id -= 1
    back = {"b", "back", "bk", "bck", "backk", "bcak"}
    back.add(str(back_id))
    user = 999
    logo()  # Print the logo
    print_single_menu(userData)  # Print print_single_menu
    print(" WHAT INFO DO YOU WANT TO EDIT?")
    user = input(
        colour
        + " Please make a choice via number and then press enter to confirm: "
        + "\x1b[0m"
    )
    for x in back:
        user = user.lower()
        if user == x:
            user = "back"
            break
    try:
        int(user)  # trys to convert to int
        is_int = True
    except ValueError:  # if it cant then return error
        is_int = False
    if is_int != False:  # if it is not a error
        orderRange = len(customer_data)
        if int(user) in range(orderRange):
            customer_details(int(user))  # edit the relevate spot using the correct mode
            customer_details("run")
        else:  # if it is an int but not in the range then return an error
            error("Not an option")
            customer_details("run")
    elif user == "back":
        customer_details("edited")  # write the new changes to the  file
        main()
    else:
        error("'" + user + "' is not a option")
        customer_details("run")


def customer_details(mode):
    
    
    

    user = 999
    adress = "N/A"
    print_data = debug_check("data")

    f = open(temp_path + "\session.txt", "a")  # Doc used for history
    if mode == "run":
        clear()
        logo()  # Print the logo
        if customer_data[0] != "DEFAULT":
            edit_details()
            if print_data == "data":
                print("CUSTOMER EDITING DATA")
        print(
            "##################################################################################################################"
        )
        customer_details(0)  # set the name
        customer_details(1)  # set the number
        customer_details(2)  # set the frozen/cooked
        customer_details(3)  # set the dilivery
        customer_details("file")  # set the file
        print("All details entered")
        time.sleep(0.5)
        main()
    elif mode == 0:
        name = input(
            colour + "Please enter your name: " + "\x1b[0m"
        )  # Name allows numbers becuase of people who may be named like Prince Harray the 3rd
        if name == "DEFAULT":
            name = name+" " #add a space, this way the system knows that is not the default data and to the human eye it is fine
        customer_data[0] = name  # replace the name
        return
    elif mode == 1:
        phoneNumber = input(
            colour + "Please enter your phone number: " + "\x1b[0m"
        )  # get the number
        phoneisNumber = phoneNumber  # store as duplicate
        try:
            int(phoneNumber)  # trys to convert to int
            phoneisNumber = True
        except ValueError:  # if it cant the return error
            phoneisNumber = False
        if phoneisNumber == False:
            error("'" + str(phoneNumber) + "' is not a number")
            customer_details(1)  # re-run
        customer_data[1] = (
            "+64 " + phoneNumber
        )  # store number in slot, add the +64 as the int checker doesnt allow that
        return
    elif mode == 2:
        if customer_data[2] != "FROZEN/COOKED":
            print(
                " This action will "
                + "\033[31m"
                + " RESET"
                + "\x1b[0m"
                + " your order."
            )  # aler that it will be reset
            awnser = input(" Do you wish to continue? [Y/N] : ")
            awnser = (
                awnser.lower()
            )  # make input lower case so that the program supports "Y" "y" "n" "N"
            if awnser == "y":
                reset()  # reset , reason is becuase it will mess up the pricing with the frozen discount
                customer_details("run")  # run the customer details again
            elif awnser == "n":
                return
            else:
                error("'" + str(awnser) + "' is not a option")
                return
        print_single_menu(["Frozen", "Cooked"])  # Print menu
        pickFrozenOrCooked = input(colour + "Please choose an option: " + "\x1b[0m")
        if pickFrozenOrCooked == "0" or pickFrozenOrCooked == "1":
            customer_data[2] = pickFrozenOrCooked
        else:
            error("'" + str(pickFrozenOrCooked) + "' is not a option")
            customer_details(2)
        return
    elif mode == 3:
        print_single_menu(["Delivery", "PickUp"])
        pickPickUpOrDelivery = input(colour + "Please choose an option: " + "\x1b[0m")
        if pickPickUpOrDelivery == "0" or pickPickUpOrDelivery == "1":
            customer_data[3] = pickPickUpOrDelivery
        else:
            error("'" + str(pickPickUpOrDelivery) + "' is not a option")
            customer_details(3)
        if customer_data[3] == "0":
            customer_details(4)  # if its delivery get the adress
        if customer_data[3] == "1":
            customer_data[
                4
            ] = "N/A"  # if it is not then set the adress to the default, this is for when changin from delivery to pickup
        return
    elif mode == (4):
        adress = input(colour + "Please enter your adress: " + "\x1b[0m")
        customer_data[4] = adress
        return
    elif mode == "file":
        # set all the file details
        f.write("Customer Name: " + customer_data[0] + "\n")
        f.write("Customer Phone Number: " + customer_data[1] + "\n")
        f.write("Pick Frozen Or Cooked: " + customer_data[2] + "\n")
        f.write("PickUp Or Delivery: " + customer_data[3] + "\n")
        f.write("Adress: " + customer_data[4] + "\n")
        f.close()
        return
    elif mode == "edited":
        f.write("NEW CUSTOMER DATA: \n")  # write that this is new eddited data
        f.close()
        customer_details("file")  # set the data
        return
    else:
        error("Not a mode")
        main()


def main():
    
    
    
    global total_cost
    ordercheck = user_order[0]
    clear()
    user = 999
    allowdebug = debug_check("debug")
    logo()  # Print the logo
    remv = ""
    if customer_data[0] != "DEFAULT":  # if use has entered info
        div = "##################################################################################################################"
        print(div)
        sessionData = (
            colour
            + "Customer Name: "
            + "\x1b[0m"
            + customer_data[0][:70]
            + colour
            + "   OrderCost: "
            + "\x1b[0m"
            + "$"
            + "{:.2f}".format(total_cost)
        )  # store the header
        legnth = len(div)  # count how long the divider is
        legnth -= len(sessionData)  # take away how long the session data is
        legnth = legnth / 2  # divide it by 2 to place text in the center
        print(
            " " * int(legnth) + sessionData
        )  # print 'legnth' amount of spaces before the session data
        main_print_single_menu = [
            "Edit Customer Details",
            "Fish and Chip Orders",
            "Finish",
            "Cancel Current",
        ]
    else:
        main_print_single_menu = [
            "Set Customer Details" + "\033[90m",
            "Fish and Chip Orders",
            "Finish" + "\x1b[0m",
            "Cancel Current",
        ]  # grey out the Fish and Finish options to indicate that those options are not avalible
    if len(ordercheck) != 0:
        main_print_single_menu.append("Remove an item from order")
        remv = len(main_print_single_menu)  # get its place for the input
        remv -= (
            1  # take away 1 becuase the array starts at 0 but the counter starts at 1
        )
    main_print_single_menu.append("Exit")
    exit1 = len(main_print_single_menu)  # get its place for the input
    exit1 = (
        exit1 - 1
    )  # take away 1 becuase the array starts at 0 but the counter starts at 1
    print_single_menu(main_print_single_menu)  # Print print_single_menu
    user = input(
        colour
        + " Please make a choice via number and then press enter to confirm: "
        + "\x1b[0m"
    )
    if user == "0":
        print("0")
        customer_details("run")
    elif user == "1":
        print("1")
        fish_menu()
    elif user == "2":
        print("2")
        finish()
    elif user == "3":
        print("3")
        set_history()
        f = open("history.txt", "a")
        f.write(
            "Canceled, Not finished" + "\n"
        )  # Used to know why the order was canceled in history file
        f.close()
        reset()  # Rest the file

        main()
    elif user == str(remv):
        print(remv)
        print(user)
        remove_item()
    elif user == str(exit1):
        print(exit1)
        print(user)
        if ignore_history != "ignore_history":
            set_history()
            f = open("history.txt", "a")
            f.write(
                "Exited, Not finished" + "\n"
            )  # Used to know why the order was canceled in history file
            f.close()
        quit()
    elif user == "debug" and allowdebug == "debug":
        print("debug MODE")
        debug()
    else:
        error("'" + user + "' is not a option")
        main()


# debug
def debug():
    
    global debug_mode
    
    
    
    global total_cost
    
    
    
    clear()
    user = 999
    userColor = 0

    logo()  # Print the logo
    debug_print_single_menu = [
        "Select Theme Color",
        "Temp File Location",
        "Print Data While running",
        "Print User Data",
        "Print TempFile",
        "History",
        "Print Total Cost",
        "Print User Items",
        "Add a debug tag",
        "Print debug tags",
        "Get current dir",
        "Delte user data",
        "Print user data from history",
    ]
    venv_check = debug_check("venv")  # Check if virtual
    if venv_check == "venv":

        debug_print_single_menu.append(
            "Install a python package"
        )  # Add venv required options
        venvOp1 = len(debug_print_single_menu)  # check how many in array
        venvOp1 = venvOp1 - 1
        debug_print_single_menu.append("Execute a python file in a venv")
        venvOp2 = len(debug_print_single_menu)  # check how many in array
        venvOp2 = venvOp2 - 1
    chatBotCheck = debug_check("chatBot")
    if chatBotCheck == "chatBot":

        debug_print_single_menu.append("Run the bot")  # Add venv required options
        chatBotOp1 = len(debug_print_single_menu)  # check how many in array
        chatBotOp1 = chatBotOp1 - 1
        debug_print_single_menu.append("Train the bot")
        chatBotOp2 = len(debug_print_single_menu)  # check how many in array
        chatBotOp2 = chatBotOp2 - 1
        debug_print_single_menu.append("Add bot data")
        chatBotOp3 = len(debug_print_single_menu)  # check how many in array
        chatBotOp3 = chatBotOp3 - 1
        debug_print_single_menu.append("Install required packages")
        chatBotOp4 = len(debug_print_single_menu)  # check how many in array
        chatBotOp4 = chatBotOp4 - 1
    debug_print_single_menu.append("Exit")  # Add exit so its always last
    exit1 = len(debug_print_single_menu)  # get its place for the input
    exit1 = exit1 - 1
    print_single_menu(debug_print_single_menu)  # Print print_single_menu
    user = input("Please make a choice via number and then press enter to confirm: ")
    if user == "0":

        print(str("Colors:"))
        debug_print_single_menu = ["Black", "Red", "DarkGreen", "DarkYellow"]
        print_single_menu(debug_print_single_menu)
        debugcol = input("SELECT COLOR:")
        if debugcol == "0":
            newcolour = "\033[30m"
        elif debugcol == "1":
            newcolour = "\033[31m"
        elif debugcol == "2":
            newcolour = "\033[32m"
        elif debugcol == "3":
            newcolour = "\033[33m"
        print(newcolour)
        print("EXAMPLE TEXT")  # show the debugger that it works
        print("\x1b[0m")
        colour = newcolour
        time.sleep(1)
        debug_mode.append("Color")
        debug()
    elif user == "1":
        print(tempfile.gettempdir())  # print temp dir
        time.sleep(1.5)  # give time to read
        debug()
    elif user == "2":
        debug_mode.append("data")  # append data to debug tags
        debug()
    elif user == "3":
        print_single_menu(customer_data)
        time.sleep(3)  # time to read
        debug()
    elif user == "4":
        print_a_file(temp_path + "\session.txt")
        time.sleep(1.5)
        debug()
    elif user == "5":
        print_a_file("history.txt")
        input("press enter to finish \n")
        debug()
    elif user == "6":
        print(str("{:.2f}".format(total_cost)))

        input("press enter to finish \n")
        debug()
    elif user == "7":
        print_dual_menu(user_order)
        input("press enter to finish \n")
        debug()
    elif user == "8":
        tag = input("Tag name:")
        debug_mode.append(tag)
        debug()
    elif user == "9":
        print_single_menu(debug_mode)
        input("press enter to finish \n")
        debug()
    elif user == "10":
        print(os.getcwd())
        time.sleep(1.5)
        debug()
    elif user == "11":
        customerName = input("Customer's Name: ")
        start_line = check_two_lines("history.txt", "Customer Name:", customerName)

        if start_line == False:
            error("Person not found")
            debug()
        start_line -= 1
        end_line = get_end_line("history.txt", start_line, "----------------")
        if end_line == False:
            error("History not finished")
            debug()
        print(str(start_line) + " " + str(end_line))
        delete_portion("history.txt", start_line, end_line)
        time.sleep(1.5)
        debug()
    elif user == "12":
        name = input("Customer's Name: ")
        lines = find_user_data("history.txt", name)
        print(lines)
        print("----------------")
        for x in lines:
            start_line = int(x)
            start_line -= 1
            end_line = get_end_line("history.txt", start_line, "----------------")
            if end_line == False:
                error("History not finished")
                debug()
            read_portion("history.txt", start_line, end_line)
        input("press enter to finish \n")
        debug()
    elif venv_check == "venv" and user == str(venvOp1):
        package = input("Package name: ")
        os.system(venv_pip_exec + " install " + package)
        debug()
    elif venv_check == "venv" and user == str(venvOp2):
        program_loc = input("Program location: ")
        os.system(venv_exec + " " + program_loc)
        debug()
    elif chatBotCheck == "chatBot" and user == str(chatBotOp1):
        f = open("data.txt", "a")
        f.write("\n")
        f.write("InABotEmulateTrue")
        f.close()
        os.system(venv_exec + " " + chat_bot_loc + "/chatgui.py")

        time.sleep(1)
        delete_line("data.txt", "InABotEmulateTrue")
        debug()
    elif chatBotCheck == "chatBot" and user == str(chatBotOp2):
        os.system(venv_exec + " " + chat_bot_loc + "/train_chatbot.py")
        time.sleep(3)
        debug()
    elif chatBotCheck == "chatBot" and user == str(chatBotOp3):
        os.system(venv_exec + " " + chat_bot_loc + "/intents.py")
        time.sleep(1)
        debug()
        debug()
    elif chatBotCheck == "chatBot" and user == str(chatBotOp4):
        print("DONT CLOSE ANY WINDOWS")
        time.sleep(1)
        requirmenets = [
            "numPy",
            "Flask",
            "nltk",
            "tensorflow",
        ]  # these arent installed in main startup becuase they can be big and are optional
        for x in requirmenets:
            os.system(venv_pip_exec + " install " + x)
        debug()
    elif user == str(exit1):
        main()
    else:
        error("'" + user + "' is not a option")
        main()


# PROGRAM
f = open("data.txt", "a")
f.write(
    "\n"
)  # Creates a newline for a new order, this also creates the data file if its not there
f.close()
bot_run = check_file("data.txt", "InABotEmulateTrue")
if bot_run != True:

    debug = debug_check("data")  # Checks if data has been set in debug mode
    ignore_history = debug_check(
        "ignore_history"
    )  # Checks if ignore_history has been set in debug mode, this is just so Im not creating loads of entrys into the file while testing
    if debug == "data":
        print("Defined Functions, Set vars, Imported dependices")
    reset()
    if debug == "data":
        print("Reset files")
    if ignore_history != "ignore_history":
        f = open("history.txt", "a")
        f.write(
            "\n"
        )  # Creates a newline for a new order, this also creates the history file if its not there
        f.close()
    print(
        "##################################################################################################################"
    )

    if debug == "data":
        print("Opened File, Set file header")
    idleCheck = (
        "idlelib" in sys.modules
    )  # NOT PLACED IN VARIBLES BECUASE THEN in_idle() WOULD BE DEFIEND AFTER BEIGN CALLED WHICH RESULTS IN AN ERROR
    idledebug = debug_check("idle")  # SAME HERE
    if debug == "data":
        print("Checked for idle and for idle debug tag")
        print("idleCheck: " + str(idleCheck))
    venv()
    if idleCheck == True:  # IF it is then run the next check
        if (
            idledebug == "idle"
        ):  # if the debug tag is set to idle then alert that it is and continue
            if debug == "data":
                print("idle debug tag set, dont show warning menu")
            error("Runnning in idle with debug mode")
            main()
        else:  # else show the idle print_single_menu
            if debug == "data":
                print("idle debug tag not set, showing warning")
            run_in_idle()
    else:
        if debug == "data":
            print("idle check returned false, running as normal")
        os.system("title Freddy's Fast Fish")  # name the window to be freddys fast fish
        main()
