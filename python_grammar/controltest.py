#!/usr/local/bin/python3
inputStrH = input("请输入身高(m):")
inputStrW = input("请输入体重(kg):")

h = float(inputStrH)
w = float(inputStrW)
bim = w / (h**2)
print(bim)
if bim < 18.5:
    print("过轻")
elif bim >= 18.5 and bim < 25:
    print("正常")
elif bim >= 25 and bim < 28:
    print("正常")
elif bim >= 28 and bim < 32:
    print("肥胖")
else:
    print("严重肥胖")