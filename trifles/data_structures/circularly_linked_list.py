'''Circularly Linked List in Python.
'''


class CircularlyLinkedList:
    '''Native Python Class for implementing a Generic Circularly Linked List.
    '''
    def __init__(self):
        '''Instantiate a CircularlyLinkedList with None cursor.

        __Returns__

        ----
        - (CircularlyLinkedList): Instantiated CircularlyLinkedList object.
        '''
        self.cursor = None

    def __repr__(self):
        out = ''
        if not self.empty():
            first = self.cursor
            out += str(first.data)
            out += ' -> '
            curr = first.next
            while curr != first:
                out += str(curr.data)
                out += ' -> '
                curr = curr.next
            out += '...repeat...'
        return out

    def __iter__(self):
        first = self.cursor
        yield first
        if not self.empty():
            curr = first.next
            while curr != first:
                yield curr
                curr = curr.next

    def get_back(self):
        '''Get data contained in node behind cursor.

        __Returns__

        ----
        - (any): Data contained in node behind cursor.
        '''
        if not self.empty():
            return self.cursor.data

    def get_front(self):
        '''Get data contained in node in front of cursor.

        __Returns__

        ----
        - (any): Data contained in node in front of cursor.
        '''
        if not self.empty():
            next_node = self.cursor.next
            if next_node is not None:
                return next_node.data

    def advance(self):
        '''Move cursor forward one node.
        '''
        if not self.empty():
            self.cursor = self.cursor.next

    def add(self, data):
        '''Instert a new node with given data after the cursor.

        __Args__

        ----
        - data (any): Data held within the new node.
        '''
        new_node = CLLNode(data, None)
        if self.empty():
            new_node.next = new_node
            self.cursor = new_node
        else:
            new_node.next = self.cursor.next
            self.cursort.next = new_node

    def remove(self):
        '''Remove node in front of cursor.
        '''
        old = self.cursor.next
        if old == self.cursor:
            self.cursor = None
        else:
            self.cursor.next = old.next
        del old

    def empty(self):
        '''Check to see if the Circularly Linked List contains any nodes.

        __Returns__

        ----
        - (bool): True if the cursor is not None.
        '''
        return self.cursor is None


class CLLNode:
    '''Node to hold generic data for Circularly Linked List.
    '''
    def __init__(self, data, next):
        '''Instantiate a CLLNode with specified data and next node.

        __Args__

        ----
        - data (any): data to be held by node.
        - next (CLLNode): next node in the list.

        __Returns__

        ----
        - (CLLNode): Instantiated CLLNode object.
        '''
        self.data = data
        self.next = next

    def __next__(self):
        return self.next

    def __repr__(self):
        return str(self.data)
