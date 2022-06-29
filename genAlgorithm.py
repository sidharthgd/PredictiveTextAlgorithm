import re


global wordsArray
wordsArray = []
global nodesArray
nodesArray = []

class wordNode:
    weightsArray = []
    wordsArray = []
    def __init__(self, word):
        self.word = word
        self.weightsArray = []
        self.wordsArray =  []

    def add(self, newWord):
        if newWord in self.wordsArray:
            self.weightsArray[self.wordsArray.index(newWord)]+=1
        else:
            self.wordsArray.append(newWord)
            self.weightsArray.append(1)

def findSuggestedWord(word):
    try:
        #print("index of words array should be 0 but is: " + str(wordsArray.index(word)))
        node = nodesArray[wordsArray.index(word)]
    except:
        return -1

    maxIndex = node.weightsArray.index(max(node.weightsArray))
    #print("nodesArray of: " + wordsArray[wordsArray.index(word)])
    #print("first node word is: " + nodesArray[wordsArray.index(word)].word)
    #print(nodesArray[wordsArray.index(word)].weightsArray)
    #print("The max number found in array was: " + str(max(node.weightsArray)))
    #print("The index of 19 is: " + node.weightsArray.index(19))
    #print("The max index returned was: " + str(maxIndex))
    return node.wordsArray[maxIndex]


def saveWeights():
    with open('weights.txt', 'w') as file:
        for i in range (len(wordsArray)):
            file.write(wordsArray[i] + "\n")
            for j in nodesArray[i].wordsArray:
                file.write(j + " ")
            file.write("\n")
            for j in nodesArray[i].weightsArray:
                file.write(str(j) + " ")
            file.write("\n")

def readWeights():
    with open('weights.txt', 'r') as file:
        while True:
            word = file.readline()
            wordsArray.append(re.sub(r'[^a-zA-Z]', "", word))
            #print("Just read: " + word)

            newNode = wordNode(word)
            wordsLine = file.readline()
            for tempWord in wordsLine.split():
                newNode.wordsArray.append(re.sub(r'[^a-zA-Z]', "", tempWord))
            weightsLine = file.readline()
            for weight in weightsLine.split():
                newNode.weightsArray.append(int(re.sub(r'[^0-9]', "", weight)))
            nodesArray.append(newNode)

            if word == '':
                break


def genWeights(filenames):
    currWord = ""
    afterWord = ""
    for fname in filenames:
        with open(fname,'r') as file:
            for line in file:
                for word in (re.sub(r'[*-]', " ", line)).split():
                    currWord = afterWord
                    afterWord = (re.sub(r'[^a-zA-Z]', "", word)).lower() #remove punctuation
                    #print(currWord + " " + afterWord)
                    if (currWord != ""):
                        if currWord not in wordsArray:
                            wordsArray.append(currWord)
                            nodesArray.append(wordNode(currWord))
                        nodesArray[wordsArray.index(currWord)].add(afterWord) #add weight of afterWord to node
    '''
        print("all the words in the novel: ")
        print(wordsArray)
        print("weights array of first word: ")
        print(nodesArray[0].weightsArray)
        print("first word would suggest: " + nodesArray[0].wordsArray[25])
        print("nodes array size is: " + str(len(nodesArray)))
        print("words array size is: " + str(len(wordsArray)))
        print("**")
        print("**")
        print("**")
        print("the first word is: " + wordsArray[0])
        print(findSuggestedWord(wordsArray[0]))
'''

filenames = ['warandpeace.txt', 'bleakhouse.txt']
#genWeights(filenames)
#saveWeights()
readWeights()
#readWeights()
#print("all the words in the novel: ")
#print(wordsArray)
#print("weights array of first word: ")
#print(nodesArray[0].weightsArray)
#print("nodes array size is: " + str(len(nodesArray)))
#print("words array size is: " + str(len(wordsArray)))
#print("the first word is: " + wordsArray[0])
#print(findSuggestedWord(wordsArray[0]))
while True:
    inputWord = input("Enter word: ")
    print(findSuggestedWord(inputWord))
