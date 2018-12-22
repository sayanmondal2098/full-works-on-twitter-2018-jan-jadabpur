import pandas
from pandas import read_csv ,read_excel ,read_json ,read_pickle ,read_sql
import os 
import re 

#imported from file
from naturalprocessingwordnet import getlengthofarray,getline
from naturalprocessingwordnet import getsortedsynonyms,getsynonyms,getsysets,gettempwords
from onlyfilereadwrite import searchwordinposfile, searchwordinnegfile

print ("\n","#"*50,"\n","HI IT'S STARTING OF CSV HANDLER SCRIPT","\n","#"*50)
print (gettempwords())
def exactmatch(filename,word):
    line = filename.readline()
    line = line.split()
    for w in line:
            if w == word:
                print ("Fully Matched Word","\n")

def posfilematching(word):
    for i in range(0,getlengthofarray(word)):
        exactmatch("list of positive words.txt",gettempwords()[i])



print (bool(searchwordinposfile("acumen","list of positive words.txt")))


