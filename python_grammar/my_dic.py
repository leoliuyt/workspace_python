d = {"Michael" : 95, 'Bob': 75,'Tracy': 85}
d['Jack'] = 90
print(d)

# ict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
d.get("Jack")
d.get("Aha",-1)
