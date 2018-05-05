

def enroll(name,gender,age=6,city='Beijing'):
    print("name:",name)
    print("gender:",gender)
    print("age:",age)
    print("city:",city)

enroll("Jack","man",city="Shanghai")

#可变参数
def calc(*numbers):
    print(type(numbers))#<class 'tuple'>
    sum = 0
    for x in numbers:
        sum += x
    return sum

sum = calc(1,2,3,4,5,6,7)
print("sum = ",sum)

# 关键字参数
def person(name,age,**kw):
    print(type(kw))
    print('name:', name, 'age:', age, 'other:', kw)

person('leo','18',city='Beijing')

extra = {'city':'Beijing','job':'Engineer'}

person('leo','18',**extra)

#命名关键字参数

def nameKeyword(name,age,*,city,job):
    print('name: ', name, 'age: ', age, 'city: ', city,'job: ',job)
nameKeyword('leo','20',city='Shanghai',job='Engineer')

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：

def nameKWWithArgs(name,age,*args,city,job):
    print(type(args))
    print('name: ', name, 'age: ', age, 'city: ', city,'job: ',job)

extraArr = [1,2,3,4]
nameKWWithArgs('leoliu','18',*extraArr,city = 'Yantai',job = 'Engineer')

extraDic = {'city':'Beijing','job':'Engineer'}
nameKeyword('leoliuyt',18,**extraDic)