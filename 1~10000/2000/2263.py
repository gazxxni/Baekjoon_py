import sys
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

ans = []
stack = [(0, n - 1, 0, n - 1)]
while stack:
    inL, inR, postL, postR = stack.pop()
    if inL > inR:
        continue
    root = postorder[postR]
    ans.append(root)
    mid = inorder.index(root, inL, inR + 1)
    left_size = mid - inL
    right_size = inR - mid
    if right_size > 0:
        stack.append((mid + 1, inR, postL + left_size, postR - 1))
    if left_size > 0:
        stack.append((inL, mid - 1, postL, postL + left_size - 1))

print(*ans)
