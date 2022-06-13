# 구현

def solution(state, a, b, arr):
    if state == 1:
        arr[a] = b
    elif state == 2:
        for i in range(a, b + 1):
            if arr[i] == 0:
                arr[i] = 1
            else:
                arr[i] = 0
    elif state == 3:
        for i in range(a, b + 1):
            arr[i] = 0
    else:
        for i in range(a, b + 1):
            arr[i] = 1


N, M = map(int, input().split())
arr = [0]
arr += list(map(int, input().split()))

for _ in range(M):
    state, a, b = map(int, input().split())
    solution(state, a, b, arr)

print(' '.join(map(str, arr[1:])))
