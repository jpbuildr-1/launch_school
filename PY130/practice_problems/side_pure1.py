'''
What side effects are present in the foo function in the following code?
'''
bar = 42
qux = [1, 2, 3]
baz = 3

def foo(lst):
    value = lst.pop()
    print(f'popped {value} from the list')
    return value + bar + baz

foo(qux)
# lst.pop()
# print(f'popped {value} from the list')
