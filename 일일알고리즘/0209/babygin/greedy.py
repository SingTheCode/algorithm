import sys

sys.stdin = open("input.txt")

num = int(input())

c = [0] * 10

for i in range(6):
    c[num % 10] += 1
    num //= 10

triplet = run = 0

for i in range(10):
    if c[i] >= 3:
        c[i] -= 3
        triplet += 1
        continue
    if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1
if run + triplet == 2:
    print("#0 1")
else:
    print("#0 0")
