# 그리디
import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))

    result = 0

    containers.sort(reverse=True)
    trucks.sort(reverse=True)

    for container in containers:
        for truck in trucks:
            if container <= truck:
                result += container
                trucks.pop(0)
                break

    print(f'#{tc} {result}')
