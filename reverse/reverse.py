class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # TO BE COMPLETED
    # returning if there are no nodes in the list
    if self.head is None:
      return

    # instantiating a prev var
    prev = None

    # setting current node to equal the current head
    current = self.head

    while(current is not None):
      # saving the current.next_node var as to not lose it
      next_node = current.next_node

      # then reassigning the current next_node to prev (aka. None the first time)
      current.next_node = prev
      # then assigning prev to the current for the next iteration
      prev = current
      # assigning new current to next_node (this is our iteration as to not loop infinitely)
      current = next_node
      # then also assigning new head (which equals current at this time)
      self.head = prev