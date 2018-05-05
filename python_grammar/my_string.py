stringInDoubleQuotes = "Hello Python!"

stringInSingleQuotes = ' Hello Python! '

stringInTripleQuotes = '''Hello Python ！
This might be a long string
going through mutiple lines.
'''

print(stringInDoubleQuotes)
print(stringInSingleQuotes)
print(stringInTripleQuotes)


aNumber = 123
aString = str(aNumber)
print(aString)

welcome = stringInDoubleQuotes + stringInSingleQuotes
print(welcome)

upperStr = welcome.upper()
lowerStr = welcome.lower()

print(upperStr+lowerStr)

stripeStr = stringInSingleQuotes.strip()
print(stripeStr)

print(dir(stripeStr))

# print(help(stripeStr.count))

# //[start ..< end]
print(stringInDoubleQuotes[0:7])

print("Hello %s" % "Mars")

print("PI:%f" % 3.14)

print("PI: %.2f" % 3.14)

welcomeDic = {"action":"Hello","name":"Mars"}
print("%(action)s %(name)s!" % welcomeDic)