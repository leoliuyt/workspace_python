a = float(input('a:'))
b = float(input('b:'))
c = float(input('c:'))
import math
# s = (a**2+b**2-c**2)/4
s = math.sqrt((a+b-c)*(a+b+c)*(a-b+c)*(-a+b+c))/4 
print('s = {0}'.format(s))