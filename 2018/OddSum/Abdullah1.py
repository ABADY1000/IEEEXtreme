

size = int(input())

data = [int(x) for x in input().split()]

# dataset = set(data)

isOdd = []

for x in data:
    isOdd.append(x%2 == 1)

counter = 0
for x in range(len(isOdd)):
    if isOdd[x] == True:
        counter += isOdd[x+1:].count(False)
    elif isOdd[x] == False:
        counter += isOdd[x+1:].count(True)

print(counter)
