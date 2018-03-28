from gensim.models import Word2Vec
from textblob import TextBlob
import pandas as pd 

#infile = 'filetest.csv'
#df = pd.read_csv('filetest.csv')

#data = df.values.tolist()

#for row in data:
#    blob = TextBlob(row[0])
#    print blob
#    sentences = blob
# define training data
#print sentences
# train model

# <----------------------------------------TEST 1-------------------------------------------------------------->
sentences = 'LOL, I LIKE IT '
model = Word2Vec(sentences, min_count=10000)
# summarize the loaded model
print(model)
# summarize vocabulary
#words = list(model.wv.vocab)
#print(words)
# access vector for one word
#print(model['sentence'])
# save model
#model.save('model.bin')
# load model
#new_model = Word2Vec.load('model.bin')
##print(new_model)

