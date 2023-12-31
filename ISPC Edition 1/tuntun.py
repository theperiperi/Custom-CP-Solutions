T = int(input())
for i in range(0, T):
    n, k = map(int, input().split())
    if k == 1:
        print(n)
        continue
    
    ans = 0
    while n > 0:
        power_of_2 = 1
        while power_of_2 * k <= n:
            power_of_2 *= k
        ans += n // power_of_2
        n %= power_of_2
        
    print(ans)
