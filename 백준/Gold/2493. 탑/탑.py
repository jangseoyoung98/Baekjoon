# 알고리즘 : 탑 - 탑의 레이저를 송신한 탑 인덱스 찾기
# input : N, towers[], // stack[], result[]
# output : result[레이저 맞은 탑의 인덱스 리스트]

# towers를 enumerate()로 (자동생성)인덱스+밸류값 각각을 반환한다. -> i, val
# 스택이 비어 있지 않고,
# 스택 위에 있던 원소가 새로 넣고자 하는 원소보다 "크다면" -> append를 한다. (result에 넣는다. 스택 위에 있는 원소의 인덱스를)

# 스택 위에 있던 원소가 새로 넣고자 하는 원소보다 "작다면" -> pop을 한다.

# 스택이 비어 있다면 -> 알아서 result에 0이 남는다.

import sys
N = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))

stack = []
result = [0] * N

for i, tower in enumerate(towers): # i : 인덱스 / val : 값

    while stack and stack[-1][1] < tower:
        stack.pop()

    if stack:
        result[i] = stack[-1][0]

    stack.append((i+1, tower)) # 타워의 인덱스는 1부터 시작하니까!

print(*result, sep=" ")




