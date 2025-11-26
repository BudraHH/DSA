from typing import List, Optional
from binary_tree.BinaryTree import TreeNode, BinaryTree

def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if not inorder and not postorder:
        return None

    root = TreeNode(postorder[-1])
    rootInorderIndex = inorder.index(postorder[-1])
    # print(f"rootInorderIndex: {rootInorderIndex}")
    # print(f"root: {root.val}")
    # print(f"inorder: {inorder}")
    # print(f"postorder: {postorder}")
    left_inorder = inorder[:rootInorderIndex]
    left_postorder = postorder[:len(left_inorder) ]
    # print(f"left_inorder: {left_inorder}")
    # print(f"left_postorder: {left_postorder}")
    right_inorder = inorder[rootInorderIndex + 1:]
    right_postorder = postorder[len(left_postorder) : -1]
    # print(f"right_inorder: {right_inorder}")
    # print(f"right_postorder: {right_postorder}")
    root.left = buildTree(left_inorder, left_postorder)
    root.right = buildTree(right_inorder, right_postorder)
    return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
BinaryTree.printLevelOrder(buildTree(inorder, postorder))