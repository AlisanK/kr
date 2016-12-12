n=int(input())
Prices=list(map(int,input().split()))
def price(n,Prices):
    cost=[Prices[0],Prices[1]]
    if n>2:
        for i in range(2,n):
            cost.append(min(cost[i-1],cost[i-2])+Prices[i])
    return cost[n-1]
print(price(n, Prices))