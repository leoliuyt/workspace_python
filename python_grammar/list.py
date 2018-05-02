classmates = ['Michael','Bob','Tracy']

print(classmates)
print("list length = %d" % len(classmates))

print(classmates[0])
print(classmates[-1])

# 方法
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
classmates.append("Adam")
classmates.append("Adam")
print("append = :",classmates)
# classmates.clear()
# print("clear = :",classmates)
# print(help(classmates.count))
print("传入值在list中出现的次数count = :",classmates.count("Adam"))

ita = ["a","b"]
classmates.extend(ita)
print("追加元素extend:",classmates)

print("index :",classmates.index("Adam"))#3
classmates.insert(0,"First")
print("insert :",classmates)
print("pop :",classmates.pop(2))

classmates.remove("a")
print("remove :",classmates)
classmates.reverse()
print("reverse :",classmates)
classmates.sort()
print("sort :",classmates)

print("#################")
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
