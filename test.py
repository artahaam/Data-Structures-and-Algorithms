test = [1]
print(id(test))
test += [1,]
print(id(test))
for i in range(200):
    test += [i, ]
print(id(test))
print(test)