def maxDepth(self, root):
    if root is None:
        return 0
    
    left_depth = self.maxDepth(root.left)
    right_depth = self.maxDepth(root.right)
    
    return 1 + max(left_depth, right_depth)



class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# In-order Traversal (Left, Root, Right)
def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.value, end=' ')
        in_order_traversal(root.right)

# Pre-order Traversal (Root, Left, Right)
def pre_order_traversal(root):
    if root is not None:
        print(root.value, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

# Post-order Traversal (Left, Right, Root)
def post_order_traversal(root):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=' ')

# Level-order Traversal (Breadth-first)
from collections import deque

def level_order_traversal(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example usage
if __name__ == "__main__":
    # Creating a binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print("In-order traversal:")
    in_order_traversal(root)
    print("\nPre-order traversal:")
    pre_order_traversal(root)
    print("\nPost-order traversal:")
    post_order_traversal(root)
    print("\nLevel-order traversal:")
    level_order_traversal(root)
