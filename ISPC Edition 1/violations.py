def count_inversions(n,arr):
    inv_count = 0

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                inv_count += 1

    return inv_count

for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    violations = count_inversions(n,arr)
    print(violations)
