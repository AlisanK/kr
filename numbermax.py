max = 0
count = 1
s = map( int, input().split())
for i in s:
    if i>max:
        max = i
        count = 1
    elif i == max:
        count+=1
print(count)