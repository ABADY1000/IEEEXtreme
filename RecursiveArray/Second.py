
# Abdullah 
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
    data = [current]
    length = len(data)
    sequent_rep = False

    seq_rep = False
    existence = False

    uniqe = []
    number_to_generate = 10

    while(True):
        for _ in range(number_to_generate):
            data.append(ListGenerator(data[-1]))
            if data[-1] == data[-2]:
                sequent_rep = True
                break
           
        # Repetition Checker
        if sequent_rep:
            seq_rep = True
            break

        # Exestience Checker
        last = data[-1]
        if last in data[:-1]:
            existence = True
            break

    if seq_rep:
        uniqe = data[:-1]
    elif existence:
        uniqe = set()
        for x in data:
            if x in uniqe:
                break
            uniqe.add(x)
        
    print(len(uniqe))
