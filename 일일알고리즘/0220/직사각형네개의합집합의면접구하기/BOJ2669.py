import sys
sys.stdin = open("input.txt")
result = 0

arr = [[0]*100 for _ in range(100)]

for _ in range(4):
    startX, startY, endX, endY = map(int, input().split())
    for i in range(startX, endX):
        for j in range(startY, endY):
            if arr[i][j] == 0:
                arr[i][j] = 1
                result += 1

print(result)