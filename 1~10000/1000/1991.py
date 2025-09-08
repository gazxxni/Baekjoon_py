import sys
input = sys.stdin.readline

n = int(input())
heap = {}

for _ in range(n):
    a, b, c = input().split()
    heap[a] = [b, c]  # {노드: (왼쪽 자식, 오른쪽 자식)}

def preorder(node):  # 현재 노드를 방문 → 왼쪽 서브트리 → 오른쪽 서브트리
    if node == '.':
        return
    print(node, end='')
    preorder(heap[node][0])
    preorder(heap[node][1])

def inorder(node):  # 왼쪽 서브트리 → 현재 노드 방문 → 오른쪽 서브트리
    if node == '.':
        return
    inorder(heap[node][0])
    print(node, end='')
    inorder(heap[node][1])

def postorder(node):  # 왼쪽 서브트리 → 오른쪽 서브트리 → 현재 노드 방문
    if node == '.':
        return
    postorder(heap[node][0])
    postorder(heap[node][1])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()




"""
노드 개수 N
방문 시간 O(1)
전체 연산 O(N)
"""