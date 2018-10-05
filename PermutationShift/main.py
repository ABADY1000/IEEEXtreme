



size = int(input())
data = [int(x) for x in input().split()]

def elementPosition(lis):
    arrayp=[]
    for i,x in enumerate(lis):
        destance=size-(i+1)+x
        if destance>=size:
            destance-=size
        arrayp.append(destance)
    return arrayp

if __name__ == '__main__':

    aways = elementPosition(data)

    biggest = max(aways)
    count = []
    for x in range(biggest+1):
        count.append(aways.count(x))

    print(max(count))

    