# 이진표현
import sys

sys.stdin = open('input.txt')

checkList = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111',
             '0001011']

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    result = 0
    count = 0
    isBreak = 0
    arr = [input() for _ in range(N)]
    for oneLine in arr:
        if isBreak:
            break
        for i in range(M - 1, -1, -1):
            cnt = 0
            tmp = 0
            if oneLine[i] == '1':
                for j in range(i - 55, i + 1, 7):
                    code = oneLine[j:j + 7]

                    for k in range(10):
                        if checkList[k] == code:
                            if cnt % 2:
                                tmp += k
                                cnt += 1
                                result += k
                            else:
                                tmp += k * 3
                                cnt += 1
                                result += k
                if tmp % 10:
                    result = 0
                isBreak = 1
            if isBreak:
                break

    print(f'#{tc} {result}')

# 교수님 풀이
# import sys
# sys.stdin = open('input.txt')
#
# # number = {
# #     '0111011': 7,
# #     '0110001': 5,
# # }
# number = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
#
# T = int(input())
#
#
# def password():
#     for row in code:                        # 입력된 암호코드를 한 줄씩 순회
#         for i in range(M-1,-1,-1):          # 뒤에서 앞으로 하나씩 접근
#             if row[i] == '1':               # '1' 을 만나면
#                 pw = row[i-55:i+1]          # 56자리를 자른다
#                 temp = valid = 0
#                 for j in range(8):          # 8자리의 암호코드를 하나씩 확인(홀수/짝수 확인)
#                     for k in range(10):     # number 안의 숫자와 일치하는 인덱스 찾기
#                         if number[k] == pw[j*7:(j+1)*7]:
#                             if j%2:         # 짝수번째 숫자는 단순 합산
#                                 temp += k
#                             else:           # 홀수번째 숫자는 3배후 합산
#                                 temp += k*3
#                             valid += k      # 홀수짝수 관계없이 합산
#                 if temp%10:                 # 10의 배수가 아니면(정상 암호가 아니면)
#                     return 0                # 0 반환
#                 else:                       # 정상 암호이면
#                     return valid            # valid 반환
#
#
# for tc in range(1, T+1):
#     N,M = map(int, input().split())
#     code = [input() for _ in range(N)]
#     print(f'#{tc} {password()}')