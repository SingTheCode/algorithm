import sys
sys.stdin = open("sample_input.txt")

T = int(input())
for tc in range(1, T+1):
    P, p_a, p_b = map(int, input().split())
    cnt_a = cnt_b = 0
    a_l = b_l = 0
    a_r = b_r = P
    result = ""

    for i in range(P):
        if (a_l + a_r) // 2 != p_a:
            if (a_l + a_r) // 2 > p_a:
                a_r = (a_r + a_l) // 2
                cnt_a += 1
            if (a_l + a_r) // 2 < p_a:
                a_l = (a_r + a_l) // 2
                cnt_a += 1
        if (b_l + b_r) // 2 != p_b:
            if (b_l + b_r) // 2 > p_b:
                b_r = (b_r + b_l) // 2
                cnt_b += 1
            if (b_l + b_r) // 2 < p_b:
                b_l = (b_r + b_l) // 2
                cnt_b += 1
        if (a_l + a_r) // 2 == p_a and (b_l + b_r) // 2 == p_b:
            break


    if cnt_a == cnt_b:
        result = "0"
    else:
        result = "A" if cnt_a < cnt_b else "B"
    print(f'#{tc} {result}')