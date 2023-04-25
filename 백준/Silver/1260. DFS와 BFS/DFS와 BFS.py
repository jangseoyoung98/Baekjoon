import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]  

# 그래프 정보 입력 받기
for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s) # undirected graph인 경우

# 그래프 각 노드에 연결된 인접 노드 정렬
for i in range(1, N+1):
    graph[i].sort()

# DFS 구현
def DFS(start, isVisited):
    isVisited[start] = True
    print(start, end=" ") # 따로 문자열로 만들어서 보관하지 않고, 그냥 바로 print 하게끔..
    
    for v in graph[start]:
        if not isVisited[v]: # == 0 이거 대신 깔끔하게 `not`
            DFS(v, isVisited)

# BFS 구현
def BFS(start):
    isVisited = [False] * (N+1) # BFS에서 또 isVisited를 사용하기 위해서는, 동일한 이름이더라도 초기화 해주어야 함!
    que = deque([start]) # 선언하고 append 따로 할 필요 없이 한 번에!
    isVisited[start] = True
    
    while que:
        v = que.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not isVisited[i]:
                que.append(i)
                isVisited[i] = True


isVisited = [False] * (N+1)
DFS(V, isVisited)
print()
BFS(V)