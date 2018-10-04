
# Abdullah 
# Not a good solution

from time import time

begun = False
start = 0
end = 0

def FindTime(name):

    if begun:
        end = time()
        begun = False
        print("{} time is: {}".format(name,end - start))
    else:
        start = time()
        begun = True


def ListGenerator(lis):

    newArray = []         
    for x in lis:
        newArray.append(lis[x-1])
    return tuple(newArray)


if __name__ == '__main__':
    
    Data = open('D:\\programming\\Coders2030\\RecursiveArray\\Data.txt', mode='r')

    # size = int(input())
    size = int(Data.readline())
    current = tuple([int(x) for x in Data.readline().strip().split()])
    output = 1
    data = [current]
    length = len(data)
    sequent_rep = False

    seq_rep = False
    existence = False

    uniqe = []
    number_to_generate = 10

    while(True):

        x = {12:15,6:8}
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
