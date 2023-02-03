# Clean the following text. After cleaning, count three most frequent words in the string.

import re

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

def clean_text(s):
    return re.sub(r'[!@#$%^&*():]','',s)

def most_frequent_words(s):
    words = re.split(r' |\.',s)
    wordsC = {}
    for word in words:
        if word =="":
            continue
        if word in wordsC:
            wordsC[word] +=1
        else:
            wordsC[word] = 1
    wordsC=sorted(wordsC.items(), key=lambda item:item[1],reverse=True)
    return wordsC[:3]

print(clean_text(sentence))
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
print(most_frequent_words(clean_text(sentence))) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
