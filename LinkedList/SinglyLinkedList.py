class ListNode():
    def __init__(self,value):
        self.value = value
        self.next = None
        
class LinkedList():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def get(self,index:int) ->int:
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head
        
        while index != 0:
            current = current.next 
            index -= 1
        
        return current       
        
    def addAtHead(self,value:int)-> None:
        newNode = ListNode(value)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        
        self.size += 1
        
    def addAtTail(self,value:int)-> None:
        newNode = ListNode(value)
        
        if self.head is None:
            self.head = newNode
            self.tail = newNode 
        else:
            self.tail.next = newNode
            self.tail = newNode 
        self.size += 1
                 
            
    def addAtIndex(self, index: int, value: int) -> None:
        if index < 0 or index > self.size:
            return   
        elif  index == 0:
            self.addAtHead(value)
        elif index == self.size:
            self.addAtTail(value)
        else:
           current = self.head
           
                
                    