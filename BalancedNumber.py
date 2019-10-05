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


def main():
    
    word = get_word()

    L = len(word)
    if  L % 10 != 0:
        print(0)
        return

    C = L // 10
    word_int = [int(n) for n in word]
    A = 45 * C
    R = sum(word_int)

    if A == R:
        print(1)
        return

    print(0)
    return

if __name__ == "__main__":
    main()