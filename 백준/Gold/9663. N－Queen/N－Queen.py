import sys

count = 0

def n_queens(cols, i):
    global count
    n = len(cols) - 1
    if(i == n):
        count += 1
    else:
        for j in range(n):
            cols[i] = j
            if (promising(cols, i)):
                n_queens(cols, i+1)

def promising(cols, i): # 유망성 검사 - 모든 경우의 수에 대하여 열 검사 / 대각선 검사
    for k in range(i):
        if(cols[k] == cols[i] or (abs(cols[i] - cols[k]) == i - k)):
            return False
    return True
 
N = int(sys.stdin.readline().strip())
cols = [0] * (N + 1)
n_queens(cols, 0)
print(count)