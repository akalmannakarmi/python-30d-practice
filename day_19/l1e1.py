# Write a function which count number of lines and number of words in a text. All the files are in the data the folder: 
# a) Read obama_speech.txt file and count number of lines and words 
# b) Read michelle_obama_speech.txt file and count number of lines and words 
# c) Read donald_speech.txt file and count number of lines and words 
# d) Read melina_trump_speech.txt file and count number of lines and words

files = ["obama_speech.txt","michelle_obama_speech.txt","donald_speech.txt","melina_trump_speech.txt"]

for file in files:
    with open("day_19/data/"+file) as f:
        data = f.read()
    lines = data.count("\n")+1
    words = data.count(" ")+1
    print(file)
    print(f"Lines:{lines}\nWords:{words}")