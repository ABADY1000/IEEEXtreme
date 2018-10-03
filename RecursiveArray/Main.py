
# Not a good solution   


def ListGenerator(lis):

    newArray = []         
    for x in lis:
        newArray.append(lis[x-1])
    return tuple(newArray)


if __name__ == '__main__':
    size = int(input())
    current = tuple([int(x) for x in input().split()])
    output = 1
    data = {current}
    length = len(data)

    while True:
        current = ListGenerator(current)
        data.add(current)

        if len(data) == length:
            break
        else:
            output += 1
            length += 1

    print(output)


