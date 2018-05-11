class SayMetaClass(type):
    def __new__(cls,name,bases,attrs):
        print('cls:',cls,'name:',name,'bases:',bases,'attrs:',attrs)
        attrs['say_'+name] = lambda self,value,saying=name:print(saying+','+value+'!')
        return type.__new__(cls,name,bases,attrs)
class Hello(object,metaclass = SayMetaClass):
    pass
hell = Hello()
hell.say_Hello('Python')

class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda a,value:a.append(value)
        return type.__new__(cls,name,bases,attrs)
class MyList(list,metaclass=ListMetaclass):
    pass
L = MyList()
L.add(1)
print(L)