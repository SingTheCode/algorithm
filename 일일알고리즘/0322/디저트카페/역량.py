# 재귀
import sys

sys.stdin = open('sample_input.txt')


def DFS(si, sj):
    global visited
    global max_eat

    check_item = []
    sum_eat = 0
    stack = [(si, sj)]
    while stack:
        ci, cj = stack.pop()
        if not visited[ci][cj]:
            visited[ci][cj] = 1
            sum_eat += arr[ci][cj]
            check_item.append(arr[ci][cj])

            for k in range(4):
                ni = ci + di[k]
                nj = cj + dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    if ni == si and nj == sj:
                        max_eat = max(max_eat, sum_eat)
                    if not arr[ni][nj] in check_item and not visited[ni][nj]:
                        stack.append((ni, nj))
                    else:
                        sum_eat -= arr[ci][cj]


T = int(input())

di = [-1, 1, 1, -1]
dj = [1, 1, -1, -1]

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * 4 for _ in range(N)]
    max_eat = 0

    for i in range(N):
        for j in range(N):
            DFS(i, j)

# 학생 풀이
# def moving(d, y, x, cnt):       # 움직이기
#     ny = y + dy[d]
#     nx = x + dx[d]
#     if 0 <= ny < n and 0 <= nx < n and visited[arr[ny][nx]] == 0:
#         visited[arr[ny][nx]] = 1        # 방문 표시
#         recur(d, ny, nx, cnt + 1, 1)
#         visited[arr[ny][nx]] = 0        # 재귀를 빠져 나오면 방문 표시 제거
#
#
# def recur(cur, y, x, cnt, move):
#     global max_cnt
#     if cur == 3 and i == y:             # 사각형 완성했을 때
#         max_cnt = max(max_cnt, cnt)     # 최댓값 업데이트
#         return
#     if cur == 2 and max_cnt > cnt * 2:  # 가지치기 두 변의 길이가 현재 값보다 작으면 return
#         return
#     if cur == 2 and i + j == y + x:     # 두 변을 그린 후부터는 변의 길이에 맞춰 잇는다.
#         recur(cur + 1, y, x, cnt, 0)    # 마지막 세번째 꺾고 시작점으로 잇는다.
#         return
#     # 가던 방향으로 움직인다.
#     moving(cur, y, x, cnt)
#     # 방향 전환 - 2번까지 임의로 꺾고 3번부터는 사각형을 그리니 임의로 꺾지 않는다.
#     if cur < 2 and move:    # 한 번이라도 움직였을 때 꺾는다.
#         recur(cur + 1, y, x, cnt, 0)
#
#
# dy = [1, 1, -1, -1]     # 움직일 순서 : 오른쪽 아래, 왼쪽 아래, 왼쪽 위, 오른쪽 위
# dx = [1, -1, -1, 1]
# for tc in range(1, 1 + int(input())):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     visited = [0 for _ in range(101)]       # 중복 확인하기 위함
#     max_cnt = 0                             # 출력할 결과
#
#     for i in range(n):          # 모든 점에서 start
#         for j in range(n):
#             recur(0, i, j, 0, 0)
#
#     if max_cnt == 0:            # 사각형을 그릴 수 없으면 -1 출력
#         print(f'#{tc} -1')
#     else:
#         print(f'#{tc} {max_cnt}')


# 교수님 풀이
# def DFS(n, ssum):
#     global ans
#     if n > 12:
#         if ans > ssum:
#             ans = ssum
#         return
#
#     DFS(n + 1, ssum + lst[n] * day)  # 일일권
#     DFS(n + 1, ssum + mon)  # 월간
#     DFS(n + 3, ssum + mon3)  # 분기
#     DFS(n + 12, ssum + year)  # 년간
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     day, mon, mon3, year = map(int, input().split())
#     lst = [0] + list(map(int, input().split()))
#     # ans = 12345678
#     # DFS(1, 0)
#     # print(f'#{test_case} {ans}')
#     D = [0] * 13
#     for i in range(1, 13):
#         mmin = D[i - 1] + lst[i] * day
#         mmin = min(mmin, D[i - 1] + mon)
#         if i >= 3:
#             mmin = min(mmin, D[i - 3] + mon3)
#         if i >= 12:
#             mmin = min(mmin, D[i - 12] + year)
#         D[i] = mmin
#     print(f'#{test_case} {D[12]}')