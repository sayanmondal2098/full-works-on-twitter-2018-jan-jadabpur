fname = input("Enter file name: ")
# num_lines = 0
# with open(fname, 'r') as f:
#     for line in f:
#         num_lines += 1
# print("Number of lines:")
# print(num_lines)

# total_line_count = sum(1 for line in open(fname))

# print (total_line_count)


# count lines, sentences, and words of a text file
# set all the counters to zero
lines, blanklines, sentences, words = 0, 0, 0, 0

try:
  # use a text file you have, or google for this one ...
#   fname = 'GettysburgAddress.txt'
  textf = open(fname, 'r')
except IOError:
  print ('Cannot open file %s for reading' % fname)
  import sys
  sys.exit(0)
# reads one line at a time
for line in textf:
  print (line),   # test
  lines += 1
  
  if line.startswith('\n'):
    blanklines += 1
  else:
    # assume that each sentence ends with . or ! or ?
    # so simply count these characters
    sentences += line.count('.') + line.count('!') + line.count('?')
    
    # create a list of words
    # use None to split at any whitespace regardless of length
    # so for instance double space counts as one space
    tempwords = line.split(None)
    # print (tempwords)  # test
    
    # word total count
    words += len(tempwords)

lines = tuple(open(fname, 'r'))


with open(fname, "r") as ins:
    array = []
    for line in ins:
      print(array.append(line))
# textf.close()
print ('-' * 100)
# print (tempwords)
# print ("Lines      : ", lines)
# print ("Blank lines: ", blanklines)
print ("Sentences  : ", sentences)
# print ("Words      : ", words)
# optional console wait for keypress
def filename():
  return fname
def no_sentences():
    return sentences

def gettempwords():
  return (tempwords)

def getallline():
  return (lines)

def getline():
  return(line)

print(no_sentences())
print ('//' * 100)
# print(getline())
print (gettempwords())
print ('*' * 100)
