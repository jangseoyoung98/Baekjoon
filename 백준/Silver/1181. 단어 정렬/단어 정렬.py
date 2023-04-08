N = int(input())
sortList = []

for i in range(N):
    word = input()
    sortList.append(word)

sortList = set(sortList) # 중복된 단어 제거
sortList = list(sortList)

sortList.sort() # 사전 순으로
sortList.sort(key = len) # 길이가 짧은 순으로

for i in sortList:
    print(i)