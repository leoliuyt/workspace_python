# import io
# try:
#     f = open('/Users/lbq/Documents/公司文档/首创教育云1046','r')
# finally:
#     print('finally')
#     if f:
#         f.close()

with open('/Users/lbq/Documents/公司文档/首创教育云1046','r') as f:
    # print(f.read())
    # fileContent = f.read()
    # print(fileContent)
    for line in f.readlines():
        print(line)

