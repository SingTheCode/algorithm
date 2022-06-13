# 재귀
# 학생 풀이
import sys

sys.stdin = open('sample_input.txt')


def recur(cur, fee):
    global min_fee
    if fee >= min_fee:  # 현재 요금이 업데이트 된 최소 요금보다 비싸면 return
        return
    if cur >= 12:  # 12개월을 넘어서는 경우
        min_fee = min(min_fee, fee)  # 최소값 업데이트
        return

    if arr[cur] == 0:
        recur(cur + 1, fee)  # 이용하지 않으면 다음 월로 이동
    else:
        recur(cur + 1, fee + day * arr[cur])  # 당일 요금은 이용 일만큼 곱한다.
        recur(cur + 1, fee + mon)  # 월 요금만 더하면 된다.
        recur(cur + 3, fee + mon_3)  # 3달은 3달을 더해줘야 한다.


for tc in range(1, 1 + int(input())):
    day, mon, mon_3, year = map(int, input().split())
    arr = list(map(int, input().split()))
    min_fee = year  # 1년 요금은 처음에 넣고 최솟값으로 업데이트
    recur(0, 0)
    print(f'#{tc} {min_fee}')

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