import sys

input = sys.stdin.readline
N = int(input())
times = []

for i in range(N):
    start, end = map(int, input().split())
    times.append([start, end])

times = sorted(times, key = lambda x : x[0])
times.sort(key = lambda x : x[1])
# times = sorted(key = lambda x : x[1])

cnt = 1 # 0번째 거 넣고 시작하니까
end = times[0][1]
for i in range(1, N):
    if times[i][0] >= end:
        cnt += 1
        end = times[i][1]

print(cnt)
    