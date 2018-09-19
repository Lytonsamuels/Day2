def vowels(word):
    vowelSubString = ''
    finishedLetters = ''
    duplicateCount = 0
    vowel = 'a,e,i,o,u'
    for x in word:
        if x not in finishedLetters:
            if x in vowel:
                vowelSubString += x
            count = word.count(x)
            if count > 1:
                duplicateCount += 1
            finishedLetters += x
    return(vowelSubString, duplicateCount)
            