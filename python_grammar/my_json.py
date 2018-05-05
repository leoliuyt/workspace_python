import json
d = {'name':'Bob','age':20,'score':88}
jsonString = json.dumps(d)
print('type:',type(jsonString),'value=',jsonString)

jsonD = json.loads(jsonString)
print('type:',type(jsonD),'value=',jsonD)

class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    
    #相当于重写oc中的description
    def __str__(self):
        return 'Student object(%s,%s,%s)' % (self.name,self.age,self.score)

s = Student('Bob',20,88)
s_json = json.dumps(s,default=lambda obj:obj.__dict__)
print(s_json)

#反序列化
rebuild = json.loads(s_json,object_hook=lambda d:Student(d['name'],d['age'],d['score']))
print('type:',type(rebuild),'value:',rebuild)