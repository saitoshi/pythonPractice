'''
@name WordFrequency Counter 
@desc Counts the frequency of a word based on the given sentence 
@returns List of the 
'''

def wordFrequencyCounter(strWords):
    # split the given string collection into a list
   wordList = strWords.split()
   # get the unique words 
   uniqueWords = set(wordList)
   #iterate 
   for word in uniqueWords:
        print('Frequency of ', word , 'is :', wordList.count(word))

wordFrequencyCounter("apple mango apple orange orange apple guava mango mango")


