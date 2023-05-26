length = int(input())

lst = [int(input()) for i in range(length)]

print(sum(num for num in lst if num % 2 == 0))
