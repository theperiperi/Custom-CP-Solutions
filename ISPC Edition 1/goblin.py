for i in range(int(input())):
    n,k=map(int,input().split())
    set1=set()
    for i in range(n):
        x,y=map(int,input().split())
        y=y+k*x 
        set1.add(y)

    set1=sorted(set1)
    print(len(set1))
    for i in set1:
        print(i,end=" ")
    print()





