
names, target = input().split(' '), input()

for name in names:
    if name[0] == target[0]:
        print('Compare notes')
        break
else:
    print('No such luck')
