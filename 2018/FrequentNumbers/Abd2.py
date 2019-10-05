from collections import Counter

f = Counter([1,1,1,1,2,2,5,5,5,5,5,4,4,3,9,8,8,7,7,7,10])


# size = int(input())

# data = []

# for _ in range(size):
#     x = [int(x) for x in input().split()]
#     data.append(tuple(x + [x[1] - x[0]]))

# data = sorted(data,key= lambda x: x[2])
# counter = 0
# for x in range(size-1):
#     for y in range(x+1,size):
#         if data[y][0] < data[x][0] and data[y][1] > data[x][1]:
#             counter += 1
#             break

# print(counter)