# 스택
import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = input()
    stack = []
    numberStack = []

    icp = {'*': 2, '+': 1, '(': 3}
    isp = {'*': 2, '+': 1, '(': 0}

    for i in range(N):
        if arr[i].isdigit():
            numberStack.append(arr[i])

        else:
            if not stack:
                stack.append(arr[i])
                continue

            elif stack:
                if arr[i] == ')':
                    while stack[-1] != '(':
                        numberStack.append(stack.pop())
                    stack.pop()

                elif icp[arr[i]] > isp[stack[-1]]:
                    stack.append(arr[i])

                else:
                    while icp[arr[i]] <= isp[stack[-1]]:
                        numberStack.append(stack.pop())
                    stack.append(arr[i])

    for i in range(len(numberStack)):
        if numberStack[i].isdigit():
            stack.append(numberStack[i])

        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())

            if numberStack[i] == "+":
                result = num1 + num2
            elif numberStack[i] == "*":
                result = num1 * num2

            stack.append(str(result))

    print(f'#{tc} {stack[0]}')
