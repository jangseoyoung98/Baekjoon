"""
곱하고 -> str으로 바꾸고 -> for문 돌면서 각각마다 숫자가 몇 번 사용되었는지 출력한다. (count 함수 사용)
"""

A = int(input())
B = int(input())
C = int(input())

mul = str(A * B * C)
result = ""

for i in range(10):
    i = str(i)
    cnt = str(mul.count(i))
    result += cnt + "\n"

print(result)
