import glob
import re
id = 1

with open('reviews.tsv', 'w') as f:

    for filename in glob.iglob('./neg/*.txt'):
         print(id)
         id += 1
         file = open(filename, 'r')
         text = file.read()
         print(text)
         f.write(str(id) + "\t" + "0" + "\t" + re.sub("[^a-zA-Z0-9]"," ", text) + "\n")
     
    for filename in glob.iglob('./pos/*.txt'):
        print(id)
        id += 1
        file = open(filename, 'r')
        text = file.read()
        f.write(str(id) + "\t" + "1" + "\t" + re.sub("[^a-zA-Z0-9]"," ", text) + "\n")
        print(text)