UPPER_LIMIT = 10E9

def count_even(number:str):
    number_list = list(number)
    n = 0
    for x in number_list:
        if int(x)%2 == 0:
            n+=1
    return n

def process(n:str):
    alpha = list(n)

    # All the digits are even
    if all([int(x)%2==0 for x in alpha]):
        return 1
    
    # All the digits are odd
    if all([int(x)%2==1 for x in alpha]):
        return -1

    # Any other cases but the above
    evens = count_even(n)
    number = int(n)
    counter_under = 0
    counter_above = 0

    # Count number less then X apply condition
    while count_even(str(number)) >= evens or number < 0:
        counter_under +=1
        number -=1

    number = int(n)
    while count_even(str(number)) >= evens or number > UPPER_LIMIT:
        counter_above +=1
        number +=1

    return counter_above * counter_under

    
    
    
if __name__ == '__main__':
    print(process(input()))
