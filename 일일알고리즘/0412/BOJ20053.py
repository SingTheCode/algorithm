# 구현
T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    mmax = max(arr)
    mmin = min(arr)
    print(mmin, mmax)
