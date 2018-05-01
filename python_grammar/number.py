import math
add = 1 + 2
print(add)

decrease = 2 - 1
print(decrease)

# python3.6:0.5 
# python2  :0
floatDivide = 1 / 2
print(floatDivide)

# //代表返回整数
intDivide = 1 // 2
print(intDivide) 

# intComplex = 1+2i
floatComplex = complex(1.0,2.0)

print(floatComplex)

powerInt = 5 ** 2
print(powerInt)

# 函数
print("绝对值：abs(-10) = %s" % abs(-10))#10
print("绝对值：fabs(-10) = %s" % math.fabs(-10))#10.0
print("向上取整：ceil(4.1) = %s" % math.ceil(4.1))#5
print("向下取整：ceil(4.9) = %s" % math.floor(4.9))#4
print("返回浮点数x的四舍五入值 round(4.9164,2) = %s" % round(4.9164,2))#4.92
print("最大值：max(10,11,9) = %s" % max(10,11,9))#11
print("最小值：min(10,11,9) = %s" % min(10,11,9))#9
print("返回x的整数部分与小数部分modf(9.12) = " , math.modf(9.12))#(0.11999999999999922, 9.0)
print("x**y 运算后的值pow(2,3) = %s" % pow(2,3))#8
print("e的x次幂：exp(1) = %s" % math.exp(1))#2.718281828459045
print("x的平方根：sqrt(x) = %s" % math.sqrt(9))#3.0
print("log(x) = %s" % math.log(100,10))#2.0
print("log10(x) = %s" % math.log10(100))#2.0

print("pi = %s" % math.pi)#3.141592653589793
print("e = %s" % math.e)#2.718281828459045


