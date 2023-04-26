import sys
from collections import deque

# 미로의 크기 N과 M을 입력 받는다.
N, M = map(int, sys.stdin.readline().split())
# 미로를 2차원 리스트로 입력 받는다.
miro = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# BFS 함수를 정의한다. (너비 우선 탐색)
"""
bfs 로직
- 큐를 생성한다. 그리고 큐에 맨 첫 원소를 append 한다.
- 큐가 빌 때까지 while을 반복하는데
  - 큐를 popleft 한다. -> x
  - x의 인덱스를 방문 처리한다.
  - (그래프에서 x의 엣지들을 확인해서) x의 엣지들을 전체 다 큐에 append 한다.
"""
def bfs(x, y):
    # 이동할 네 방향을 정의한다. (상 하 좌 우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # deque을 생성한다.
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()

        # 현재 위치에서 4가지 방향으로 위치를 확인한다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치가 벗어나면 안 되므로, 조건을 추가한다. -> 1)미로의 끝에 닿는다.
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # # 2) 갈 수 없는 경우(0 -> 벽이다.)
            # if miro[nx][ny] == 0:
            #     continue

            # 위 두 조건이 아닌 경우에는 (1이므로) 이동한다.
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                que.append((nx, ny))
    
    # 마지막 값에서 카운트 값을 뽑는다.
    return miro[N-1][M-1]

print(bfs(0,0)) # 리스트의 인덱스는 0부터 시작하게 했으므로 (1,1)은 (0,0)부터 시작한다고 생각!

