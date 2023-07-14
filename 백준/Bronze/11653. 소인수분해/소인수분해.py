N = int(input())
result = [] # 문자열로 하면 메모리 절약


if(N != 1):
    i = 2
    end = N
    while(end > 1):
        if(end % i != 0):
            i += 1
            continue
    
        result.append(i)
        end = end // i
    
    for i in result:
        print(i)