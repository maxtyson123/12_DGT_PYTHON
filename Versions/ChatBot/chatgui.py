
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import os
path = os.getcwd()+"/../ChatBot" #the reason we have to add this is becuase when the script gets the wroikf directory it getts weher it was excuted from which was the main dir of main.py
print(path)
import sys
mainPyLoc = os.getcwd()
print("SYS")
sys.path.insert(0, mainPyLoc)
print("IMPORYT")
import main as script
print("PLEASE TRAIN BEFORE FIRST RUN")
print(" ")
print(" ")
print(" ")
print(" ")
print("If you encounter nltk errors, run training script ")
print("main.main()")
script.logo()
from keras.models import load_model
model = load_model(path+'\chatbot_model.h5')
import json
import random

intents = json.loads(open(path+'\intents.json').read())
words = pickle.load(open(path+'\words.pkl','rb'))
classes = pickle.load(open(path+'\classes.pkl','rb'))
chipsResponse = False
amtOfFish = 0
fishType = 0
firstFishResponse = False
secondFishResponse = False

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            print("Tag: "+tag)
            if tag == "fish":
               print("-fish tag commnads")
               result = "dotnPrint"
               fish(0,0)
               break
            elif tag == "chips":
               print("-chips tag commnads")
               print("running()")
               chips(False, 0)
               result = "dotnPrint"
               break
            else:
             print("-any tag commnads")       
             result = random.choice(i['responses'])
             break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
  
    return res

#Food ordering
def chips(impt,amt):
   global chipsResponse
   if impt == False:
       print("isInput FALSE")
       ChatLog.insert(END, "Bot: " + "How many scoops of chips would you like?" + '\n\n')
       ChatLog.config(state=DISABLED)
       ChatLog.yview(END)
       chipsResponse = True
   if impt == True:
       print("isInput TRUE")
       ChatLog.config(state=NORMAL)
       ChatLog.insert(END, "You: " + amt + '\n\n')
       ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
       ChatLog.insert(END, "Bot: " + "Adding "+amt+" scoops of chips to your order" + '\n\n')
       ChatLog.config(state=DISABLED)
       ChatLog.yview(END)
       chipsResponse = False
   #pass the response to the main.py #i will have to make sure main.py can handle this later
def fish(isInput,userInput):
   global firstFishResponse
   global secondFishResponse
   global amtOfFish
   global fishType
   if isInput == 0:
       print("isInput FALSE")
       ChatLog.insert(END, "Bot: " + "What type of fish do you want." + '\n\n')
       ChatLog.insert(END, "$4.10: " + "Shark, Flounder, Cod, Gurnet, John Dory, Gold Fish," + '\n\n')
       ChatLog.insert(END, "$7.20: " + "Snapper, Pink Salmon, Tuna, Smoked Marlin, Kahwai, Dolphin" + '\n\n')
       ChatLog.config(state=DISABLED)
       ChatLog.yview(END)
       firstFishResponse = True
   if isInput == 1:
       print("isInput TRUE")
       ChatLog.config(state=NORMAL)
       ChatLog.insert(END, "You: " + userInput  + '\n\n')
       ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
       ChatLog.insert(END, "Bot: " + "How many "+userInput+" do you want?" + '\n\n')
       ChatLog.config(state=DISABLED)
       ChatLog.yview(END)
       fishType = userInput 
       firstFishResponse = False
       secondFishResponse = True
   if isInput == 2:
       print("isInput TRUE")
       ChatLog.config(state=NORMAL)
       ChatLog.insert(END, "You: " + userInput  + '\n\n')
       ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
       ChatLog.insert(END, "Bot: " + "Adding " + userInput + " "+fishType+" to your order"+ '\n\n')
       ChatLog.config(state=DISABLED)
       ChatLog.yview(END)
       amtOfFish = userInput
       print("Passing "+userInput + " "+fishType+" to main.py")
       amtOfFish = 0
       fishType = 0               
       secondFishResponse = False    
   
import tkinter
from tkinter import *


def send():
    global chipsResponse
    global firstFishResponse
    global secondFishResponse
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    print("chipsResponse: "+str(chipsResponse))
    print("Running if chipsResponse")
    if chipsResponse == True:
       print("Chips amount is: "+msg)
       chips(True,msg)
       return
    elif firstFishResponse == True:
       print("Fish type is: "+msg)
       print("Error is here")
       fish(1,msg)
       return
    elif secondFishResponse == True:
       print("Fish amount is: "+msg)
       fish(2,msg)
       return
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

        res = chatbot_response(msg)
        print(res)
        if res != "dotnPrint":
            ChatLog.insert(END, "Bot: " + res + '\n\n')

            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)


base = Tk()
base.title("Freddy's Fast Fish")
base.geometry("400x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5,
                    bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',
                    command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

base.mainloop()
