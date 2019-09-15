'''Place to experiment with different data structures and algorithms.
'''

from . import data_structures


def reverse_vector_with_stack(vector):
    '''Reverses a vector using a stack "in-place".

    __Args__

    ----
    - vector (iterable): Vector to be reversed and returned.

    __Returns__

    ----
    - (iterable): Vector that was input with the elements' order reversed.
    '''
    stack = data_structures.stack.Stack()

    # create stack (LIFO)
    for element in vector:
        stack.push(element)

    # pop of the elements of the Stack (LIFO)
    for idx, element in enumerate(vector):
        vector[idx] = stack.pop()
