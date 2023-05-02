import sys

input = sys.stdin.readline

N, K = map(int, input().split())
stuffs = [[0,0]]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for _ in range(N):
   stuffs.append(list(map(int, input().split())))

# dp[i][j] : i번째까지 도구를 넣었을 때, j라는 최대 용량
for i in range(1, N+1):
   for j in range(1, K+1):
      w = stuffs[i][0]
      v = stuffs[i][1]

      if w > j:
         dp[i][j] = dp[i-1][j]
      else:
         dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[N][K])