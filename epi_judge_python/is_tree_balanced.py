from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

def get_height_balance(tree, height = 0):
    if not tree:
        return [-1, True] 

    left = get_height_balance(tree.left)

    if not left[1]:
        return [-1, False]

    right = get_height_balance(tree.right)

    if not right[1]:
        return [-1, False]

    diff = abs(left[0] - right[0])

    if diff > 1:
        return [-1, False]

    height = max(left[0], right[0]) + 1

    return [height, True]





def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    return get_height_balance(tree)[1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
