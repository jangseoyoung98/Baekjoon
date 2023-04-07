score = int(input())
grade = score // 10

if grade == 9 or grade == 10:
    print('A')
elif grade == 8:
    print('B')
elif grade == 7:
    print('C')
elif grade == 6:
    print('D')
else:
    print('F')