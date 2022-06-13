# 구현
visited = [1] * 31

for i in range(28):
    N = int(input())
    visited[N] = 0

for j in range(1, 31):
    if visited[j] == 1:
        print(j)
