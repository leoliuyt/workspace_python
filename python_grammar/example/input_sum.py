# -*- coding:UTF-8 -*-
print('求两个数之和')
numStr1= input('第一个数:')
numStr2= input('第二个数:')
numStr3=str(float(numStr1) + float(numStr2))
# print('%s + %s = %s' % (numStr1,numStr2,numStr3)) 
print('{0} + {1} = {2}'.format(numStr1,numStr2,numStr3))