import json
import os
path = os.getcwd()+"/../ChatBot"
data_file = open(path+'\intents.json').read()
intents = json.loads(data_file)
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'): #if in windows
        command = 'cls'
    os.system(command)
def tag(tag, intents_json):
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            print(tag)
            return(tag)
    return("Doesnt Exist")
contTag = True
while 1 == 1:
 while contTag == True:
    print("type next to go to next input, quit to quit")    
    whatsTag = input("What is the tag: ")
    
    intentTag = tag(whatsTag, intents)
    tag = intentTag
    if intentTag == "Doesnt Exist":
       print("Doesnt Exist")
       break
    elif whatsTag.lower() == "quit":
        quit()
    pattern = "NONE"
    response = "NONE"
    while pattern != "next":
           print("For every pattern you want type it and press enter, once done type 'next'")
           pattern = input("Pattern: ")
           list_of_intents = intents['intents']
           for i in list_of_intents:
            if i['tag'] == tag and pattern.lower() != "next":
                print(tag +" "+pattern)
                i["patterns"].append(pattern)
              
    while response != "next":
           print("For every pattern you want type it and press enter, once done type 'next'")
           response = input("Response: ")
           list_of_intents = intents['intents']
           for i in list_of_intents:
            if i['tag'] == tag and response.lower() != "next":
                print(tag +" "+response)
                i["responses"].append(response)
    if os.path.exists(path+'\intents.json'):
        os.remove(path+'\intents.json')
    print(intents)    
    with open(path+'\intents.json', 'w') as outfile:
        json.dump(intents, outfile)
    clear()
