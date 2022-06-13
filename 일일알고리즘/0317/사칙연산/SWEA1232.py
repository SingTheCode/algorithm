# 이진 트리
import sys

sys.stdin = open('input.txt')


def is_order(v):
    if v:
        is_order(ch1[v])
        is_order(ch2[v])
        solution(values[v])


def solution(item):
    global stack

    if str(type(item)) != "<class 'int'>":
        value2 = stack.pop()
        value1 = stack.pop()
        if item == '+':
            stack.append(value1 + value2)
        elif item == '-':
            stack.append(value1 - value2)
        elif item == '*':
            stack.append(value1 * value2)
        else:
            stack.append(value1 / value2)
    else:
        stack.append(item)


def change_tmp(char):
    if char.isdecimal():
        return int(char)
    else:
        return char


for tc in range(1, 11):
    N = int(input())
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    values = [0] * (N + 1)
    stack = []

    for i in range(N):
        tmp = list(map(change_tmp, input().split()))
        if len(tmp) == 4:
            index, value, ch1_index, ch2_index = tmp
            ch1[index] = ch1_index
            ch2[index] = ch2_index
            values[index] = value
        else:
            index, value = tmp
            values[index] = value

    is_order(1)
    result = int(stack.pop())
    print(f'#{tc} {result}')
