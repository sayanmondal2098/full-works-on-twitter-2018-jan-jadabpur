from naturalprocessingwordnet import getsynonyms
textFile = open("./a.txt", "r")
wordsToFind = textFile.read().lower().split(" ")
# wordsToFind[:-1]
wordsToFind[-1] = wordsToFind[-1].strip().strip(".")
# wordsToFind = ["motivated"]
positiveWordsFile = open("./list of positive words.txt", "r")
negativeWordsFile = open("./list of negative words.txt", "r")
start = False
positiveFile = list(positiveWordsFile)
negativeFile = list(negativeWordsFile)
posSet = set()
negSet = set()
neutralSet = set()
positiveWords = []
negativeWords = []
for i in positiveFile:
    if i == "a+\n":
        start = True
    if start:
        positiveWords.append(i.lower().strip())
start = False

for i in negativeFile:
    if i == "2-faced\n":
        start = True
    if start:
        negativeWords.append(i.lower().strip())
class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 256

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case

        return ord(ch)

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

            # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord

def removeDuplicatesSave(file_name, set_data):
    with open(file_name, 'r') as fp:
        file_data = fp.readlines()
        for word in file_data:
            set_data.add(word.strip())
        fp.close()
        set_data=set(set_data)
    with open(file_name, 'w') as fp:
        for word in set_data:
            fp.write(word + "\n")
        fp.close()

def main():
    # Trie object
    positiveTrie = Trie()
    negativeTrie = Trie()

    # Construct positive and negative tries
    for key in positiveWords:
        positiveTrie.insert(key)
    for key in negativeWords:
        negativeTrie.insert(key)
    for word in wordsToFind:
        word = word.lower()
        if positiveTrie.search(word):
            posSet.add(word)
            removeDuplicatesSave("./destinationposfile.txt", posSet)
        elif negativeTrie.search(word):
            negSet.add(word)
            removeDuplicatesSave("./destinationnegfile.txt", negSet)
        else:
            synonyms = []
            synonymFound = False
            synonyms = getsynonyms(word)
            for syn in synonyms:
                if positiveTrie.search(syn):
                    posSet.add(syn)
                    synonymFound = True
                    break
                elif negativeTrie.search(syn):
                    negSet.add(syn)
                    synonymFound = True
                    break
            if synonymFound == False:
                neutralSet.add(word)
        # Search for different keys
    removeDuplicatesSave("./destinationposfile.txt", posSet)
    removeDuplicatesSave("./destinationnegfile.txt", negSet)
    removeDuplicatesSave("./destinationneufile.txt", neutralSet)
if __name__ == '__main__':
    main()
