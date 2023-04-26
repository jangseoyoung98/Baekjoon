import sys

# 재귀 깊이를 설정한다. (DFS를 재귀로 풀 것이기 때문!)
sys.setrecursionlimit(10**6)

# 노드의 갯수와 간선 정보를 입력 받는다.
N = int(sys.stdin.readline())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(N-1)]

# 그래프를 만든다. (인접 리스트로 만든다.)
graph = [[] for _ in range(N+1)]
for edge in edges:
    s, e = edge
    graph[s].append(e)
    graph[e].append(s)

# (그래프 만들기 함수 버전)
# def make_adj_list(N, edges):
#     adj_list = [[] for _ in range(N+1)]
#     for edge in edges:
#         u, v = edge
#         adj_list[u].append(v)
#         adj_list[v].append(u)
#     return adj_list

# isVisited = [False] * (N+1) -> 이거 대신 parents에서 노드가 0인지 아닌지로 판별!

# DFS 탐색을 이용해서 각 노드의 부모 노드를 찾는다.
def dfs(graph, parents, node, parent):
    parents[node] = parent
    
    for next_node in graph[node]:
        if parents[next_node] == 0:
            dfs(graph, parents, next_node, node)

# 각 노드의 부모 노드를 저장할 리스트를 만들어 준다.
parents = [0] * (N+1)
dfs(graph, parents, 1, 0)

for i in range(2, N+1):
    print(parents[i])


    
    




