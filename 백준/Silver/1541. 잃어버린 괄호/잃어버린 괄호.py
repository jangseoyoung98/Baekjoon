import sys

str = sys.stdin.readline().strip()
temp = str.split('-')

# 인덱스 0번째는 무조건 +(양수)이다.
# 인덱스 1번부터 각각의 요소를 더하고 - 씌우면 되는데, 
# 만약 +가 중간에 끼여 있으면, 두 개를 다시 파싱 한 후 그 두 개를 더하고 -를 씌운다. -> 리스트 요소가 여러개
nums = temp
n = len(temp)
for i in range(0, n):
    result = temp[i].split('+')
    nums[i] = list(map(int, result))

min = sum(nums[0])
for j in nums[1:]:
    res = sum(j)
    min -= res

print(min)