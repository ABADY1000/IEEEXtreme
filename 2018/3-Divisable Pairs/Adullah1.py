
size = int(input())

data = [int(x) for x in input().split()]

def factorial(x):
    return sum(range(x+1))

counter = 0
rest = []

for x in data:
    rest.append(x % 3)

zeros = rest.count(0)
ones = rest.count(1)
twos = rest.count(2)

counter = ones * twos

counter += factorial(zeros-1 )

print(counter)