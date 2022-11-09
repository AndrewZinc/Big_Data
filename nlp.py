import nltk
from nltk import word_tokenize

text = word_tokenize('I like running in the woods')

output = nltk.pos_tag(text)

print(output)