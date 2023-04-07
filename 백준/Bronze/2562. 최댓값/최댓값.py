nums = []
max = 0
maxIndex = -1

for i in range(9):
    num = int(input())
    nums.append(num)
    if num > max:
        max = num
        maxIndex = i + 1

print(max)
print(maxIndex)
