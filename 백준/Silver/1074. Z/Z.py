import sys

N, r, c = map(int, sys.stdin.readline().split())

def recur(N, r, c):
    if N == 0:
        return 0
    N -= 1
    return 2 * (r % 2) + (c % 2) + 4 * recur(N, r // 2, c // 2)


print(recur(N, r, c))