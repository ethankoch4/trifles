'''Double Ended Queue in Python.
'''


class DoubleEndedQueue:
    '''Native Python Class for implementing a Double Ended Queue.
    '''
    def __init__(self):
        '''Instantiate a Double Ended Queue with no max capacity.

        __Returns__

        ----
        - (DoubleEndedQueue): Instantiated DoubleEndedQueue object.
        '''
        self.array = []

    def size(self):
        '''Get the size of the Double Ended Queue as it is currently.

        __Returns__

        ----
        - (int): Number of elements in Double Ended Queue.
        '''
        return len(self.array)

    def empty(self):
        '''Check to see if the Double Ended Queue contains any elements.

        __Returns__

        ----
        - (bool): True if the Double Ended Queue contains no elements.
        '''
        return not bool(self.array)

    def push_front(self):
        '''Put new element at front of the Double Ended Queue.

        __Args__

        ----
        - data (any): Data to put as element at front of Double Ended Queue.
        '''
        self.array.insert(0, data)

    def push_back(self):
        '''Put new element at back of the Double Ended Queue.

        __Args__

        ----
        - data (any): Data to put as element at back of Double Ended Queue.
        '''
        self.array.append(data)

    def pop_front(self):
        '''Remove and return element at front of the Double Ended Queue.

        __Returns__

        ----
        - (any): Element found at front of the Double Ended Queue.
        '''
        element = self.array[0]
        del self.array[0]
        return element

    def pop_back(self):
        '''Remove and return element at back of the Double Ended Queue.

        __Returns__

        ----
        - (any): Element found at back of the Double Ended Queue.
        '''
        element = self.array[-1]
        del self.array[-1]
        return element

    def get_front(self):
        '''Get the element at the front of the Double Ended Queue.

        __Returns__

        ----
        - (any): The element at the front of the Double Ended Queue.
        '''
        return self.array[0]

    def get_back(self):
        '''Get the element at the back of the Double Ended Queue.

        __Returns__

        ----
        - (any): The element at the back of the Double Ended Queue.
        '''
        return self.array[-1]
