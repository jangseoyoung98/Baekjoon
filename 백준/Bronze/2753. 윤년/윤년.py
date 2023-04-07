#  (4의 배수) and 100의 배수 X or 400의 배수
# 100 X 400 O
# 100 O 400 O

# 100 O 400 X


year = int(input())

if year % 4 != 0:
    print(0)
elif (year % 100 == 0) and (year % 400 != 0):
    print(0)
else:
    print(1) 