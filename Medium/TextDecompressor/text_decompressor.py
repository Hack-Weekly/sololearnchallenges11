compressed_str = input()

chars = [char for char in compressed_str if char.isalpha()]
nums = ''.join([' ' if char.isalpha() else char for char in compressed_str]).split()
print(''.join([chars[index] * int(nums[index]) for index in range(len(chars))]))
