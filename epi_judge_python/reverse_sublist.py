from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    result = sub_head = ListNode(0, L)

    for i in range(0, start - 1):
        sub_head = sub_head.next

    iter_n = sub_head.next

    for _ in range(0, finish - start):
        temp = iter_n.next
        iter_n.next = temp.next
        temp.next = sub_head.next 
        sub_head.next = temp

    return result.next

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
