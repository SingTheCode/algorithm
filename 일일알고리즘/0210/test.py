square_dict = {}

for i in range(4):
    square_lst = list(map(int, input().split()))
    for j in range(square_lst[1], square_lst[3]):
        lst = [0] * (square_lst[2]) # 초기화 각 y값에 들어갈 list
        for k in range(square_lst[0], square_lst[2]):
            lst[k] = 1
        if j in square_dict.keys():
            if len(lst) > len(square_dict[j]):
                square_dict[j] += lst[len(square_dict[j]):]
            else:
                for num in range(len(square_dict[j])+1):
                    if square_dict[j][num] == 0:
                        square_dict[j][num] += lst[num]
        else:
            square_dict[j] = lst


tot = 0
for k in square_dict.values():
    tot += sum(k)

print(tot)