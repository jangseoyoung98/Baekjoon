import sys

# 함수 (이분탐색)
# 전역변수 N 리스트를 가지고, 반으로 쪼개면서 key가 있는지를 찾는다.
def search(pl, pr, key):
    global N_list
    
    if pl > pr:
        return -1
    
    pc = (pl + pr) // 2

    if N_list[pc] == key:
        return pc
    elif N_list[pc] > key:
        pr = pc - 1
        return search(pl, pr, key)
    else: # N_list[pc] < key
        pl = pc + 1
        return search(pl, pr, key)




# N을 입력 받아 -> N개의 정수를 입력 받아 배열에 저장한다. + sort 함수를 사용해서, 정렬한다. => 전역 변수
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

# M을 입력 받아 M만큼 돌리면서 -> M개의 정수를 입력 받을 때마다 검사하고 0 또는 1로 저장한다.
# 최종 결과를 출력한다.
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
for i in range(M):
    isThere = search(0, N - 1, M_list[i])
    if isThere == -1:
        M_list[i] = 0
    else:
        M_list[i] = 1

print(*M_list, sep="\n")
    
