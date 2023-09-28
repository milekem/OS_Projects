import numpy as np
import csv

capacity = 7
referenceString = np.random.randint(20, size=1000)
print(referenceString)
memory = {}
recentlyUsed = []
toDelete = []
globalTimer = 0
pageFault = 0
pageHit = 0
usageCounter = 0

for i in referenceString:
    if len(memory) < capacity:
        # If there's space in memory and the page is not in memory, add it.
        if i not in memory:
            memory[i] = 1
            print("Page fault!", memory)
            pageFault += 1
            recentlyUsed.append(i)
            print(recentlyUsed)
        else:
            # If the page is already in memory, update its usage.
            memory[i] += 1
            j = recentlyUsed.index(i)
            del recentlyUsed[j]
            recentlyUsed.append(i)
            print("Page hit!", memory)
            print(recentlyUsed)
            pageHit += 1
    elif len(memory) >= capacity:
        # If memory is full and the page is not in memory, replace a page.
        if i not in memory:
            temp = min(memory.items(), key=lambda x: x[1])
            for item in memory.items():
                if item[1] == temp[1]:
                    toDelete.append(item)
            if len(toDelete) > 1:
                toDelete = sorted(toDelete, key=lambda x: x[1])
                del memory[toDelete[0][0]]
                j = recentlyUsed.index(toDelete[0][0])
                del recentlyUsed[j]
                toDelete = []
            else:
                j = recentlyUsed.index(toDelete[0][0])
                del recentlyUsed[j]
                del memory[toDelete[0][0]]
                toDelete = []

            memory[i] = 1
            recentlyUsed.append(i)
            print(recentlyUsed)
            print("Page fault!", memory)
            pageFault += 1
        else:
            # If the page is in memory, update its usage.
            j = recentlyUsed.index(i)
            del recentlyUsed[j]
            recentlyUsed.append(i)
            memory[i] += 1
            print("Page hit!", memory)
            pageHit += 1
            print(recentlyUsed)

print("Hits:", pageHit, "Faults:", pageFault)
