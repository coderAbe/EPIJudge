from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
import math

def inside_limit(node, min_lim, max_lim):
    if not node:
        return True

    if node.data < min_lim or node.data > max_lim:
        return False

    return inside_limit(node.left, min_lim, node.data)  and  inside_limit(node.right, node.data, max_lim)


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True 

    return inside_limit(tree.left, -math.inf, tree.data) and inside_limit(tree.right, tree.data, math.inf)




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
