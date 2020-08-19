from test_framework import generic_test

def add (x,y):
    return x + y

def substract (x,y):
    return y - x

def division (x,y):
    return y // x

def product (x,y):
    return x * y


operation = {
        '+': lambda x,y: x + y,
        '-': lambda x,y: y - x,
        '/': lambda x,y: y // x,
        '*': lambda x,y: x * y,
        }

def evaluate(expression: str) -> int:
    stack = []
    for curr in expression.split(','):
        if curr.isnumeric():
            stack.append(int(curr))
        else:
            if len(stack) > 1:
                x = stack.pop()
                y = stack.pop()
                oper = operation[curr]
                stack.append(oper(x,y))

    return stack.pop() 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
