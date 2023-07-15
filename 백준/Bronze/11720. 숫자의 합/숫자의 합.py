import sys

input = sys.stdin.readline
cnt = int(input())
N = input()

nums = [0 for _ in range(cnt)]
for i in range(cnt):
    nums[i] = int(N[i])

print(sum(nums))
