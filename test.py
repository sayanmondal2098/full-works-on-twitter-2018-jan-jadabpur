
for word in getline():
    searchword(word,'a.txt','b.txt')

searchword("good","a.txt","bbbbbb.txt")
def paragraph(sourcefile):
    f = open(sourcefile,'r')
    readlines = f.readlines()
    print (readlines)

# tokenizer(getline())

print ('-'*50)
# print(tokenize_sentences(getline()))
# searchword('a','a.txt','bb.txt')
for word in getline():
    print (getsynonyms(word))
