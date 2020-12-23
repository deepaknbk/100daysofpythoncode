
from collections import Counter
import calendar
import itertools
import random
import re
import string
import requests

names = 'pybites mike bob julian tim sara guido'.split()

for name in names:
    print("Names:",name.title())

first_half_alphabet = list(string.ascii_lowercase)[:13]
new_names = []
for name in names:
    if name[0] in first_half_alphabet:
        new_names.append(name.title())
print("New Names:",new_names)
new_names2 = [name.title() for name in names if name[0] in first_half_alphabet]
print("New Names2:",new_names2)


resp = requests.get('http://projects.bobbelderbos.com/pcc/harry.txt')
words = resp.text.lower().split()
print("First 5 words from Harry:",words[:5])

cnt = Counter(words)
print("Most Common words from Harry:",cnt.most_common(5))


words = [re.sub(r'\W+', r'', word) for word in words]


resp = requests.get('http://projects.bobbelderbos.com/pcc/stopwords.txt')
stopwords = resp.text.lower().split()
print("Stop words:",stopwords[:5])
words = [word for word in words if word.strip() and word not in stopwords]

cnt = Counter(words)
print("Most Common words after removing stop words:",cnt.most_common(5))

