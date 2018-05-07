def consumer():
    r = ''
    while True:
        print('----------------')
        n = yield r 
        if not n:
            print('return了')
            return
        print('[CONSUMER] Consuming %s……' % n)
        r = '200 OK'
def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print('[PRODUCER] Producing %s……' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
