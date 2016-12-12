s = map(int, input().split())
D = dict()
for i in s:
    if i in D:
        D[i]+=1
    else:
        D[i]=1

D2 = sorted(D.items(), key= lambda item: item[1])
print(D)

counter = 0
for key in D.keys():
    if D[key] == D2[-2][1]:
        counter +=1

print(counter)