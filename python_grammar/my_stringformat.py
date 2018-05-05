string = "{0} {1}!".format("Hello","Mars")

welcome = {"action":"Hello","name":"Mars"}
stringA = "{action} {name}!".format(**welcome)
# print(help(string.format))
print(stringA)
