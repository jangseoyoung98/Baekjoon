num = int(input())
case = []
result = []

for i in range(num):
    case = list(map(int, input().split()))
    cnt = case[0]
    sum = 0
    avg = 0
    smartStudent = 0
    for j in range(1, cnt+1):
        sum += case[j]
    avg = sum / cnt
    # print(avg)
    
    for j in range(1, cnt+1):
        if case[j] > avg:
            smartStudent += 1
    
    rate = smartStudent / cnt * 100
    result.append(rate)

for i in result:
    print(f"{i:.3f}%")


"""
입력 받은 수만큼 돌리는데
-> 한 줄 입력 받을 때마다 처리해서 -> 다른 배열에 값들을 넣고 & 문자열로 값을 넣고
-> 한 번에 출력한다.

처리는
0번째 인덱스는 따로 cnt 변수에 담고
1부터 n-1까지의 인덱스를 돌면서, 평균을 구한다.
다시 1부터 n-1까지의 인덱스를 돌면서, 평균을 넘는 학생을 뽑아내 비율을 구한다.

그리고 출력한다.

"""