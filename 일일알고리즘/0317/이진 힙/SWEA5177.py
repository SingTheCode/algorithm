# 최소 힙
import sys

sys.stdin = open('sample_input.txt')


def enq(n):
    global last
    last += 1
    tree[last] = n
    c = last
    p = c // 2
    while p >= 1 and tree[p] > tree[c]:
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c // 2


def solution():
    global result
    c = last
    while c >= 1:
        p = c // 2
        result += tree[p]
        c = p


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    tree = [0] * (1000001)
    last = 0
    result = 0

    for i in range(N):
        enq(arr[i])
    solution()
    print(f'#{tc} {result}')
