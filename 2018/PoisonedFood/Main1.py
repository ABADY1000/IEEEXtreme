
portions_size = int(input())

portions = []
poisoned = []
danger_rate = []

max_dr = 1
max_i = 0
for x in range(portions_size):
    por, poi = (int(x) for x in input().split())
    dr = poi/por
    if max_dr > dr:
        max_dr = dr
        max_i = x+1
    
print(max_i)
    




