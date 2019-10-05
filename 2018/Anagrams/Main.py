size = int(input())

words = []
simies = []

for _ in range(size):
    words.append(input())

max_c = 0

i = 0
while len(words) is not 0:
    counter = 0
    a = list(words[0])
    a.sort()
    simies.append([])

    j = 1
    while j < len(words): 
    
        b = list(words[j])
        b.sort()

        if a == b:
            simies[i].append(words.pop(j))
            continue
        j+=1
        
    
    simies[i].append(words.pop(0))  
    i += 1
    
numbers = [len(x) for x in simies]
  
print(max(numbers))

