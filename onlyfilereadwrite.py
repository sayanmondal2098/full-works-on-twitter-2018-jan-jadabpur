import naturalprocessingwordnet
import re
from sentencecounter import gettempwords,getallline,getline

print ("## IT'S STARTING OF ONLYFILE READWRITE SCRIPT ##")
def createnegfile(filename,word):
    # filename = input("Enter destination file name in string format :")
    f = open(filename,'a')
    f.writelines(word +"\n")

def searchword(word, sourcename):
    if word in open('list of negative words.txt').read():
            createnegfile('destinationnegfile.txt',word)
    elif word in open('list of positive words.txt').read():
            createnegfile('destinationposfile.txt',word)  


def searchwordinnegfile(word,sourcename):
    opennegdictionary = open("list of negative words.txt")
    readnegline = opennegdictionary.readline()
    readnegline = readnegline.split()
    for w in readnegline:
        if w == word:
            createnegfile('destinationnegfile.txt',word)

def searchwordinposfile(word,sourcename):
    openposdictionary = open("list of positive words.txt")
    readposline = openposdictionary.readline()
    readposline = readposline.split()
    for w in readposline:
        if w == word:
            createnegfile('destinationposfile.txt',word)



print (gettempwords())
print (gettempwords().__format__)
print (gettempwords().__getitem__)
print (len(gettempwords()))
for i in range(0,(len(gettempwords()))):
    print (gettempwords()[i])

print ("Ent of For loop")
#print the word in sorted words
print (sorted(gettempwords()))
#print the array size
print(gettempwords().__sizeof__())
print ("the 2nd word is :"+ gettempwords()[0])

