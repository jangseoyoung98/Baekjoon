# 피보나치 수열 (하향식 Top-down)
"""
n부터 시작한다 + 재귀 사용 + memoization
필요한 것 : 전역으로 memo를 만들어 놓는다.
1. 종료 조건 1) num == 0, 1이면 0, 1 리턴한다.
2. 종료 조건 2) memo[num]이 있으면 -> 해당 값을 바로 리턴한다.
3. 재귀로 돌리면서 memo에 append 한다.
"""
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
# memo = [0, 1]

# def fibo(num):
#     if len(memo) >= (num + 1): # 이미 값이 저장되어 있다는 의미
#         return memo[num]
    
#     result = fibo(num-1) + fibo(num-2)
#     memo.append(result)
    
# print(fibo(N))

# 피보나치 수열 (상향식 Bottom-up)
"""
초기값부터 시작한다 + for문 사용 + tabulization
필요한 것 : 전역으로 table을 만들어 놓는다.
1) table[] 각각의 인덱스에 초기값을 할당한다.
2) for문으로 2부터 N+1까지 값을 더해간다.
3) 그리고 N번째 값을 출력한다.
"""
table = [0] * (N+1)
table[0] = 0
table[1] = 1

for i in range(2, N+1):
    table[i] = table[i-1] + table[i-2]

print(table[N])
