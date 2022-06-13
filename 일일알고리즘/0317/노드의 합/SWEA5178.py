# 완전 이진 트리
import sys

sys.stdin = open('sample_input.txt')


def solution(p):
    while p > 0:
        if p * 2 > N:
            tree[p] = 0
        elif p * 2 + 1 > N:
            tree[p] = tree[p * 2]
        else:
            tree[p] = tree[p * 2] + tree[p * 2 + 1]
        p -= 1


T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)

    for _ in range(M):
        index, value = map(int, input().split())
        tree[index] = value

    last = N - M
    solution(last)

    print(f'#{tc} {tree[L]}')
