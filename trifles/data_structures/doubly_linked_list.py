'''Doubly Linked List in Python.
'''

class DoublyLinkedList:
    '''Native Python Class for implementing a Generic Doubly Linked List.
    '''
    def __init__(self):
        '''Instantiate a DoublyLinkedList with header and trailer.

        __Returns__

        ----
        - (DoublyLinkedList): Instantiated DoublyLinkedList object.
        '''
        self.header = DLLNode(None, None, None)
        self.trailer = DLLNode(None, None, None)
        self.header.next = self.trailer
        self.trailer.prev = self.header

    def __repr__(self):
        out = 'header'
        curr = self.header.next
        while curr != self.trailer:
            out += ' <-> '
            out += str(curr.data)
            curr = curr.next
        out += ' <-> '
        out += 'trailer'
        return out

    def __iter__(self):
        curr = self.header.next
        while curr != self.trailer:
            yield curr
            curr = curr.next

    def reverse(self):
        '''Reverse the current Doubly Linked List in-place.
        '''
        new_list = DoublyLinkedList()

        while not self.empty():
            curr_data = self.get_front()
            self.remove_front()
            new_list.add_front(curr_data)

        while not new_list.empty():
            curr_data = new_list.get_front()
            new_list.remove_front()
            self.add_back(curr_data)

    def add(self, node, data):
        '''Add new DLLNode to before the given node.

        __Args__

        ----
        - node (DLLNode): Node which the new node should be inserted before.
        - data (any): Data held within the new node.
        '''
        new_node = DLLNode(data, node.prev, node)
        node.prev.next = new_node
        node.prev = new_node

    def add_front(self, data):
        '''Add new DLLNode to beginning of Doubly Linked List.

        __Args__

        ----
        - data (any): Data held within the new node.
        '''
        self.add(self.header.next, data)

    def add_back(self, data):
        '''Add new DLLNode to end of Doubly Linked List.

        __Args__

        ----
        - data (any): Data held within the new node.
        '''
        self.add(self.trailer, data)

    def get_front(self):
        '''Get the front DLLNode's data from the Doubly Linked List.

        __Returns__

        ----
        - (any): The data held within the first node in the list.
        '''
        if not self.empty():
            return self.header.next.data

    def remove(self, node):
        '''Remove front DLLNode from the Doubly Linked List.

        __Args__

        ----
        - node (DLLNode): Node which should be removed.
        '''
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del node

    def remove_front(self):
        '''Remove front DLLNode from the Doubly Linked List.
        '''
        if not self.empty():
            self.remove(self.header.next)

    def remove_back(self):
        '''Remove back DLLNode from the Doubly Linked List.
        '''
        if not self.empty():
            self.remove(self.trailer.prev)

    def empty(self):
        '''Check to see if the Doubly Linked List contains any nodes.

        __Returns__

        ----
        - (bool): False if the any node except the header and trailer exist.
        '''
        return bool(self.header.next == self.trailer)


class DLLNode:
    '''Node to hold generic data for Doubly Linked List.
    '''
    def __init__(self, data, prev, next):
        '''Instantiate a DLLNode with specified data and next node.

        __Args__

        ----
        - data (any): data to be held by node.
        - prev (DLLNode): previous node in the list.
        - next (DLLNode): next node in the list.

        __Returns__

        ----
        - (DLLNode): Instantiated DLLNode object.
        '''
        self.data = data
        self.prev = prev
        self.next = next

    def __next__(self):
        return self.next

    def __repr__(self):
        return str(self.data)
