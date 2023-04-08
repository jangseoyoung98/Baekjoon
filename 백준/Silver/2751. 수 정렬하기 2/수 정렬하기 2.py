import sys

N = int(sys.stdin.readline().strip())
nums = []

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    nums.append(num)

nums.sort()
print(*nums, sep="\n")


