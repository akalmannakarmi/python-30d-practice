# Use the function, find_most_frequent_words to find: 
# a) The ten most frequent words used in Obama's speech 
# b) The ten most frequent words used in Michelle's speech 
# c) The ten most frequent words used in Trump's speech 
# d) The ten most frequent words used in Melina's speech

import re

def find_most_common_words(file,count):
    with open("day_19/data/"+file,encoding='utf-8') as f:
        data = f.read()
    words = re.split(r' |\n',data)
    Cwords = {}
    for word in words:
        if word in Cwords:
            Cwords[word] +=1
        else:
            Cwords[word] = 1
    Cwords = sorted(Cwords.items(),key=lambda item:item[1],reverse=True)
    return Cwords[:count]

files = ["obama_speech.txt","michelle_obama_speech.txt","donald_speech.txt","melina_trump_speech.txt"]

for file in files:
    print(file)
    print(find_most_common_words(file,10))