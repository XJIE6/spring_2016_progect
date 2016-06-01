n = 3

print("--------------")
set1 = [[] for i in range(0, n)]
for i in range(0, n) :
    set1[i] = set((km1.labels_ == i).nonzero()[0])
    print(len(set1[i]))
print("--------------")
set2 = [[] for i in range(0, n)]
for i in range(0, n) :
    set2[i] = set((km2.labels_ == i).nonzero()[0])
    print(len(set2[i]))

print("--------------")
set3 = [[] for i in range(0, n)]
for i in range(0, n) :
    set3[i] = set((km3.labels_ == i).nonzero()[0])
    print(len(set3[i]))

print("--------------")
for i in range(0, n) :
    for j in range(0, n) :
        print ('('+ str(i) + ', ' + str(j) + ') ' + str(len(set1[i].intersection(set2[j])) / len(set1[i].union(set2[j]))))


for i in range(0, n) :
    for j in range(0, n) :
        print ('('+ str(i) + ', ' + str(j) + ') ' + str(len(set1[i].intersection(set3[j])) / len(set1[i].union(set3[j]))))
