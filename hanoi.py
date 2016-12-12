def Hanoi(i,j,n):
    if n==1:
        if i==2 or j==2:
            print("переложить диск с оси " + str(i) + " на ось "+ str(j))
        else:
            print("переложить диск с оси " + str(i) + " на ось 2" "\n" "переложить диск с оси 2" + " на ось "+ str(j))
    elif i==2 or j==2:
        Hanoi(i,6-i-j,n-1)
        print("переложить диск с оси " + str(i) + " на ось "+ str(j))
        Hanoi(6-i-j,j,n-1)
    else:
        Hanoi(i,6-i-j,n-1)
        Hanoi(6-i-j,j,n-1)
        print("переложить диск с оси " + str(i) + " на ось 2")
        Hanoi(j,6-i-j,n-1)
        Hanoi(6-i-j,j,n-1)
Hanoi(1,3,3)