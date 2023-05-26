ceil = int(input())

SUM = 0

for num in range(0, ceil):
    if num % 3 == 0 or num % 5 == 0:
        SUM += num

print(SUM)
