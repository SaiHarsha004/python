class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    # Helper function to print the list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Create a linked list: 1 -> 2 -> 3 -> 4 -> None
linked_list = LinkedList()
linked_list.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
linked_list.head.next = second
second.next = third
third.next = fourth

print("Original list:")
linked_list.print_list()

linked_list.reverse_iterative()

print("Reversed list:")
linked_list.print_list()
