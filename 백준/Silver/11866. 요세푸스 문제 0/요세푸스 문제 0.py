# 알고리즘 : 원형 큐로, popleft 되는 순서를 구한다.
# input : N, K (입력) | (필요) queue []
# output : popleft 되는 순서 -> answer []
from collections import deque
import sys

N, K = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, N+1)])
ans = "<"

i = 1
while len(queue) != 1:
    index = ((K * i) % N) - 1
    i += 1
    queue.rotate(-(K-1))
    x = queue.popleft()
    ans += (str(x) + ", ")

# dequeue 모듈을 받아와, queue 리스트에 담는다.
# N과 K를 입력 받아 -> 1부터 N까지의 수를 리스트에 저장한다. (이때 리스트의 크기는 N으로 한다.)
# (K * 1/2/3.. % 7 한 인덱스를 popleft 해서 리스트에 보관한다.)

# 나중에 다 출력한다.
remain = queue.popleft()
ans += (str(remain) + ">") 
print(ans)


