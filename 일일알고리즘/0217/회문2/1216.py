import sys
sys.stdin = open('input.txt')

MAX_SIZE = 100

def is_palindrome(str):
    if str == str[::-1]:
        return len(str)
    return False

T = 10
for _ in range(1, T+1):
    tc = int(input())
    arr = [list(input()) for _ in range(MAX_SIZE)]
    max_palindrome = 0

    for i in range(MAX_SIZE):
        for palindrome_len in range(MAX_SIZE, max_palindrome, -1):
            if palindrome_len < max_palindrome:
                break
            for startIndex in range(0, MAX_SIZE - palindrome_len + 1):
                tmp = ''
                for j in range(palindrome_len):
                    tmp += arr[i][startIndex + j]
                newPalindrome = is_palindrome(tmp)
                if newPalindrome:
                    max_palindrome = newPalindrome
                    break

        for palindrome_len in range(MAX_SIZE, max_palindrome, -1):
            if palindrome_len < max_palindrome:
                break
            for startIndex in range(0, MAX_SIZE - palindrome_len + 1):
                tmp =''
                for j in range(palindrome_len):
                    tmp += arr[startIndex + j][i]
                newPalindrome = is_palindrome(tmp)
                if newPalindrome:
                    max_palindrome = newPalindrome


    print(f'#{tc} {max_palindrome}')


# 교수님 풀이
# def is_palindrome(word):
#     idx = 0
#     while idx + M-1 < len(word):
#         pali = word[idx:idx + M]
#         if pali == pali[::-1]:          # 뒤집었을때 일치하면 회문
#             return pali                 # 회문 반환
#         idx += 1
#     return False
#
#
# T = int(input())
#
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [input() for _ in range(N)]
#
#     for i in range(N):
#         tmp = ''
#         for j in range(N):
#             tmp += arr[j][i]            # tmp 는 열방향
#         result = is_palindrome(tmp)     # 열방향 회문 체크
#         if result:
#             break
#         result = is_palindrome(arr[i])  # 행방향 회문 체크
#         if result:
#             break
#
#     print(f'#{tc} {result}')