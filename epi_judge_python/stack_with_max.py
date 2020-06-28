from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Stack:
    max_value = []
    stack = [] 

    def empty(self) -> bool:
        return len(self.stack) == 0

    def max(self) -> int:
        if len(self.max_value) > 0:
            return self.max_value[-1]

    def pop(self) -> int:
        if not self.empty():
            removed = self.stack.pop()
            if len(self.max_value) and removed == self.max_value[-1]:
                self.max_value.pop()
            return removed

    def push(self, x: int) -> None:
        if len(self.max_value) == 0:
            self.max_value.append(x)
        elif self.max_value[-1] <= x:
            self.max_value.append(x)
        self.stack.append(x)


def stack_tester(ops):
    try:
        s = Stack()

        for (op, arg) in ops:
            if op == 'Stack':
                s = Stack()
            elif op == 'push':
                s.push(arg)
            elif op == 'pop':
                result = s.pop()
                if result != arg:
                    raise TestFailure('Pop: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'max':
                result = s.max()
                if result != arg:
                    raise TestFailure('Max: expected ' + str(arg) + ', got ' +
                                      str(result))
            elif op == 'empty':
                result = int(s.empty())
                if result != arg:
                    raise TestFailure('Empty: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported stack operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('stack_with_max.py',
                                       'stack_with_max.tsv', stack_tester))
