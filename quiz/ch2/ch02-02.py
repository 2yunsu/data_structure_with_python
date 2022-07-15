a = 0
li=[]
def seq(n):
    if (n==1):
        return 1
    else:
        list.append(li,1)
        print(len(li))
        return seq(n-1)+3

print(seq(10))
