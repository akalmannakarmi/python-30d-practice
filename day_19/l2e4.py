# Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory

import re
from data.stop_words import stop_words

def remStop(words):
    stopWords=set(stop_words)
    return words-stopWords

def get_words(file):
    with open("day_19/data/"+file,encoding='utf-8') as f:
        data = f.read()
    words = re.split(r' |\n',data)
    return set(words)

files = ["obama_speech.txt","michelle_obama_speech.txt","donald_speech.txt","melina_trump_speech.txt"]

michelle_words = remStop(get_words("michelle_obama_speech.txt"))
melina_words = remStop(get_words("melina_trump_speech.txt"))

print("Michelle words lack",melina_words-michelle_words)
print("Melina words lack",michelle_words-melina_words)