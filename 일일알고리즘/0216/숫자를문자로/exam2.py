import sys
sys.stdin = open("input.txt")

def itoa(number, numArr):
    while number > 0:
        rest = number % 10
        number = number // 10
        numArr.append(rest)
    for i in range(len(numArr)):
        numArr[i] = chr(numArr[i] + 48)

T = int(input())
for tc in range(1, T+1):
    result = ""
    numArr =[]
    number = int(input())

    if number < 0:
        result += "-"
        number = abs(number)
    itoa(number, numArr)
    for i in range(len(numArr)):
        result += numArr[len(numArr) - i - 1]
    print(f'#{tc} {result} {type(result)}')
