N = int(input())
strN = str(N)
result = 0

if N < 100:
    result = N
else:
    result += 99
    
    for i in range(100, N+1):
        tempStr = str(i)
        first = int(tempStr[0])
        second = int(tempStr[1])
        third = int(tempStr[2])

        if (first - second) == (second - third):
            result += 1
print(result)
