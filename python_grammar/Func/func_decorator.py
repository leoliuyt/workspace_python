import functools
# def log(func):
#     def wrapper(*args,**kw):
#         print('call %s():' % func.__name__)
#         return func(*args,**kw)
#     return wrapper
def log(text):
    def decorator(func):
        # @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s():' % (text,func.__name__))
            return func(*args,**kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = text
        return wrapper
    return decorator

# now = log(now)
# now = log('abcd')(now)
@log('abcd')
def now():
    print('2018-10-11')

f = now
print('f=',f.__name__)
print(f.__method__)
print(f.__route__)

