import math

A, B, V = map(int, input().split())

newV = V - A
cnt = 1
if newV <= 0:
    pass
else:
    oneUp = A - B
    cnt += math.ceil(newV / oneUp)

print(cnt)

