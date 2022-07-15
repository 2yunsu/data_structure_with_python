from 
class BidirectNode:
    def __init__(self, x, prevNode:'BidirectNode', nextNode:'BidirectNode'):
        self.item = x
        self.prev = prevNode
        self.next = nextNode

class CircularDoublyLinkedList:
    def __init__(self):
        self.__head = BidirectNode
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0

    def index(self, x):
        cnt=0
        for element in self:
            if element ==x:
                return cnt
            cnt += 1
        return -12345

    def contains(x):
        if CircularDoublyLinkedList.index(x) == True:
            return True
        else:
            return False

list=CircularDoublyLinkedList()
list.
