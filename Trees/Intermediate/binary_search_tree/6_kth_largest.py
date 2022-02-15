# Traverse in reverse inorder fashion
def kthLargestUtil(root, k, ans):
    if not root:
        return
    kthLargestUtil(root.right, k, ans)
    if k[0] == 1:
        if not ans:
            ans.append(root.data)
        return 
    k[0] -= 1
    kthLargestUtil(root.left, k, ans)

def kthLargest(root, k):
    ans = []
    kthLargestUtil(root, [k], ans)
    return ans[0]