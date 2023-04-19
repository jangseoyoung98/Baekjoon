# PriorityQueue 모듈을 사용한다.
from queue import PriorityQueue
import sys

input = sys.stdin.readline
N = int(input())
que = PriorityQueue(maxsize=N)

# ★ PQ 모듈에서 비어있는지 확인하는 방법은 .empty()로, 비어있다면 True를 리턴한다.
# ★ 크기 지정은 maximize가 아니라 maxsize이다!
# ★ PQ는 데이터를 추가(put)한 순서에 상관 없이 데이터를 꺼낼 때(get) 값을 '오름차순' 하여 반환하는 특징을 갖고 있다.
for _ in range(N):
    num = int(input())

    if num == 0:
        if que.empty():
            print(0)
            # continue
        else:
            # print(que.get()) # 가장 큰 값을 출력해야 한다.
            print(que.get()[1])

    else:
        # que.put(num)
        que.put((-num, num))

# 내림차순으로 삽입 및 정렬
# ★ 만약 결과를 역순으로 반환하고 싶다면, 튜플 형태로 값을 put 하여 반환 받으면 된다.라고 한다...







