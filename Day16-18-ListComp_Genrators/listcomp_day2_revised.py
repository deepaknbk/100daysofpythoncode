import random
NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

name_title=[name.title() for name in NAMES]
print("Print names in Title case:",name_title)

def reverse_names(name):
    first,last=name.split()
    return f'{last} {first}'

def gen_pairs():
    first_nm=[name.split()[0].title() for name in NAMES]
    while True:
        first,second=None,None
        while first==second:
            first,second=random.sample(first_nm,2)

        yield f'{first} teams up with {second}'

name_reverse=[reverse_names(name).title() for name in NAMES]

print("Reverse Names:",name_reverse)

team=gen_pairs()

for _ in range(10):
    print(next(team))
