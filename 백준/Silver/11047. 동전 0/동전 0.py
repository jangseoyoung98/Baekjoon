import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
cnt = 0

for i in coins:
    cnt += K // i
    K %= i
    if K == 0:
        break

print(cnt)