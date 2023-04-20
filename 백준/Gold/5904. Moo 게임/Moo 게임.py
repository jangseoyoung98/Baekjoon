import sys
sys.setrecursionlimit(10**6 )
input = sys.stdin.readline

def moo(acc, ctr, N):   # ctr은 중간 지점의 길이이다.
    prev = (acc-ctr) // 2
    if N <= prev: return moo(prev, ctr-1, N)
    elif N > prev + ctr: return moo(prev, ctr-1, N-prev-ctr)
    else: return "o" if N-prev-1 else "m"

N = int(input())

acc, n = 3, 0   # acc는 m과 o로 이루어진 전체 문자열의 길이이고, n은 점화식에서 k의 역할과 같다고 상정한다.
while N > acc:
    n += 1      # 점화식에서 k이다!
    acc = acc*2 + n+3

result = moo(acc, n + 3, N)
print(result)