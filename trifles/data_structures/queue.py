'''Queue in Python.
'''


class Queue:
    '''Native Python Class for implementing a Queue.
    '''
    def __init__(self):
        '''Instantiate a Queue with no max capacity.

        __Returns__

        ----
        - (Queue): Instantiated Queue object.
        '''
        self.array = []

    def push(self, data):
        '''Put new element at back of the Queue.

        __Args__

        ----
        - data (any): Data to put as element at back of Queue.
        '''
        self.array.append(data)

    def pop(self):
        '''Remove and return element at front of the Queue.

        __Returns__

        ----
        - (any): Element found at front of the Queue.
        '''
        element = self.array[0]
        del self.array[0]
        return element

    def get_front(self):
        '''Get the element at the front of the Queue.

        __Returns__

        ----
        - (any): The element at the front of the Queue.
        '''
        return self.array[0]

    def get_back(self):
        '''Get the element at the back of the Queue.

        __Returns__

        ----
        - (any): The element at the back of the Queue.
        '''
        return self.array[-1]

    def size(self):
        '''Get the size of the Queue as it is currently.

        __Returns__

        ----
        - (int): Number of elements in Queue.
        '''
        return len(self.array)

    def empty(self):
        '''Check to see if the Queue contains any elements.

        __Returns__

        ----
        - (bool): True if the Queue contains no elements.
        '''
        return not bool(self.array)
