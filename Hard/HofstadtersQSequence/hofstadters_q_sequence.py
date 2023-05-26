from sys import setrecursionlimit
setrecursionlimit(100000)

results = [0] * 100000

def q_seq(num):
    if num == 1 or num ==2:
        return 1
    if results[num] != 0:
        return results[num]

    results[num] =  q_seq(num - q_seq(num - 1)) + q_seq(num - q_seq(num -2))

    return results[num]

print(q_seq(int(input())))
