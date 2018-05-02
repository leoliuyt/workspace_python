import os
ds = [d for d in os.listdir('.')]
print(ds)

l = [x * x for x in range(1,5) if x % 2 == 0]#[4, 16]
print(l)

l = [m + n for m in 'ABC' for n in 'XYZ']
print(l)

d = {'x':'A','y':'B','z':'C'}
kvs = [k + '=' + v for k,v in d.items()]
print(kvs)