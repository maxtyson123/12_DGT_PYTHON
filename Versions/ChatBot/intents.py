import json
import os
path = os.getcwd()+"/../ChatBot"
data_file = open(path+'\intents.json').read()
intents = json.loads(data_file)

def writepattern(tag, intents_json):
    pattern = input("Pattern: ")
    runAgain1 = tag
    runAgain2 = intents_json
    if pattern != "next":
       list_of_intents = intents_json['intents']
       for i in list_of_intents:
        if(i['tag']== tag):
            print(tag +" "+pattern)
            
       writepattern(runAgain1, runAgain2)
def writeresponse(tag, intents_json):
    response = input("Response: ")
    if response != "next":
       writeresponse()
def tag(tag, intents_json):
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            print(tag)
            return(tag)
    print("Doesnt Exist")        
whatsTag = input("What is the tag: ")
intentTag = tag(whatsTag, intents)
print("For every pattern you want type it and press enter, once done type 'next'")
writepattern(intentTag, intents)
print("For every Response you want type it and press enter, once done type 'next'")
writeresponse()
