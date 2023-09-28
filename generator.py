import numpy as np

i: int = 1000  #ilosc procesow do wygenerowania

p = []
at = []
bt = []
for a in range(0, i):
    p.append(a)
    bt.append(int(np.random.normal(loc=30,scale=5, size=1))) #(int(np.random.randint(1, 20)))
    at.append(int(np.random.randint(1, 500)))#(int(np.random.randint(1, 500)))#(int(np.random.normal(loc=10,scale=5, size=1)))


with open('test.csv', 'w') as f:    #zapisanie danych do pliku
    f.write("%s,%s,%s\n" % ('pNumber', "burstTime", "arrivalTime"))
    for i in range (0, i):
        f.write("%s,%s,%s\n"%(p[i],bt[i],at[i]))