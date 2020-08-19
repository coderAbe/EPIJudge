from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def helper_recur (nodeLeft, nodeRight): 
    if not nodeLeft and not nodeRight:
        return True
    if (not nodeLeft and nodeRight) or (not nodeRight and nodeLeft):
        return False
    if nodeLeft.data != nodeRight.data:
        return False
    return helper_recur(nodeLeft.right, nodeRight.left) and helper_recur(nodeLeft.left, nodeRight.right)


def is_symmetric(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True
    return helper_recur(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
