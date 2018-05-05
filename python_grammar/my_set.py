s = set([1,2,3])
print(s)

a = {1,2,3}
b = {2,3,4}
c = a | b
d = a & b
print("c :",c)
print("d :",d)

s.add(4)
s.add(4)

print(s)