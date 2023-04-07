a = int(input())
b = int(input())
b_1 = b // 100
b_2 = (b - b_1 * 100) // 10
b_3 = b % 10

print(a*b_3)
print(a*b_2)
print(a*b_1)
print(a*b)

