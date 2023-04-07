num = int(input())
score = ""
cntO = 0

for i in range(num):
    test = input()
    # split 기준으로 잘라서 -> 문자의 갯수
    test = test.split('X')
    for j in test:
        cnt = j.count('O')
        if cnt > 1:
            cnt = (cnt*(cnt+1))//2
        cntO += cnt
    
    score += ((str(cntO)) + "\n")
    cntO = 0

print(score)
    
