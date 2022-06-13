import sys

sys.stdin = open("sample_input.txt")


def checkPalindrome(i, j, M, arr, isCol):
    for k in range(0, M // 2 + 1):
        if isCol:
            if arr[i][j + k] != arr[i][j + M - k - 1]:
                return False
        else:
            if arr[i + k][j] != arr[i + M - k - 1][j]:
                return False
        if k == M // 2:
            return True

T = int(input())
for tc in range(1, T + 1):
    result = ""

    isChecked = False

    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N - M + 1):
            if checkPalindrome(i, j, M, arr, True):
                for l in range(j, j + M):
                    result += arr[i][l]
                    isChecked = True
        if isChecked:
            break
    for j in range(N):
        for i in range(N - M + 1):
            if checkPalindrome(i, j, M, arr, False):
                for l in range(i, i + M):
                    result += arr[l][j]
                    isChecked = True
        if isChecked:
            break

    print(f'#{tc} {result}')

    ## 은석님 풀이
    # if arr == arr[::-1]

    #교수님 풀이
    # def is_palindrome(word):
    #     idx = 0
    #     while idx + M - 1 < N:
    #         pali = word[idx:idx + M]
    #         if pali == pali[::-1]:
    #             return pali
    #         idx += 1
    #     return False
    #
    # for i in range(N):
    #     tmp = ''
    #     for j in range(N):
    #         tmp += arr[j][i]
    #     result = is_palindrome(tmp)
    #     if result:
    #         break
    #     result = is_palindrome(arr[i])
    #     if result:
    #         break
    #
    # print(f'#{tc} {result}')