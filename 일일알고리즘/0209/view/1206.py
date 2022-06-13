import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    result = 0

    for i in range(2, N - 2):
        maxBuilding = 0
        for j in range(i - 2, i):
            if buildings[j] > maxBuilding:
                maxBuilding = buildings[j]
        for j in range(i + 1, i + 3):
            if buildings[j] > maxBuilding:
                maxBuilding = buildings[j]
        if buildings[i] > maxBuilding:
            result += buildings[i] - maxBuilding

    print(f'#{tc} {result}')
