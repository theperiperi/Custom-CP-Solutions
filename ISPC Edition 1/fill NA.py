for i in range(int(input())):
    mean,median,rows=map(int,input().split())
    #rows must be greater than 1
    #median should be less than = mean*rows
    
    if rows==1:
        if median==mean:
            print("YES")
        else:
            print("NO")
    else:
        minm=median+((1+median)*(rows-1)//2)
        if minm<mean*rows:
            print("YES")
        else:
            print("NO")
