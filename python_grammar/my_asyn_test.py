import asyncio,random
@asyncio.coroutine
def smart_fib(n):
    index,a,b = 0,0,1
    while index < n:
        # sleep_secs = random(0,0.2)
        sleep_secs = 0.1
        yield from asyncio.sleep(sleep_secs)
        print('smart one think {} secs to get {}'.format(sleep_secs,b))
        a,b = b,a+b
        index += 1

@asyncio.coroutine
def stupid_fib(n):
    index,a,b = 0,0,1
    while index < n:
        # sleep_secs = random(0,0.4)
        sleep_secs = 0.2
        yield from asyncio.sleep(sleep_secs)
        print('stupid one think {} secs to get {}'.format(sleep_secs,b))
        a,b = b,a+b
        index += 1
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [smart_fib(10),stupid_fib(10)]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished.')
    loop.close()