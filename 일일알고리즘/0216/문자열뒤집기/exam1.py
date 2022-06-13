import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    str = list(input())
    for i in range(len(str) // 2):
        str[i], str[len(str) - i - 1] = str[len(str) - i - 1], str[i]
    for i in range(len(str)):
        print(str[i], end="")
    print()