class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None


class MyLinkedList:

    
    def __init__(self):
        self.head = Node()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        if not curr:
            return -1
            
        for i in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val:  int) -> None:
        new_node = Node(val)
        if self.head.val is None:
            self.head = new_node
            self.size += 1
            return
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.addAtHead(val)
            return
        new_node = Node(val)
        curr = self.head
        while curr:
            if curr.next is None:
                break
            curr = curr.next
        curr.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        new_node = Node(val)
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        new_node.next = curr.next
        curr.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size - 1:
            return
        if index == 0:
            self.head = self.head.next
            return
        curr = self.head
        for _ in range(index - 1):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1

    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.val)
            curr = curr.next
        print(elements)


my_list = MyLinkedList()
# my_list.addAtIndex(0, 10)
# my_list.addAtIndex(0, 20)
# my_list.addAtIndex(1, 30)
# print(my_list.get(0))

#######################################

# my_list.addAtTail(1)
# print(my_list.get(0))
# my_list.display()
###############################

# my_list.addAtHead(1)
# my_list.addAtTail(3)
# my_list.display()
# my_list.addAtIndex(1, 2)
# my_list.display()
# print(my_list.get(1))
# my_list.deleteAtIndex(1)
# my_list.display()
# my_list.addAtHead(7)
# my_list.addAtHead(2)
# my_list.addAtHead(1)
# my_list.addAtIndex(3, 0)
# my_list.display()
# print(my_list.size)
# my_list.deleteAtIndex(2)
# my_list.display()
# my_list.addAtHead(6)
# my_list.addAtTail(4)
# my_list.display()
# print(my_list.get(4))
# my_list.addAtHead(4)
# my_list.addAtIndex(5, 0)
# my_list.addAtHead(6)
# my_list.display()

#########################################
my_list.addAtHead(1)
my_list.addAtTail(3)
my_list.addAtIndex(1, 2)
my_list.display()
print(f"Element in index 1: {my_list.get(1)}")
my_list.deleteAtIndex(1)
my_list.display()       # after deletion at index 1
print(f"Element in index 1: {my_list.get(1)}")

