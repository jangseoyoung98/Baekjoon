import sys
from collections import deque
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
isVisited = [False] * (N+1)
cnt = 0

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

# DFS 호출 횟수로 그래프의 갯수를 구한다!!

def dfs(v):
    isVisited[v] = True

    for next in graph[v]:
        if not isVisited[next]:
            dfs(next)    

for i in range(1, N+1):
    if not isVisited[i]:
        dfs(i)
        cnt += 1

print(cnt)

# index = 0
# for v in graph:
#     # v -> 노드
#     if not isVisited[index]:
#         isVisited[index] = True
#         for e in graph[index]:
#             if not isVisited[e]:
#                 isVisited[e] = True    
#     if isVisited.count(False):
#         cnt += 1
#     index += 1













