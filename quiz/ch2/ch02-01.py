def rec(n):
    if n==1:
        return 0
    else:
        k=5*rec(n-1)+3
        return k

n=int(input())
print(rec(n))