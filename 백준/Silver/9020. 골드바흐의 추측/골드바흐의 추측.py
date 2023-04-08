"""
테스트 케이스의 갯수를 입력 받는다.
그 갯수만큼 포문을 돌리면서 수를 입력 받아 -> 리스트에 보관한다.

포문을 돌려서, 리스트에서 하나씩 꺼내서 두 소수를 출력한다.
절반 지점부터 돌리기 시작해서, +1씩 증가하고 (대응되는 아이는 값 - 대응수로 할당)
각각이 소수인지를 판별해서, 맞으면 출력

[소수 판별]
포문으로 소수 판별을 시도한다.

"""
import sys

def isPrime(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


T = int(sys.stdin.readline().strip())
nums = []
for i in range(T):
    nums.append(int(sys.stdin.readline().strip()))

for i in nums:
    tempA = i // 2
    if (i % 2 == 0): # T가 짝수라면 (짝 + 짝)
        tempB = tempA
    else: # T가 홀수라면 (짝 + 홀)
        tempB = tempA + 1

    while(True):
        primeA = isPrime(tempA)
        primeB = isPrime(tempB)

        if primeA == True and primeB == True:
            print(tempA, tempB)
            break
        else:
            tempA -= 1
            tempB += 1
    













