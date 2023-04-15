# 숫자 N을 입력 받는다. -> 1부터 N까지의 숫자로 리스트를 만든다. (Stack)
# 무한루프..?로 돌려서 앞에 거 빼고, 다음 앞에 거 append 한 후 앞에 거 빼고 -> 함수 호출
# 종료 조건 : 앞에 거 pop 했을 때 남는 카드의 갯수가 1개가 된다면 종료한다.
from collections import deque
import sys

N = int(sys.stdin.readline())
queue = deque()

for i in range(1, N+1):
    queue.append(i)
    
while True:
    if len(queue) == 1:
        break
    queue.popleft()
    first = queue.popleft()
    queue.append(first)

last = queue.pop()
print(last)