UPPER_LIMIT = 10E9

def count_even(number:str):
    number_list = list(number)
    n = 0
    for x in number_list:
        if int(x)%2 == 0:
            n+=1
    return n

#TODO: Enter the (n) in reverse order... and then continue your great function
def first_even(n:str):
    ''' Return the index of first even number, Note:( indexing returned is reversed - minus sign -) '''
    n = n[-1::-1]
    for i,x in enumerate(n):
        if int(x)%2==0:
            return -1 

def process(n:str):
    alpha = list(n)
    

    # All the digits are even
    if all([int(x)%2==0 for x in alpha]) or int(n)%2==0:
        return 1
    
    # All the digits are odd
    if all([int(x)%2==1 for x in alpha]):
        return -1

    # Any other cases but the above
    evens = count_even(n)
    number = int(n)
    counter_under = 0
    counter_above = 0
    f_e_place = first_even(n)

    if True:
        new_str = n[f_e_place:]
        new_num = int(new_str)
        counter_under = new_num + 1
        counter_above = pow(10,len(new_str)) - new_num + int('1'*len(new_str))

        #TODO: Here I have stopped
    else:
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
