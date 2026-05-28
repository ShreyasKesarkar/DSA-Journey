class ListNode():
    def __init__(self,value):
        self.value = value 
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        current = self.head

        while index != 0:
            current = current.next
            index -= 1

        return current.value        

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1


    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1    


    def addAtIndex(self, index: int, val: int) -> None:
        
        if index < 0 or index > self.size:
            return
        elif index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            current = self.head
            while index - 1 != 0:
                current = current.next
                index -= 1
            new_node = ListNode(val)

            new_node.next = current.next
            current.next.prev = new_node
            current.next = new_node
            new_node.prev = current
            self.size  += 1                 
        



    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        elif index == 0:
            current = self.head.next
            if current:
                current.prev = None

            self.head = self.head.next 

            self.size -= 1

            if self.size == 0 :
                self.tail = None

        elif index == self.size - 1:
            current = self.tail.prev

            if current:
                current.next = None
            self.tail = self.tail.prev

            self.size -= 1

            if self.size == 0:
                self.head = None 

        else:
            current = self.head

            while index - 1 != 0:
                current = current.next
                index -= 1
            current.next = current.next.next
            current.next.prev = current

            self.size -= 1 