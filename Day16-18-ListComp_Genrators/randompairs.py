import random
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

name_split=[]
for name in NAMES:
    a,b=name.split(' ')
    name_split.append(a.title())
    name_split.append(b.title())
    #print(name_split)

for _ in range(10):
    #print(random.choice(name_split),random.choice(name_split))
    print(f'{random.choice(name_split)} teams up with {random.choice(name_split)}')