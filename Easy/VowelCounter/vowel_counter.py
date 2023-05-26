sentence = input().casefold()

print(sum(1 for char in sentence if char in 'aeiou'))
