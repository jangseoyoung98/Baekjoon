""""
입력 받은 두 숫자를 거꾸로 읽어서 -> 더 큰 값 찾기
"""

A, B = input().split() # A와 B는 각각 문자열

len_A = len(A)
len_B = len(B)

newA = ""
newB = ""

for i in range(len_A-1, -1, -1):
    newA += A[i]
for i in range(len_B-1, -1, -1):
    newB += B[i]

newA = int(newA)
newB = int(newB)

if newA > newB:
    print(newA)
else:
    print(newB)
