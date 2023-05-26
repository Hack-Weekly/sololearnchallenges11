TAX = 1.07

TAXED, TAXLESS = [], []

for price in input().split(','):
    if float(price) < 20:
        TAXED.append(float(price))
    else:
        TAXLESS.append(float(price))

print(round(sum(TAXED) * TAX + sum(TAXLESS), 2))
