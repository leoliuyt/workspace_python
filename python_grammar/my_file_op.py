import os
#操作系统类型 
# posix :Linux、Unix或Mac OS X
# nt :windows
print(os.name)
# 获取操作系统详细信息
print(os.uname())
# 操作系统的环境变量
# print(os.environ)
print(os.environ.get('PATH'))

# 查看当前目录的绝对路径
print(os.path.abspath('.'))
#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
path = os.path.join('/Users/lbq/Documents','testdir')
# 创建目录
# os.mkdir(path)
# 删掉一个目录:
# os.rmdir(path)

tupleData = os.path.split('/Users/lbq/Documents')
print(tupleData)

tupleData2 = os.path.splitext('/path/to/file.txt')
print(tupleData2)
#对文件重命名
# os.rename('abc.txt','cba.txt')
#删除文件
# os.remove('cba.txt')
filelist = [x for x in os.listdir('.') if os.path.isdir(x)]
print('当前目录下所有文件夹:',filelist)

pyfilelist = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

print("当前目录下所有.py文件:",pyfilelist)

