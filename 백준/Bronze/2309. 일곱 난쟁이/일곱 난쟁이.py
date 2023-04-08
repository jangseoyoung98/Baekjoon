## 완전 탐색..?
# 아홉명의 키를 일단 리스트에 다 저장하고
# 이중 for 문을 사용해, 하나씩 고정시켜가면서 다 더해서, 합이 100이 되는지를 구한다.
# 그걸 리스트에 저장해, 오름차순으로 보여준다.

import sys
mans = []

for _ in range(9):
    man = int(sys.stdin.readline().strip())
    mans.append(man)

result = sum(mans)

for i in range(0, 8):
    result -= mans[i]
    for j in range(i+1, 9):
        result -= mans[j]
        if result == 100:
            mans.remove(mans[j])
            mans.remove(mans[i])
            mans.sort()
            print(*mans, sep="\n")
            exit()
        else:
            result += mans[j]
    result += mans[i]



