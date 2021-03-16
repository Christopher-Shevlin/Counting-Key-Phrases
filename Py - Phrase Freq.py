from nltk.util import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.collocations import *


data = ["this", "is", "not", "a", "test", "this", "is", "real", "not", "a", "test", "this", "is", "this", "is", "real", "not", "a", "test"]

bigrams = ngrams(data, 2)

bigrams_c = {}
for b in bigrams:
    if b not in bigrams_c:
        bigrams_c[b] = 1
    else:
        bigrams_c[b] += 1
        
print(bigrams_c)