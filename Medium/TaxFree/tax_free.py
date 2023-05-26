TAX = 0.07

prices = [float(price) for price in input().split(',')]

TAXED = [price for price in prices if price < 20]

print(round(sum(TAXED) * TAX + sum(prices) , 2))

# TAX = 1.07

# TAXED, TAXLESS = [], []

# for price in input().split(','):
#     if float(price) < 20:
#         TAXED.append(float(price))
#     else:
#         TAXLESS.append(float(price))

# print(round(sum(TAXED) * TAX + sum(TAXLESS), 2))
