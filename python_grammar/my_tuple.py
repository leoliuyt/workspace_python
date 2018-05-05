# tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy', 'Adam', 'Adam')
print(classmates[0])

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)

# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。

