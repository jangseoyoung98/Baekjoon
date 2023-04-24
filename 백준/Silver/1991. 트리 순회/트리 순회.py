import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
strs = []

for _ in range(N):
    parent, lchild, rchild = map(str, sys.stdin.readline().split()) # map 객체로 들어감 ㅌ -> str 타입임
    strs.append((parent, lchild, rchild))  # 입력 받은 부모/왼쪽자식/오른쪽자식을 튜플의 형태로 리스트에 append 한다.

tree = {}

class Node:
    def __init__(self, parent, lchild, rchild):
        self.item = parent
        self.lchild = lchild
        self.rchild = rchild
        
def preorder(node):
    print(node.item, end='')
    if node.lchild != '.':
        preorder(tree[node.lchild])
    if node.rchild != '.':
        preorder(tree[node.rchild])

def inorder(node):
    if node.lchild != '.':
        inorder(tree[node.lchild])
    print(node.item, end='')
    if node.rchild != '.':
        inorder(tree[node.rchild])

def postorder(node):
    if node.lchild != '.':
        postorder(tree[node.lchild])
    if node.rchild != '.':
        postorder(tree[node.rchild])
    print(node.item, end='')

for parent, lchild, rchild in strs:
    tree[parent] = Node(parent, lchild, rchild)

preorder(tree['A']) # 키에 대한 밸류로 Node 클래스 객체가 전달 됨!
print()
inorder(tree['A'])
print()
postorder(tree['A'])