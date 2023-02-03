# Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

import requests

response = requests.get("http://www.gutenberg.org/files/1112/1112.txt")

def find_most_common_words(text,count):
    words=text.split(' ')
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

print(find_most_common_words(response.text,10))