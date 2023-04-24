import sys
sys.setrecursionlimit(10**6)

inputs = []

while True:
    try:
        inputs.append(int(sys.stdin.readline()))
    except:
        break

def postorder(start, end):
    global inputs

    if start > end: # 자식 노드가 더 이상 없다!
        return
    
    mid = end + 1 # 오른쪽 노드가 없을 수도 있으니까 -> postorder(mid, end)를 호출시키지 않기 위함 (왼쪽이 없다고 봐도, (start+1, mid-1)이 위 종료조건에서 그냥 끝남)
    
    for i in range(start+1, end+1):
        if inputs[start] < inputs[i]:
            mid = i
            break
    
    postorder(start+1, mid-1) # 왼쪽 순회
    postorder(mid, end)       # 오른쪽 순회
    print(inputs[start])

postorder(0, len(inputs) - 1)
    
    









