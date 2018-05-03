def normalize(name):
    return name.capitalize()

l = ['adam', 'LISA', 'barT']

l2 = list(map(normalize,l))

print(l2)

from functools import reduce      
def prod(L):
    return reduce(lambda x,y:x*y,L)

numberL = [3, 5, 7, 9]
result = prod(numberL)
print(result)

#filter
#回数
# from math import ceil
import math
def is_palindrome(n):
    numberStr = str(n)
    length = len(numberStr)
    index = math.ceil(length/2.)
    if numberStr[:length//2] == numberStr[index:]:
        return True
    else:
        return False
output = filter(is_palindrome, range(1, 10000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')