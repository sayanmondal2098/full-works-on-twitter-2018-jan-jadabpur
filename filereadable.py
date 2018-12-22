import naturalprocessingwordnet
from sentencecounter import gettempwords,filename,getline

def createnegfile(filename,word):
    # filename = input("Enter destination file name in string format :")
    f = open(filename,'a')
    f.writelines(word +"\n")



def searchword(word, sourcename):
        counter = 0

        if word in open('list of negative words.txt').read():
                createnegfile('destinationnegfile.txt',word)
                counter = counter + 1
        else:
                for item in naturalprocessingwordnet.getsynonyms(word):
                        if item in open('list of negative words.txt').read():
                                createnegfile('destinationnegfile.txt', word)
                                counter = counter + 1
        
        if word in open('list of positive words.txt').read():
                createnegfile('destinationposfile.txt',word)
                counter = counter + 1 
        else:
                for item in naturalprocessingwordnet.getsynonyms(word):
                        if item in open('list of positive words.txt').read():
                                createnegfile('destinationposfile.txt', word)
                                counter = counter + 1

        if counter == 0:
                createnegfile('destinationneufile.txt', word)




for word in gettempwords():
    searchword(word, filename)

print('*'*50)
for i in range(0,(gettempwords().__len__())):
    searchword(sorted(gettempwords())[i],filename)



# print('*'*50)
# for i in range(0,5):
#     print(sorted(gettempwords())[i])
   
