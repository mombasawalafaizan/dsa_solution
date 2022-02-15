def inorder(a, v, n, idx):
    if idx >= n:
        return
    inorder(a, v, n, 2*idx+1)
    v.append(a[idx])
    inorder(a, v, n, 2*idx+2)

def minSwaps(v):
    arrpos = [*enumerate(v)]
    swaps = 0
    arrpos.sort(key=lambda x:x[1])
    for i in range(len(v)):
        # If element is in its correct position
        if i == arrpos[i][0]:
            continue
        # Swap the element with its desired value
        else:
            idx = arrpos[i][0]
            arrpos[i], arrpos[idx] = arrpos[idx], arrpos[i]
        # Until correct element is postioned at its place, repeat so decrement
        # i to repeat the same step
        if i != arrpos[i][0]:
            i -= 1
        swaps += 1
        
    return swaps


# The idea is to use the fact that inorder traversal of Binary Search Tree is in increasing order of their value.
# So, find the inorder traversal of the Binary Tree and store it in the array and try to sort the array. 
# The minimum number of swap required to get the array sorted will be the answer.
if __name__ == "__main__":
    a = [5, 6, 7, 8, 9, 10, 11 ]
    n = len(a)
    v = []
    # a is the original given binary tree
    # v contains the inorder traversal, after this function
    inorder(a, v, n, 0)
    # Count the minimum swaps to sort the inorder traversal
    print(minSwaps(v))