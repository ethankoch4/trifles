'''Stack in Python.
'''


class Stack:
    '''Native Python Class for implementing a Stack.
    '''
    def __init__(self):
        '''Instantiate a Stack with no max capacity.

        __Returns__

        ----
        - (Stack): Instantiated Stack object.
        '''
        self.array = []

    def size(self):
        '''Get the size of the stack as it is currently.

        __Returns__

        ----
        - (int): Number of elements in stack.
        '''
        return len(self.array)

    def empty(self):
        '''Check to see if the Stack contains any elements.

        __Returns__

        ----
        - (bool): True if the Stack contains no elements.
        '''
        return not bool(self.array)

    def get_top(self):
        '''Get the element at the top of the Stack.

        __Returns__

        ----
        - (any): The element at the top of the Stack.
        '''
        return self.array[-1]

    def push(self, data):
        '''Put new element at top of the Stack.

        __Args__

        ----
        - data (any): Data to put as element at top of Stack.
        '''
        self.array.append(data)

    def pop(self):
        '''Remove and return element at top of the Stack.

        __Returns__

        ----
        - (any): Element found at top of the Stack.
        '''
        element = self.array[-1]
        del self.array[-1]
        return element
