'''Singly Linked List in Python.
'''

class SinglyLinkedList:
    '''Native Python Class for implementing a Generic Singly Linked List.
    '''
    def __init__(self):
        '''Instantiate a SinglyLinkedList with None root.

        __Returns__

        ----
        - (SinglyLinkedList): Instantiated SinglyLinkedList object.
        '''
        self.root = None

    def __repr__(self):
        out = ''
        curr = self.root
        while curr is not None:
            out += str(curr.data)
            out += ' -> '
            curr = curr.next
        out += str(curr)
        return out

    def __iter__(self):
        curr = self.root
        while curr is not None:
            yield curr
            curr = curr.next

    def add_front(self, data):
        '''Add new SLLNode to beginning of Singly Linked List.

        __Args__

        ----
        - data (any): Data held within the new node.
        '''
        new_node = SLLNode(data, self.root)
        self.root = new_node

    def get_front(self):
        '''Get the front SLLNode's data from the Singly Linked List.

        __Returns__

        ----
        - (any): The data held within the front node in the list.
        '''
        if self.empty():
            return self.root
        return self.root.data

    def remove_front(self):
        '''Remove front SLLNode from the Singly Linked List.
        '''
        if not self.empty():
            self.root = self.root.next

    def empty(self):
        '''Check to see if the Singly Linked List contains any nodes.

        __Returns__

        ----
        - (bool): True if the root is None.
        '''
        return self.root is None


class SLLNode:
    '''Node to hold generic data for Singly Linked List.
    '''
    def __init__(self, data, next):
        '''Instantiate a SLLNode with specified data and next node.

        __Args__

        ----
        - data (any): data to be held by node.
        - next (SLLNode): next node in the list.

        __Returns__

        ----
        - (SLLNode): Instantiated SLLNode object.
        '''
        self.data = data
        self.next = next

    def __next__(self):
        return self.next

    def __repr__(self):
        return str(self.data)
