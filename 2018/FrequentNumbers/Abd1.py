
# Number of repetitions
reps = [int(x) for x in input().split()]

# The data
data = [int(x) for x in input().split()]

# Already used numbers
used = []
#The number of reps for each number
results = []

# Look for each number and aff
for x in data:
    if x not in used:
        #
        used.append(x)
        results.append(data.count(x))

counter = 0
# print(results)
# print(used)
for x in reps:
    counter += results.count(x)                                                                                                

print(counter)
    