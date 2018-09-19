def countvowels(text):
    vowels ="a,e,i,o,u"
    new=""
    x = set(text)
    dup = len(text)-len(x)
    for i in vowels:
        if i in text:
            new += str(i)
    return(new,dup)
y =input('enter a sentence:')
print(countvowels(y))