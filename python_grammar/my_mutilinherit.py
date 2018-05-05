class Animal(object):
    pass

#哺乳动物
class Mammal(Animal):
    pass

#鸟类
class Bird(Animal):
    pass

# class Dog(Mammal):
#     pass
# class Bat(Mammal):
#     pass

class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

class RunalbeMixIn(object):
    def run(self):
        print('Running……')
class FlyableMixIn(object):
    def fly(self):
        print('Flying……')

class Dog(Mammal,RunalbeMixIn):
    pass
class Bat(Mammal,FlyableMixIn):
    pass