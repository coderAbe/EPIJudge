from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test



def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:
    ino_dict = {}

    for x in range(len(inorder)):
        curr = inorder[x]
        ino_dict[curr] = x 

    def recursive_helper(root, pre, ino):
        rootNode = BinaryTreeNode(root)

        pivot = ino_dict[root]
        left_of_root = ino[:pivot]
        right_of_root = ino[pivot + 1:]

        left = []
        right = []

        # AVOID THIS
        for x in pre:
            if x in left_of_root:
                left.append(x)
            else:
                right.append(x)

        if left:
            rootNode.left = recursive_helper(left[0], left[1:], ino)
        if right:
            rootNode.right = recursive_helper(right[0], right[1:], ino)

        return rootNode

    if not preorder or not inorder: 
        return None
    result = recursive_helper(preorder[0], preorder[1:], inorder)
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_from_preorder_inorder.py',
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))
