# 전위, 중위, 후위 순회, 이진트리
import sys

sys.stdin = open('input.txt')
V = int(input())
arr = list(map(int, input().split()))


def pre_order(v):
    if v:
        print(v, end=" ")
        pre_order(ch1[v])
        pre_order(ch2[v])


def in_order(v):
    if v:
        in_order(ch1[v])
        print(v, end=" ")
        in_order(ch2[v])


def post_order(v):
    if v:
        post_order(ch1[v])
        post_order(ch2[v])
        print(v, end=" ")


E = V - 1

ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)

for i in range(E):
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:
        ch1[p] = c
    else:
        ch2[p] = c

print('전위 순회 :', end=" ")
pre_order(1)
print()
print('중위 순회 :', end=" ")
in_order(1)
print()
print('후위 순회 :', end=" ")
post_order(1)
print()
