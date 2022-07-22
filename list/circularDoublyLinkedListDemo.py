from circularDoublyLinkedList import *

list = CircularDoublyLinkedList()
list.append(30); list.insert(0, 20)
a = [4, 3, 3, 2, 1]

list.extend(a)
list.reverse()
#list.pop(0)
#print("count(3):", list.count(3))
#print("get(2):", list.get(2))
#print("contains:", list.contains(3))
list.append(3)
list.printList()
list.add(5)
list.printList()
#list.printInterval(0,3)
#print(list.lastIndexOf(3))
#print(list.add(4))
# 코드 5-26