class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def zigzagLevelOrder(root: TreeNode):
    if root is None:
        return []
    stack1 = []
    stack2 = []
    zigzag = []
    
    stack1.append(root)
    while stack1 or stack2:
        level_nodes = []
        
        while stack1:
            current = stack1.pop()
            level_nodes.append(current.val)
            if current.left:
                stack2.append(current.left)
            if current.right:
                stack2.append(current.right)
        
        if level_nodes:
            zigzag.append(level_nodes)
            level_nodes = []
            
        while stack2:
            current = stack2.pop()
            level_nodes.append(current.val)
            if current.right:
                stack1.append(current.right)
            if current.left:
                stack1.append(current.left)
                
        '''print("Stack 1: ")
        for i in stack1:
            print(i.val, end = ' ')
        print()       '''
        if level_nodes:
            zigzag.append(level_nodes)
        '''print("Stack 1: ")
        for i in stack1:
            print(i.val, end = ' ')
        print()'''
        
    return zigzag

node = TreeNode(3)
node.left = TreeNode(9)
node.right = TreeNode(20)
node.right.left = TreeNode(15)
node.right.right = TreeNode(7)
print(zigzagLevelOrder(node))

    
