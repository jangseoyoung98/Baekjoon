N, X = map(int, input().split())
A = list(map(int, input().split()))
result = ""

for i in A:
    if X > i:
        result += (str(i) + " ")

print(result)