lineNum=0
Words=[]
wordlist = open('wordlist.txt', 'r')
for line in wordlist:
    Word=''
    for letter in line:
        Word+=letter
        word = Word.replace("\n", "")
    Words.append(word)
    lineNum+=1

ScrambledList = open('Encrypted.txt', 'r')
for cypher in ScrambledList:
    possibleWords = Words
    print(cypher)
    for letter in cypher:
        print (letter)
        match = [word for word in possibleWords if letter in word]
    print (match)
