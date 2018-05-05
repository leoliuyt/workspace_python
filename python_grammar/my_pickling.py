import pickle
d = {'name':'Bob','age':20,'score':88}
# dbytes = pickle.dumps(d)
# print(dbytes)

# f = open('dump.txt','wb')
# pickle.dump(d,f)
# f.close()

f = open('dump.txt','rb')
d = pickle.load(f)
f.close()
print(d)