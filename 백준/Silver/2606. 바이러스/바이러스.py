import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
isVisited = [False] * (N+1)

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

def BFS(v):
    cnt = -1    # 시작할 때 바로 1을 더하니까 -1로 시작한다.
    que = deque([v])
    isVisited[v] = True

    while que:
        x = que.popleft()
        cnt += 1
        for node in graph[x]:
            if not isVisited[node]:
                que.append(node)
                isVisited[node] = True

    return cnt


print(BFS(1))


    










