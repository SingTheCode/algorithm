# def eightToTen(num):
#     rest = num
#     result = 0
#     numArr = []
#
#     for i in range(N):
#         numArr.append(rest // (10 ** (N - i - 1)))
#         rest %= 10 ** (N - i - 1)
#
#     for j in range(N):
#         result += numArr[j] * (8 ** (N - j - 1))
#
#     return result


# tmp = int(input())
# N = len(str(tmp))

# print(format(eightToTen(tmp), 'b'))


# 내장함수
num = input()
ten = int(num, 8)
result = format(ten, 'b')
print(result)
