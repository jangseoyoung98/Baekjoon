# 가로와 세로를 입력 받는다.
# 자를 횟수를 입력 받는다.
# (횟수 만큼 입력 받을 때)
# 입력 받는 두 수에서 첫 번째가 0이면 -> rows 리스트에 넣는다.
# 1이면 -> cols 리스트에 넣는다.
# 가로와 세로를 인덱스로 등분하고 -> 각각의 가로 길이를 만들고
# 각각의 세로 길이를 만들어서
# 이중 포문으로 넓이를 구한다.

row, col = map(int, input().split())
cnt = int(input())
rows = [0] 
cols = [0]
finRows = []
finCols = []

for _ in range(cnt):
    isRowCol, index = map(int, input().split())
    if isRowCol == 0:
        cols.append(index)
    else:
        rows.append(index)

rows.sort()
cols.sort()
rows.append(row)
cols.append(col)
for i in range(len(rows) - 1):
    finRows.append(rows[i+1] - rows[i])
for i in range(len(cols) - 1):
    finCols.append(cols[i+1] - cols[i])


max = 0
for i in finRows:
    for j in finCols:
        if (i * j) > max:
            max = i * j

print(max)