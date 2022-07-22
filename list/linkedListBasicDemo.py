from linkedListBasic import *

list = LinkedListBasic()
list.append(30); list.insert(0, 20)
a = LinkedListBasic()
a.append(4); a.append(3); a.append(3); a.append(2); a.append(1)
list.extend(a)

list2 = LinkedListBasic()
list2.append(30); list2.insert(0, 20)
list2.extend(a)

#list.reverse()
#list.pop(0)
#print("count(3):", list.count(3))
#print("get(2):", list.get(2))
#print("printInterval(0,3):", print(list.printInterval(0,3)))
# list.append(3)
list.printList()
list.printaddress()
list2.printList()
res = list.samelist(list._LinkedListBasic__head.next, list._LinkedListBasic__head.next.next)
print(res)

#node1=list.getNodeglob(2)
#node2=list2.getNodeglob(2)
#print(list.samelist(node1,node2))

#list.printInterval(0,3)
#list.pop2(4,101012)

print(list.lastIndexOf(3))
# 코드 5-16