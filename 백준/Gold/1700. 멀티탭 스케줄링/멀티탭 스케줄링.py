import sys

input = sys.stdin.readline
N, K = map(int, input().split())
equips = list(map(int, input().split()))
plugs = []
c = 0

for i in range(K):
    if equips[i] in plugs:
        continue
    if len(plugs) < N:
        plugs.append(equips[i])
        continue
    
    idxs = []
    for j in range(N):
        # try - except 왠만하면 사용하지 않는 걸로..
        try:
            idx = equips[i:].index(plugs[j])
        except:
            idx = 101
        idxs.append(idx)

    out = idxs.index(max(idxs))
    plugs[out] = equips[i]
    c += 1

print(c)