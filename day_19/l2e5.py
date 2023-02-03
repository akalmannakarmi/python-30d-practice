# Find the 10 most repeated words in the romeo_and_juliet.txt

import re

def find_most_common_words(file,count):
    with open("day_19/data/"+file,encoding='utf-8') as f:
        data = f.read()
    words = re.split(r' |\n',data)
    Cwords = {}
    for word in words:
        if word == "":
            continue
        if word in Cwords:
            Cwords[word] +=1
        else:
            Cwords[word] = 1
    Cwords = sorted(Cwords.items(),key=lambda item:item[1],reverse=True)
    return Cwords[:count]

print(find_most_common_words("romeo_and_juliet.txt",10))