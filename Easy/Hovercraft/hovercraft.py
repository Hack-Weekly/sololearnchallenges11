BUILD_COST = 21000000
SELL_COST = 3000000

customers = int(input())

profit = SELL_COST * customers - BUILD_COST

if profit == 0:
    print('Broke Even')
elif profit > 0:
    print('Profit')
else:
    print('Loss')
