import itertools


string = input("String a ser permutada: ")
resultado = itertools.permutations(string, len(string))

res_set = set()

for i in resultado:
    res = ''.join(i)
    res_set.add(res)

print(len(res_set))
