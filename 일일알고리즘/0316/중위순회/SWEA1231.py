# 중위 순회
import sys

sys.stdin = open('input.txt')


# def in_order(idx):
#     if idx * 2 < V + 1:
#         in_order(idx * 2)
#     print(arr[idx], end="")
#     if idx * 2 + 1 < V + 1:
#         in_order(idx * 2 + 1)
#
#
# for tc in range(1, 11):
#     V = int(input())
#     tmp = []
#     arr = [0]
#
#     for _ in range(V):
#         tmp.append(list(input().split()))
#
#     for i in range(V):
#         arr.append(tmp[i][1])
#
#     print(f'#{tc}', end=" ")
#     in_order(1)
#     print()


# 교수님 풀이
def in_order(v):  # 중위 순회 함수
    if v:
        in_order(tree[v][0])
        res.append(alpha[v])
        in_order(tree[v][1])


def int_chg(char):  # 암시적 형변환시 숫자인 경우만 int로 형변환 하는 함수
    if char.isdecimal():
        return int(char)
    else:
        return char


for tc in range(1, 11):
    V = int(input())

    tree = [[0, 0] for _ in range(V + 1)]  # 1번부터 시작하기 위해
    alpha = [''] * (V + 1)  # 알파벳 저장하기 위한 리스트

    for i in range(V):
        data = list(map(int_chg, input().split()))
        alpha[data[0]] = data[1]  # 알파벳 별도 저장

        for j in range(2, len(data)):  # data의 길이에 따라 유연하게 반복할 수 있는 반복문
            tree[data[0]][j - 2] = data[j]

    res = []  # 결과 저장할 리스트
    in_order(1)  # 루트 정점인 1번 정점부터 중위순회
    print(f'#{tc} {"".join(res)}')
