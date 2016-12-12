x,y = map(int, input().split())
count = 0
while(x!=0 and y !=0 ):
    if x%2==0 and y%7==0 and (x>99 or y>99):
        count+=1
    x,y = map(int, input().split())
print(count)