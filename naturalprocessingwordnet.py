
#import for synonyms and antonymsdate keys

from nltk import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import words
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag, pos_tag_sents

#import for bag of word
import numpy as np
#For the regular expression
import re
#Textblob dependency
from textblob import TextBlob
from textblob import Word
#set to string 
from ast import literal_eval
#From src dependency 
from sentencecounter import no_sentences,getline,gettempwords 

import os
def getsysets(word):
    syns = wordnet.synsets(word)  #wordnet from ntlk.corpus  will not work with textblob
    #print(syns[0].name()) 
    #print(syns[0].lemmas()[0].name())  #get synsets names 
    #print(syns[0].definition())  #defination 
    #print(syns[0].examples())    #example


# getsysets("good")


def getsynonyms(word):
    synonyms = []
    # antonyms = []
 
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
            # if l.antonyms():
            #     antonyms.append(l.antonyms()[0].name())
 
    # print(set(synonyms))
    return(set(synonyms))
    # print(set(antonyms))


# getsynonyms_and_antonyms("good")


def extract_words(sentence):
    ignore_words = ['a']
    words = re.sub("[^\w]", " ",  sentence).split() #nltk.word_tokenize(sentence)
    words_cleaned = [w.lower() for w in words if w not in ignore_words]
    return words_cleaned    


def tokenize_sentences(sentences):
    words = []
    for sentence in sentences:
        w = extract_words(sentence)
        words.extend(w)
        
    words = sorted(list(set(words)))
    return words

def bagofwords(sentence, words):
    sentence_words = extract_words(sentence)
    # frequency word count
    bag = np.zeros(len(words))
    for sw in sentence_words:
        for i,word in enumerate(words):
            if word == sw: 
                bag[i] += 1
                
    return np.array(bag)

def tokenizer(sentences):
    token = word_tokenize(sentences)
    return token
    print("#"*100)
    print (sent_tokenize(sentences))
    print (token)
    print("#"*100)


# sentences = "Machine learning is great","Natural Language Processing is a complex field","Natural Language Processing is used in machine learning"
# vocabulary = tokenize_sentences(sentences)
# print (vocabulary)
# tokenizer(sentences)

def createposfile(filename,word):
    # filename = input("Enter destination file name in string format :")
    f = open(filename,'w')
    f.writelines(word+'\n')

def createnegfile(filename,word):
    # filename = input("Enter destination file name in string format :")
    f = open(filename,'w')
    f.writelines(word)

def getsortedsynonyms(word):
    sortedsynonyms = sorted(getsynonyms(word))
    return sortedsynonyms

def getlengthofarray(word):
    return getsortedsynonyms(word).__len__()

def readposfile():
    f = open('list of positive words.txt')
    return f

# def searchword(word, sourcename):
#     if word in open('list of negative words.txt').read():
#             createnegfile('destinationposfile.txt',word)
#     elif word in open('list of positive words.txt').read():
#             createposfile('destinationnegfile.txt',word)     

#     else:
#         for i in range (0,getlengthofarray(word)):
#             searchword(getsortedsynonyms(word)[i],sourcename)

def searchword(word,srcfile):
    # if word in open('list of negative words.txt').read():
    #         createnegfile('destinationposfile.txt',word)
    if word in open('list of positive words.txt').read():
            createposfile('destinationnegfile.txt',word)
    else:
        for i in range(0,getlengthofarray(word)):
            searchword(sorted(getsynonyms(word))[i],srcfile)
            f = open(srcfile,'w')
            f.writelines(word)

print ('#'*50)
# searchword('lol','a.txt')
print(readposfile())
# tokenizer(sentences)
# getsynonyms('good')
# print(sorted(getsynonyms('good'))[2])  #finding an array object [hear it's 3rd object]
print ('#'*50)
# print (getsortedsynonyms('bad').__len__())
# createposfile('created.txt','lol')
# for word in word_tokenize(getline()):
#     searchword(word,'a.txt')
