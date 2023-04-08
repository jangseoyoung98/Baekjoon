def factorial (num):
    if num < 2:
        return 1
    else:
        return num * factorial(num-1)

num = int(input())

print(factorial(num))

