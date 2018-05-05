from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('Python!')

print(f.getvalue())

ff = StringIO('Hello!\nHi!\nGoodbye!')
for line in ff.readlines():
    print(line)
# while True:
#     s = ff.readline()
#     if s == '':
#         break
#     print(s.strip())
    