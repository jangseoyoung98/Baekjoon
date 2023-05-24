import sys
input = sys.stdin.readline

N, K = map(int, input().split())
vals = []
for _ in range(N):
    val = int(input())
    vals.append(val)

rem = K  # remainder
cnt = 0
i = N - 1  # val의 큰 값부터 시작한다.

while i>=0 :
    cnt += rem // vals[i]
    rem = rem % vals[i]
    i -= 1

print(cnt)