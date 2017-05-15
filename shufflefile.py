import random
lines = open('reviews.tsv').readlines()
random.shuffle(lines)
open('reviews.tsv', 'w').writelines(lines)