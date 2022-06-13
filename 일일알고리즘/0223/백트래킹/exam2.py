# 백트래킹
def f(i, N, K):
    if i == N:
        s = 0
        for j in range(N):
            if bit[j]:
                s += arr[j]
        if s == K:
            for k in range(N):
                if bit[k]:
                    print(arr[k], end=" ")
            print()

    else:
        bit[i] = 1
        f(i + 1, N, K)
        bit[i] = 0
        f(i + 1, N, K)


N = 10
arr = [x for x in range(1, N + 1)]
bit = [0] * N
f(0, N, 10)
