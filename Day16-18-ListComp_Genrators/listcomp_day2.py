NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def name_gen():
    for i in NAMES:
        yield(i)

#name=name_gen()

namegen=[i.title() for i in name_gen()]
print("Using Generator:",namegen)

name_listcomp=[x.title() for x in NAMES]
print("Using List Comp:",name_listcomp)

name_reverse=[' '.join(reversed(y.split(' '))) for y in name_listcomp]
print("Reverse Name:",name_reverse)

# for i in name:
#     print(i.title())