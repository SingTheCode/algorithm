# 이진 탐색
import sys

sys.stdin = open('sample_input.txt')


# 교수님 풀이
def in_order(node):
    global value

    if node <= N:
        in_order(node * 2)
        tree[node] = value
        value += 1
        in_order(node * 2 + 1)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    value = 1

    tree = [0] * (N + 1)
    in_order(1)
    print(f'#{tc} {tree[1]} {tree[N // 2]}')
