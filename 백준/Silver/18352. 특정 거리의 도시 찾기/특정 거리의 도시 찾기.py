import sys
from collections import deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)] # 인덱스 1 ~ N 사용!
distance = [0] * (N+1)
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # 단방향이므로, 한 번만 append 한다!

def bfs(start):
    answer = []
    que = deque([start])
    visited[start] = True
    distance[start] = 0

    while que:
        now = que.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                que.append(i)
                distance[i] = distance[now] + 1
                if distance[i] == K:
                    answer.append(i)
    
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i)

bfs(X)





