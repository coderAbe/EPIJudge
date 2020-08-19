from typing import Optional

from list_node import ListNode
from test_framework import generic_test


# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    if not L:
        return None
    i = 0
    current, last, prev = L, L, L

    while i < k: 
        last = last.next
        i += 1
    
    while last:
        last = last.next
        prev = current
        current = prev.next

    if current == L:
        return current.next

    if current:
        prev.next = current.next
        return L
    

    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
