import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    str1_len = len(str1)
    str2_len = len(str2)
    result = 0
    count_dic = {}

    str1_set = set(str1)
    print(str1_set)
    for char in str1_set:
        count_dic[char] = 0

    for key in count_dic.keys():
        for char in str2:
            if key == char:
                count_dic[char] += 1

    for value in count_dic.values():
        if result < value:
            result = value

    print(f'#{tc} {result}')



