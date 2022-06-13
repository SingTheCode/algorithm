# 스택
import sys

sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = list(input())
    stack = []
    result = 1

    for i in range(0, len(arr)):
        if arr[i] == '{' or arr[i] == '(':
            stack.append(arr[i])
        if arr[i] == '}':
            if len(stack) == 0:
                result = 0
                break
            if stack.pop() != '{':
                result = 0
                break
        if arr[i] == ')':
            if len(stack) == 0:
                result = 0
                break
            if stack.pop() != '(':
                result = 0
                break
        if i == len(arr) - 1:
            if len(stack) != 0:
                result = 0
                break
    print(f'#{tc} {result}')
