import nltk
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')

import csv
with open('EECS_Abstracts.csv','r') as file:
    reader = csv.reader(file)
    lib = list(reader)

filtered_lib = []
for abstract in lib[0]:
    word_tokens = tokenizer.tokenize(abstract)
    filtered_abstract = [w for w in word_tokens if not w in stop_words] 
    filtered_lib.append(filtered_abstract)