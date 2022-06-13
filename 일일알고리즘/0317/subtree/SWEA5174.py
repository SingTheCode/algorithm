# 이진 트리
import sys

sys.stdin = open('sample_input.txt')


def pre_order(v):
    global cnt
    if v:
        cnt += 1
        pre_order(ch1[v])
        pre_order(ch2[v])


T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    cnt = 0

    for i in range(E):
        if ch1[arr[i * 2]] == 0:
            ch1[arr[i * 2]] = arr[i * 2 + 1]
        else:
            ch2[arr[i * 2]] = arr[i * 2 + 1]

    pre_order(N)
    print(f'#{tc} {cnt}')
