class A(object):
    def __init__(self,name):
        self.name = name

    # 存在的属性不会走该方法，调用不存在的属性才会走
    def __getattr__(self,n):
        print('__getattr__',n)
        return "aa"
    # 属性存不存在都会走
    def __setattr__(self,n,value):
        print('n = %s value = %s' % (n,value))
a = A('leoliu')
# print(a.name)
# print(a.b)
# a.name = 'hhh'
a.cc = 'leo'