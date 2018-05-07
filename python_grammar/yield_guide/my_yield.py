def gen_example():
    print('before any yield')
    yield 'first yield'
    print('between yields')
    yield 'second yield'
    print('no yield anymore')
gen = gen_example()
print(type(gen))

# yieldValue1 = next(gen)
# print(yieldValue1)

# yieldValue2 = next(gen)
# print(yieldValue2)

# yieldValue3 = next(gen)
# print(yieldValue3)

# yieldValue4 = next(gen)
# print(yieldValue4)
print('----------')
for e in gen:
    print('======',e)

g = (x*x for x in [1,2,3,4,5])
print(type(g))
for v in g:
    print(v)

def fib():
    a,b = 1,1
    while True:
        yield a
        a,b = b,a+b
g = fib()
print('---------------')
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))