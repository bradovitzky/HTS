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
    print(cypher)
    possibleWords = Words
    matches = []
    for letter in cypher:
        for word in possibleWords:
            if letter in word and word not in matches:
                matches.append(word)
        for match in matches:
            if letter not in matches:
                matches.remove(match)
    print (matches)
