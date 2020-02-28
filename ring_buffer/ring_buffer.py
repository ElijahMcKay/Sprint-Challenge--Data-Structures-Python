from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # always going to set the "current" var to be the oldest node (the one to be removed)

        # check to see if length is still less than capacity
        if self.storage.length < self.capacity:
            self.storage.add_to_head(item)
            self.current = self.storage.tail

        
        elif self.current is self.storage.tail:
            self.storage.remove_from_tail()
            self.storage.add_to_tail(item)
            self.current = self.current.prev
        elif self.current is self.storage.head:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.tail
        else:
            self.current.insert_after(item)
            self.current.delete()
            self.current = self.current.prev

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.storage.head
        while self.current:
            list_buffer_contents.insert(0, current_node.value)
            if not current_node.next:
                break
            else:
                current_node = current_node.next

        return list_buffer_contents


# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass