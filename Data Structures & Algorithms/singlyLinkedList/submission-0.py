class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None

class LinkedList:
    
    def __init__(self):
        self.head=None
        self.tail=None
    
    def get(self, index: int) -> int:
        i=0
        current=self.head
        while i<index and current:
            current=current.next
            i+=1
        if current:
            return current.val
        return -1

    def insertHead(self, val: int) -> None:
        newNode=ListNode(val)
        newNode.next=self.head
        self.head=newNode
        if not self.tail:
            self.tail=newNode

    def insertTail(self, val: int) -> None:
        newnode=ListNode(val)
        if self.tail:
            self.tail.next=newnode
            self.tail=newnode
        else:
            self.head=newnode
            self.tail=newnode

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            if self.head == self.tail:
                self.tail = None
            self.head = self.head.next
            return True
        
        i=0
        current=self.head
        while i < index - 1 and current:
            current=current.next
            i+=1
        
        if current and current.next:
            if current.next == self.tail:
                self.tail = current
            current.next = current.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        current=self.head
        arr=[]
        while current:
            arr.append(current.val)
            current=current.next

        return arr