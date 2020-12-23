def num_gen():
    for i in range(5):
        yield i


gen = num_gen()

print(next(gen))

for i in gen:
    print(i)

