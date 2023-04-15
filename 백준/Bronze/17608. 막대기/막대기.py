# 정수 N을 입력 받아 N번만큼 돌리면서, 사용자에게 입력받아 리스트에 저장하는데!
# 새로 들어온 값이 기존 값보다 크다면, 이전 값들을 pop 한다.
# 작다면, push 한다.

import sys

N = int(sys.stdin.readline())
stack = [-1]

for i in range(N):
    num = int(sys.stdin.readline())
    
    if i == 0 or num < stack[-1]: # 처음은 우선 넣는다.
        stack.append(num)
        continue
    
    # if num > stack[pos]:
    while True:
        if stack[-1] == -1:
            break
        if num < stack[-1]:
            break
        stack.pop()
        
    stack.append(num)

print(len(stack) - 1)