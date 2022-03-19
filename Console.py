#V0
import os
import time
import keyboard
play = True
gameInput = True
newLevel = False
x = 0
y = 0
posX = 5
posY = 5
levelId = 0
touching = ""
wall = ""
diricetion = ""
secretLevel = False
jump = False        
def drawLevel(array):
    for x in array:
        print(x)

def storeLevel(num):
    level = []
    if num == -2:
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                     WELCOME TO ASCII GAME BY MAX TYSON                                            +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                        w,a,d or arrow keys to move                                                +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                             space to begin                                                        +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                     __                                                            +")
     level.append("+                                                    /  \                                                           +")
     level.append("+                        %%%%%%                     ! ** !                                                          +")
     level.append("+              @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\__/                                                           +")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")  
    if num == -1:
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                               __  +")
     level.append("+                                                                                                              /  \ +")
     level.append("+                                                                                                             ! ** !+")
     level.append("+                                                                                                              \__/ +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 

    if num == 0:
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                         Welcome to ASCII GAME by Max Tyson                                        +")
     level.append("+                     A console game made in pyton using only varibles, maths and functions                         +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                   Get to the middle of the portal +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                          \        +")
     level.append("+                                                                                                           \       +")
     level.append("+                                                                                                            \      +")
     level.append("+                                                                                                             \     +")
     level.append("+                                                                                                               __  +")
     level.append("+                                                                                                              /  \ +")
     level.append("+                                                                                                             ! ** !+")
     level.append("+                                                                                                              \__/ +")
     level.append("+                               @@@@@@@                                                   @@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+                        @@@@@@@@@@@@@@@@@                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if num == 1:
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                  JUMP THE PLATFORM                                                                +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                               __  +")
     level.append("+                                                                                                              /  \ +")
     level.append("+                                                                                                             ! ** !+")
     level.append("+                                                                                                              \__/ +")
     level.append("+                        @@@@@@@@@@    @@@  @@@    @@@      @@@    @@@    @@@   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+                    @@@@@@@@@@@@@@                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+                  @@@@@@@@@@@@@@@@                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+               @@@@@@@@@@@@@@@@@@@                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+           @@@@@@@@@@@@@@@@@@@@@@@                                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if num == 2:
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                 BE WARE THE SPIKES {%%%%%%%}                                               __     +")
     level.append("+                                                                                                           /  \    +")
     level.append("+                                                                                                          ! ** !   +")
     level.append("+                                                                                                           \__/    +")
     level.append("+                                                                                                         @@@@@@    +")
     level.append("+                                                                                                @@@@@@             +")
     level.append("+                                                                                     @@@@@@                        +")
     level.append("+                                                                            @@@@@@                                 +")
     level.append("+                                                                @@@@@@                                             +")
     level.append("+                                                     @@@@@@                                                        +")
     level.append("+                                       @@@@@@@@@                                                                   +")
     level.append("+         @@@@@@@@@@@@@@@@@@@@@@@@@                                                                                 +")
     level.append("+         @@@@@@@@@@@@@@@@@@@@@@@@@                                                                                 +")
     level.append("+         @@@@@@@@@@@@@@@@@@@@@@@@@                                                                                 +")
     level.append("+      @@@@@@@@@@@@@@@@@@@@@@@@@@@@                                                                                 +")
     level.append("+      @@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") 
    if num == 3:
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")    
     level.append("+                                   Should be easy to figure this one out                                           +")
     level.append("+                                                                                                                   +")
     level.append("+              __                                                                                                   +")
     level.append("+             /  \                                                                                                  +")
     level.append("+            ! ** !                                                                                                 +")
     level.append("+             \__/                                                                                                  +")
     level.append("+             @@@@@@   @@@@@@@   @@@@@@@@  @@@@@@@ @@@@       @@@    @@@  @@@   @@@@@@@@@@                          +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                @@@@@@@@@@                         +")
     level.append("+                                                                           @@@                                     +")
     level.append("+                                                                    @@@@                                           +")
     level.append("+                                                              @@@                                                  +")
     level.append("+                                                       @@@@                                                        +")
     level.append("+                                               @@@@@                                                               +")
     level.append("+                                        @@@@                                                                       +")
     level.append("+                  @@@@@    @@@   @@@@                                                                              +")
     level.append("+       @@@@@@@@                                                                                                    +")
     level.append("+@@@@@@@@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%+")
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if num == 4:
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
     level.append("+                                                                                                                   +")
     level.append("+                                 Hint: Ground is calculated through the big eye                                    +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                           @@@                                                                     +")
     level.append("+                                                                                                                   +")
     level.append("+                                              %       @@@                                                          +")
     level.append("+                               @@@            %                                                                    +")
     level.append("+                                    @@@       %                                                                    +")
     level.append("+                                              %                                                                    +")
     level.append("+                                              %                                                                    +")
     level.append("+                                              %                                                                    +")
     level.append("+                              @@@@@@@@@@@@@@@@@@@@@@@@@         @@@@@@@@@@@              @@@@@@@@@@@@@             +")
     level.append("+                                                                                                                   +")
     level.append("+                       @@@                                                    @@@@@@                               +")
     level.append("+                                                                                                                   +")
     level.append("+                 @@@@                                                                                              +")
     level.append("+                                                                                                              _    +")
     level.append("+          @@@@                                                                                               /  \  +")
     level.append("+                                                                                                            ! ** ! +")
     level.append("+     @@@                                                                                                     \__/  +")
     level.append("+@@@@@@@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@@@@@@@@@@@@@@@@+")
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if num == 5:
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
     level.append("+                                                              __                                                   +")
     level.append("+                                                             /  \                                                  +")
     level.append("+%%%%%%%%%%%%%%%%%%%%%The g1itch seems to be getting worsE   ! ** !                                                 +")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@JUMP = CRASH@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if num == 6:
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
     level.append("+   11011                                                                                                           +")
     level.append("+                                 ErR: OuT oF MeMoRy                                                                +")
     level.append("+                                                                         10011                                     +")
     level.append("+                                                                                                                   +")
     level.append("+                                                          !                                                        +")
     level.append("+                       !                !                                                         !                +")
     level.append("+                !                                                                                                  +")
     level.append("+                                                             !                    !                                +")
     level.append("+                                                                                                                   +")
     level.append("+                                    !                                                                              +")
     level.append("+                                                !                                                                  +")
     level.append("+                                              100111                                                               +")
     level.append("+                       !                                              !                             1!             +")
     level.append("+       !                                                                                                       __  +")
     level.append("+                                                                                                              /  \ +")
     level.append("+                                         !                                               1                     !   +")
     level.append("$                    !                                                                                          \__/+")
     level.append("+                                                                         !            1           /__\             +")
     level.append("+                                                                                                                   +")
     level.append("+         !   10101                                                                                  **** *         +")
     level.append("+                                   !                 !                                 !      1      !             +")
     level.append("+                                                                                               \_______/           +")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    if num == 7:
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                    CMD >> Game()                                                                                  +")
     level.append("+                                                                                                                   +")
     level.append("+                    CMD >> restarting ...                                                                          +")
     level.append("+                    CMD >> checking score .....                                                                    +")
     level.append("+                    CMD >> echo %YOU WIN%                                                                          +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                    CMD >> [USER] How to exit???                                                                   +")
     level.append("+                    CMD >> ctrl C                                                                                  +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+                                                                                                                   +")
     level.append("+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+")
     level.append("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")  
    return level   
def storePlayer(x,y,draw):
    global touching
    global wall
    global newLevel
    global diricetion
    global secretLevel

    tmp = []
    result = []
    for i in reversed(draw):
        tmp.append(i)
    Y = tmp[y]
    X = list(Y)
    x = int(x)
    x1 = x+1
    x2 = x+2
    x3 = x+3

    
    wall = ""
    ######

    if X[x] != "@":
     if X[x-1] == "$":
          secretLevel = True       
     X[x] = "["
     if X[x-1] == "+"  or  X[x-1] == "@":
        wall = "LeftWall"
    if diricetion == "left":        
     NY = tmp[y+1]
     NX = list(NY)
     if NX[x+1] == "+" or NX[x+1] == "@":
        wall = "Roof"
    ######
    if diricetion == "left":     
     if X[x1] != "@":  
      if X[x1] == "*":
          newLevel = True 
     
      NY = tmp[y-1]
      NX = list(NY)
      if X[x1] == "%":
          touching = "Spike"
      else:
       if NX[x1] == "@":
         touching = "OnGround"    
       else:    
        touching = "Air"
     else:
       touching = "Ground"
     X[x1] = "0"  
    else:
        X[x1] = "o"  
    ######
    if diricetion == "right":      
     if X[x2] != "@":     
      if X[x2] == "*":
          newLevel = True 
      NY = tmp[y-1]
      NX = list(NY)
      if X[x2] == "%":
          touching = "Spike" 
      else:
       if NX[x2] == "@":
        touching = "OnGround"
       else:    
        touching = "Air"
     else:
       touching = "Ground"
     X[x2] = "0"
    else:
      X[x2] = "o"  
    ######    
    if X[x3] != "@":
     X[x3] = "]"
     if X[x3+1] == "+" or  X[x3+1] == "@":
        wall = "RightWall"
     if diricetion == "right":        
      NY = tmp[y+1]
      NX = list(NY)
      if NX[x3] == "+" or NX[x3] == "@":
        wall = "Roof"   
    ######    
    text = ""
    text = text.join(X)
    tmp[y] = text
    for i in reversed(tmp):
     result.append(i)
      
    return(result)          
  
def drawGame():
    
    global levelId
    global posX
    global posY
    level = storeLevel(levelId)
    level = storePlayer(posX,posY,level)
    drawLevel(level)
    return
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'): #if in windows
        command = 'cls'
    os.system(command)
def platformer():
    global play
    global gameInput
    global newLevel
    global x
    global y
    global posX 
    global posY 
    global levelId 
    global touching 
    global wall 
    global diricetion 
    global secretLevel
    global jump 
    while play == True:   
     clear()
     x = 0
     y = 0
     if touching == "Spike":
        posX = 5
        posY = 5 
     if newLevel == True:
        levelId += 1
        newLevel = False
        posX = 5
        posY = 5
     if secretLevel == True:
        levelId = 9
        secretLevel = False
        posX = 5
        posY = 5   
     if keyboard.is_pressed('right arrow') and  wall != "RightWall" or keyboard.is_pressed('d') and  wall != "RightWall":
         x += 1
         diricetion = "right"
         time.sleep(0.001)
     elif keyboard.is_pressed('left arrow') and  wall != "LeftWall" or keyboard.is_pressed('a') and  wall != "LeftWall":
         x -= 1
         diricetion = "left"
         time.sleep(0.001)
     posX += x
     if  touching == "Ground":
         posY += 1 
     if touching == "OnGround":
        if jump != True: 
         if keyboard.is_pressed('up arrow') or keyboard.is_pressed('w'):
          jump = True
          countJump = 0
          time.sleep(0.01)
     if jump == True:
        if countJump != 4:  
         countJump += 1
         if wall != "Roof": 
          posY += 1
        else:
         jump = False   
     elif touching  == "Air":
         y -= 1
     posY += y
     drawGame()
     print("Wall: "+ wall)
     print("Level: "+ str(levelId))
     print("Touching: "+ str(touching))
     print("Pos: "+str(posX)+", "+str(posY))
     time.sleep(0.05)

def start():
  global diricetion
  global levelId
  diricetion = "right"
  wait = 0
  across = 3
  up = 6
  levelMap = storeLevel(-2)
  level = storePlayer(4,2,levelMap)
  drawLevel(level)
  while wait == 0:
   if keyboard.is_pressed('space'):
    wait = 1
  clear()
  while across != 14:
   clear() 
   level = storePlayer(across,2,levelMap)
   drawLevel(level)   
   across += 1
  clear() 
  level = storePlayer(across,3,levelMap)
  drawLevel(level)   
  while across != 23:
   clear() 
   level = storePlayer(across,3,levelMap)
   drawLevel(level)   
   across += 1
  clear() 
  level = storePlayer(across,6,levelMap)
  drawLevel(level)   
  while across != 32:
   clear() 
   level = storePlayer(across,6,levelMap)
   drawLevel(level)   
   across += 1
  while up != 2:
   clear() 
   level = storePlayer(across,up,levelMap)
   drawLevel(level)   
   up -= 1
  while across != 54:
   clear() 
   level = storePlayer(across,3,levelMap)
   drawLevel(level)   
   across += 1
   
#start()
levelId = 4
cmd = True
while cmd == True:
   inpt = input('CMD>> ')
   if inpt == "Game()":
      inpt = input('CMD>> Password? ')
      if inpt == "superSecretPassword":
          platformer()
   if inpt == "Help":
       print("Shame you have no clue whats going on...")
   else:
      print("CMD>> Unknown Command") 


