def is_number(a):
    for i in range(10):
        if str(a) == str(i):
            return True
    return False
def into_10(a,n):
    res=0
    for i in range(len(a)):
        c=a.pop()
        if not is_number(c):
            c=ord(str(c))-55
        res+=int(c)*(n**i)
    return res
def into_k(a,k):
    res = []
    while a>0:
        c=a%k
        if not is_number(c):
            c=chr(c+55)
        res.append(c)
        a //= k
    for i in res[::-1]:
        print(i, end="")
n, a, k = map(str, input().split())
a=list(a)
n,k=int(n),int(k)
if n!=10:
    b=into_10(a,n)
else:
    b=int(a)
if k==10:
    print(b)
else:
    into_k(b,k)
