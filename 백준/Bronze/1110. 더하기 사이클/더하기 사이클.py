# 1. 더하기 사이클 - 수학, 구현
import sys

# 문자열이 주어졌을 때, 10보다 작다면 앞에 0을 붙여 문자열로 만든다.
# 그게 아니라면 바로 다음 단계로 간다.
N = sys.stdin.readline().strip()
if int(N) < 10:
    N = "0" + N
first = int(N) // 10
second = int(N) % 10
result = str(first + second)
count = 0   # 사이클 횟수

# 첫 번째 문자와 두 번째 문자를 더한 값을 -> str으로 만들고, 두 번째 자리를 가져온다.
# 이를 만들면서 계속 반복하면서, 첫째 자리가 원래와, 둘째 자리가 원래와 같을 때까지 반복
# count ++ 하고 출력
while True:
    if int(result) < 10:
        result = "0" + result

    first = second
    second = int(result[1])
    count += 1

    if first == int(N[0]) and second == int(N[1]):
        print(count)
        break
    
    result = str(first + second)