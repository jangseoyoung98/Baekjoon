T = int(input())
sums = []

for i in range(T):
    A, B = map(int, input().split())
    sums.append(A + B)

for i in sums:
    print(i)