from math import ceil

TAPE_AREA = 10

height, width = int(input()), int(input())

print(ceil(height * width * 2) / TAPE_AREA)
