import logging
logging.basicConfig(level=logging.INFO)
def foo(s):
    n = int(s)
    # print('>>> n = %d' % n)
    logging.info('n = %d' % n)
    return 10 / n

def main():
    foo('0')

main()