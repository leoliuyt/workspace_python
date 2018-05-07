# def yieldTest():
#     i = 1
#     while i < 4:
#         print('[yieldtest]:',i)
#         n = yield i 
#         print('n = ',n)
#         if i == 3:
#             return 100
#         i += 1

# def itest():
#     val = yield from yieldTest()
#     print('[itest]:',val)

# t = itest()
# print(type(t))
# t.send(None)
# j = 6
# while j >= 3:
#     j -= 1
#     try:
#         print('send',j)
#         t.send(j)
#         nv = next(t)
#         print('next value =',nv)
#     except StopIteration as e:
#         print('异常了')

# def gen():
#     value = 0
#     i = 0
#     while i < 10:
#         print('yield before：',i)
#         #receive 从send接收到的值
#         # value 返回给next的值
#         receive = yield value
#         print('yield after：%s receive:%s value:%s',(i,receive,value))
#         if receive == 'e':
#             break
#         value = 'got:i = %s receive = %s' % (i,receive)
#         i += 1
# g = gen()
# print('--------')
# print(g.send(None));
# # g.send('hello')
# print('--------')
# print(g.send('hello'))
# print('--------')
# print(g.send('python'))
# print('--------next:')
# print('next0 = ',next(g))
# print('--------')
# print('next1 = ',next(g))
# print('--------')
# print('next2 = ',next(g))

def g1():     
     yield range(5)
def g2():
     yield  from range(5)

it1 = g1()
it2 = g2()
print(type(it1))
print(type(it2))
print('------------')
for x in it1:
    print(x)
print('------------')
for x in it2:
    print(x)

