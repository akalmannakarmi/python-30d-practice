# What is the most frequent word in the following paragraph?
import re
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'


words = re.split(r' |\.',paragraph)
wordsC = {}
for word in words:
    if word =="":
        continue
    if word in wordsC:
        wordsC[word] +=1
    else:
        wordsC[word] = 1

sWordsC = sorted(wordsC.items(), key=lambda item:item[1],reverse=True)
print(sWordsC)
