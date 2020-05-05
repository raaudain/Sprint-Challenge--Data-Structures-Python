from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        
        # If length is less than capacity
        if self.storage.length < self.capacity:
            # Append item (add_to_tail)
            self.storage.add_to_tail(item)
            # Set current node to head node
            self.current = self.storage.head
        else:
            # If a current node exists
            if self.current.next:
                # Set node value to item
                self.current.value = item
                # Set current node to the next node
                self.current = self.current.next
            else:
                # Set current node value to item
                self.current.value = item
                # Set current node to linked list head
                self.current = self.storage.head
   

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        
        # Declare node variable
        node = self.storage.head

        # TODO: Your code here
        
        # While there is a self.storage.head
        while node:
            # Append node values to array
            list_buffer_contents.append(node.value)
            # Redeclare node as the node.next to move to next node
            node = node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
