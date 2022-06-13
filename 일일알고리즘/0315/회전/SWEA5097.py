# 큐
import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    for _ in range(M):
        tmp = queue.pop(0)
        queue.append(tmp)

    print(f'#{tc} {queue[0]}')
