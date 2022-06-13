import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    result = 0
    for i in range(len(str2) - len(str1)+1):
        for j in range(len(str1)):
            if str1[j] != str2[i+j]:
                j -= 1
                break
        if j == len(str1)-1:
            result = 1
            break
    print(f'#{tc} {result}')

    ## 상은님 풀이
    # M = len(str1)
    # N = len(str2)
    #
    # for i in range(N-M+1):
    #     if str2[i:i+M] == str1:
    #         result = 1
    #
    # print(f'#{tc} {result}')


