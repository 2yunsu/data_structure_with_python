li=[]
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        list.append(li,0)
        print(len(li))
        return fib(n-1)+fib(n-2)

print(fib(5))