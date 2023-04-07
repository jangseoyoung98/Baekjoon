x, y, w, h = map(int, input().split())

rd1 = y
rd2 = x
rd3 = h-y
rd4 = w-x
rds = [rd1, rd2, rd3, rd4]

fast = rd1

for i in range(1, 4):
    if fast > rds[i]:
        fast = rds[i]

print(fast)