Words=[]
wordlist = open('wordlist.txt', 'r')
for line in wordlist:
    Word=''
    for letter in line:
        Word+=letter
        word = Word.replace("\n", "")
    Words.append(word)

ScrambledList = open('Encrypted.txt', 'r')
for cypher in ScrambledList:
    possibleWords = Words
    print(cypher)
    matches = []
    for letter in cypher:
        print (letter)
        matches.append[word for word in possibleWords if letter in word]
    for match in matches:
        if match in matches
