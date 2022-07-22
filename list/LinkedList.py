from list.listNode import ListNode

class LinkedList:
    def __init__(self):
        self.__head = ListNode('dummy', None)
        self.__tail = self.__head
        self.__numItems = 0
"""
    def insert(self, i: int, newItem):
        if i >= 0 and i <= self.__numItems:
            prev = self.__getNode(i - 1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            self.__numItems += 1
        else:
            print("index", i, ": out of bound in insert()")  # 필요 시 에러 처리

    def append(self, newItem):
        prev = self.__getNode(self.__numItems - 1)
        newNode = ListNode(newItem, prev.next)
        prev.next = newNode
        self.__numItems += 1
"""

    def numItems(self):
        cnt = 0
        curr = self.__head.next  # 0번 노드
        while curr != None:
            cnt += 1
            curr = curr.next
        print(cnt)
        return cnt

    def numItemsrec(self):
        cnt = 0
        curr = self.__head.next
        if self.__head.next != None:
            return cnt
        else:
            return cnt+numItems()