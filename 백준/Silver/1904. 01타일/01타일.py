import sys
input = sys.stdin.readline

N = int(input())
cnt = [0] * (N+1)
cnt[1] = 1
if N >= 2:
    cnt[2] = 2

for i in range(3, N+1):
    cnt[i] = (cnt[i-1] + cnt[i-2]) % 15746

print(cnt[N])




