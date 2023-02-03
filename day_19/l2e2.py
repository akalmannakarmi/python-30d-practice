# Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output

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

# Your output should look like this
print(find_most_common_words('sample.txt', 10))
[(10, 'the'),
(8, 'be'),
(6, 'to'),
(6, 'of'),
(5, 'and'),
(4, 'a'),
(4, 'in'),
(3, 'that'),
(2, 'have'),
(2, 'I')]

# Your output should look like this
print(find_most_common_words('sample.txt', 5))

[(10, 'the'),
(8, 'be'),
(6, 'to'),
(6, 'of'),
(5, 'and')]