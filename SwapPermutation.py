# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)   

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy

def swap(A, a, b):
    A[a-1], A[b-1] = A[b-1], A[a-1]


def main():
    N = get_number()
    M = get_number()
    K = get_number()

    pairs = []
    for _ in range(M):
        a = get_number()
        b = get_number()
        pairs.append((a,b))

    # Program starts here
    perm = list(range(1, N+1))

    print(perm)
    
    for p in pairs:
        swap(perm, p[0], p[1])


    print(perm)
    





if __name__ == "__main__":
    # main()

    d = []
    while 1:
        try:
            # if len(d) > 20:
            print(get_number())
        except :
            break

    print("Done reading data...")
    print(d)
