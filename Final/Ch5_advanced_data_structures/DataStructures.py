# https://www.youtube.com/watch?v=lVFnq4zbs-g&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=1
from typing import Optional, Union


class Stack(object):
    """Stack
    :push      -> add item to the top of the stack
    :pop       -> remove and return the top item of the stack
    :peek      -> return the top element of the stack
    :is_empty  -> returns True if the stack is empty
    :get_stack -> returns the entire stack
    """

    def __init__(self):
        self.__items = []

    def push(self, item):
        """Adds the item to the top of the stack."""
        self.__items.append(item)

    def pop(self):
        """Removes and returns the top item from the stack."""
        return self.__items.pop()

    def is_empty(self):
        return self.__items == []

    def peek(self):
        return None if self.is_empty() else self.__items[-1]
        # if self.is_empty():
        #     return None:
        # else:
        #     return self.__items[-1]

    def get_stack(self):
        return self.__items


class Node(object):
    """Node class for linked lists."""

    def __init__(self, data):
        self.data = data
        self.next = None


class SLinkedList(object):
    """Singly Linked List
    LLs are made up of nodes, each node has a data and a pointer
    :value -> return the value that the node stores
    :next  -> return the next node
    """

    def __init__(self):
        self.head = None

    def print_list(self):
        """Print the value(s) of the linked list"""
        cur_node = self.head
        while cur_node:  # is not None
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data) -> None:
        """Add a new node to the end of the linked list"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return None

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data) -> None:
        """Add a new node to the beginning of the linked list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return None
        
    def length(self) -> int:
        """Return the length of the linked list"""
        cur_node = self.head
        if cur_node is None:
            return 0
        else:
            count = 1
            while cur_node.next is not None:
                cur_node = cur_node.next
                count += 1
            return count

    def insert_node(self, new_node, index: int) -> None:
        """Insert node after a given index"""
        # exit if index is out of range
        if index > self.length() - 1:
            # return None
            raise IndexError("Index out of range")
        # create Node object if data was passed
        if not isinstance(new_node, Node):
            new_node = Node(new_node)
        # locate correct node
        cur_node = self.head
        cur_index = 0
        while index > cur_index:
            cur_node = cur_node.next
            cur_index += 1
        # insert Node object
        temp_node = cur_node.next
        cur_node.next = new_node
        new_node.next = temp_node
        return None

    def get_node(self, index):
        """return a node at the given index"""
        cur_index = 0
        cur_node = self.head
        while index > cur_index:
            cur_node = cur_node.next
            cur_index += 1
        return cur_node

    # def pop_node(self, index: int) -> Optional[Node]:
    #


def main():
    ll = SLinkedList()
    ll.append("A")
    ll.append("B")
    ll.append("C")
    ll.append("D")
    print("---")
    ll.print_list()
    print(ll.get_node(2).data)

    # s1 = Stack()
    # print(s1.is_empty())
    # s1.push("A")
    # s1.push("B")
    # s1.push("C")
    # s1.push("D")
    # print(s1.get_stack())
    # print(s1.peek())


if __name__ == "__main__":
    main()
