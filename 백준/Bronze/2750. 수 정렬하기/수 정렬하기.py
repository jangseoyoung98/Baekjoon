# sort 함수.. 사용해도 될까?
# 사용자에게 입력을 받아
# sort를 적용한 리스트를 출력한다.

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()
for i in nums:
    print(i, sep="\n")
