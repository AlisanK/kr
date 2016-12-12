mas=list(map(int,input().split()))
c = 0
for n in range(0,len(mas)):
    for i in range(len(mas)-n):
        if mas[i] > mas[i+1]:
            mas[i],mas[i+1] = mas[i+1],mas[i]
            c += 1
print(c)