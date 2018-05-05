# -*- coding: utf-8 -*-
g = (x*x for x in range(10))

for n in g:
    print(n)

print('############')
def triangles():
    N = [1]
    while True:
        yield N
        N.append(0)
        N = [N[i-1] + N[i] for i in range(len(N))]

n = 0
for x in triangles():
    print(x)
    n += 1
    if n == 10:
        break
