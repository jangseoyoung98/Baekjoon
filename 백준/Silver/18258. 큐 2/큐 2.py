import sys
input = sys.stdin.readline
# 리스트는 global 할 필요 없다?
# size 변수 따로 두어서 리스트 원소의 갯수를 계산한다.


def push(x): # 정수 x를 큐에 넣는다.
    global fr, rear, queue, size
    # rear의 다음 인덱스가 N인지 확인해서, 맞다면 -> full을 출력한다.    
    # 아니라면, rear의 다음 인덱스로 이동해서, 해당 인덱스에 데이터를 삽입한다.
    if rear == N:
        print("큐가 가득 찼습니다!")
        return
    queue[rear] = x
    rear += 1
    size += 1


def pop():
    global fr, rear, queue, size
    # front가 rear보다 크다면, (empty이므로) -1을 출력한다.
    # 아니라면, front 인덱스의 원소를 data에 보관하고, front를 1 증가시킨다. 그리고 data를 출력한다.
    if size == 0:
        print(-1)
        return
    data = queue[fr]
    fr += 1
    print(data)
    if size > 0:
        size -= 1

def sizeQueue():
    global fr, rear, queue, size
    # rear - front + 1의 수를 리턴한다.
    print(size)

def empty():
    global fr, rear, queue, size
    # front가 rear보다 크다면 empty이다. -> 1 출력
    # 아니면 0 출력
    if size == 0:
        print(1)
    else:
        print(0)


def front():
    global fr, rear, queue, size
    # front 인덱스의 원소를 출력한다.
    if size == 0:
        print(-1)
        return
    print(queue[fr])


def back():
    global fr, rear, queue, size
    # rear 인덱스의 원소를 출력한다.
    if size == 0:
        print(-1)
        return
    print(queue[rear-1])



N = int(input())
queue = [0] * N
fr, rear = 0, 0 # front : 디큐할 원소의 인덱스 / rear : 큐에서 top에 있는 원소의 인덱스
size = 0

for _ in range(N):
    instruction = list(input().split())
    if instruction[0] == 'push':
        push(int(instruction[1]))
    elif instruction[0] == 'pop':
        pop()
    elif instruction[0] == 'size':
        sizeQueue()
    elif instruction[0] == 'empty':
        empty()
    elif instruction[0] == 'front':
        front()
    elif instruction[0] == 'back':
        back()