import sys

# 사용자에게 N을 입력 받는다. (N개의 숫자가 들어올 예정)
N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().split()))

candidate = [] # (완전탐색) 모든 경우의 수를 담을 리스트
order = []     # 사용했는지의 여부를 체크하기 위한 리스트

def solve(depth):
    if depth == N:
        candidate.append(
            sum(abs(num[order[i+1]] - num[order[i]]) for i in range(N-1)))
        return
    
    for x in range(N):
        if x not in order:
            order.append(x)
            solve(depth+1)
            order.pop()
        
solve(0)
print(max(candidate))
        
        
        
        
        
        