from list.listNode import ListNode


class LinkedListBasic:
	def __init__(self):
		self.__head = ListNode('dummy', None)
		self.__numItems = 0

	# [알고리즘 5 - 2] 구현: 연결 리스트에 원소 삽입하기(더미 헤드를 두는 대표 버전)
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

	# [알고리즘 5-3] 구현: 연결 리스트의 원소 삭제하기
	def pop(self, i: int):  # i번 노드 삭제. 고정 파라미터
		if (i >= 0 and i <= self.__numItems - 1):
			prev = self.__getNode(i - 1)
			curr = prev.next
			prev.next = curr.next
			retItem = curr.item
			self.__numItems -= 1
			return retItem
		else:
			return None

	# [알고리즘 5 -4] 구현: 연결 리스트의 원소 x 삭제하기 (더미 헤드를 두는 대표 버전)
	def remove(self, x):
		(prev, curr) = self.__findNode(x)
		if curr != None:
			prev.next = curr.next
			self.__numItems -= 1
			return x
		else:
			return None

	# [알고리즘 5 - 5] 구현: 연결 리스트의 i번 원소 알려주기
	def get(self, i: int):
		if self.isEmpty():
			return None
		if (i >= 0 and i <= self.__numItems - 1):
			return self.__getNode(i).item
		else:
			return None

	# [알고리즘 5 -7] 구현: x가 연결 리스트의 몇 번 원소인지 알려주기
	def index(self, x) -> int:
		curr = self.__head.next  # 0번 노드:  더미 헤드 다음 노드
		for index in range(self.__numItems):
			if curr.item == x:
				return index
			else:
				curr = curr.next
		return -2  # 안 쓰는 인덱스

	# [알고리즘 5 -8] 구현: 기타 작업들
	def isEmpty(self) -> bool:
		return self.__numItems == 0

	def size(self) -> int:
		return self.__numItems

	def clear(self):
		self.__head = ListNode("dummy", None)
		self.__numItems = 0

	def count(self, x) -> int:
		cnt = 0
		curr = self.__head.next  # 0번 노드
		while curr != None:
			if curr.item == x:
				cnt += 1
			curr = curr.next
		return cnt

	def extend(self, a):  # 여기서 a는 self와 같은 타입의 리스트
		for index in range(a.size()):
			self.append(a.get(index))

	def copy(self):
		a = LinkedListBasic()
		for index in range(self.__numItems):
			a.append(self.get(index))
		return a

	def reverse(self):
		a = LinkedListBasic()
		for index in range(self.__numItems):
			a.insert(0, self.get(index))
		self.clear()
		for index in range(a.size()):
			self.append(a.get(index))

	def sort(self) -> None:
		a = []
		for index in range(self.__numItems):
			a.append(self.get(index))
		a.sort()
		self.clear()
		for index in range(len(a)):
			self.append(a[index])

	def __findNode(self, x) -> (ListNode, ListNode):
		prev = self.__head  # 더미 헤드
		curr = prev.next  # 0번 노드
		while curr != None:
			if curr.item == x:
				return (prev, curr)
			else:
				prev = curr;
				curr = curr.next
		return (None, None)


	# [알고리즘 5-6] 구현: 연결 리스트의 i번 노드 알려주기
	def __getNode(self, i: int) -> ListNode:
		curr = self.__head  # 더미 헤드, index: -1
		for index in range(i + 1):
			curr = curr.next
		return curr

	def printList(self):
		curr = self.__head.next  # 0번 노드: 더미 헤드 다음 노드
		while curr != None:
			print(curr.item, end=' ')
			curr = curr.next
		print()

####만든 함수들

	def printInterval(self, i: int, j:int):
		if i >= 0 and j <= self.__numItems:
			for a in range(i, j):
				print(self.get(a), end=' ')

		else:
			print("index", i, ": out of bound in insert()")  # 필요 시 에러 처리

	def numItems(self):
		cnt = 0
		curr = self.__head.next  # 0번 노드
		while curr != None:
			cnt += 1
			curr = curr.next
		print(cnt)
		return cnt

	def numItemsrec(self, cnt=0, curr='head'):
		if curr == 'head':
			curr = self.__head
		if curr.next != None:
			cnt += 1
			curr = curr.next
			return self.numItemsrec(cnt, curr)
		else:
			return cnt

	def pop2(self, i: int, k: int):  # i번 노드 삭제. 고정 파라미터
		curr = self.__head.next
		if (i >= 0 and i <= self.__numItems - 1):
			for a in range(i,i+k):
				if curr.next != None:
					prev = self.__getNode(i - 1)
					curr = prev.next
					prev.next = curr.next
					retItem = curr.item
					self.__numItems -= 1
			return retItem
		else:
			return None

	def samelist(self, node1, node2):
		curr1 = node1.next
		curr2 = node2.next
		while curr1.next != None:
			curr1 = curr1.next
		while curr2.next != None:
			curr2 = curr2.next
		print('curr1, curr2', id(curr1), id(curr2))
		if curr1 == curr2:
			return True
		else:
			return False

	def printaddress(self):
		curr = self.__head.next  # 0번 노드: 더미 헤드 다음 노드
		while curr != None:
			print(curr, id(curr), end=' ')
			curr = curr.next
		print()

	def getNodeglob(self, i: int) -> ListNode:
		global curr
		curr = self.__head  # 더미 헤드, index: -1
		for index in range(i + 1):
			curr = curr.next
		return curr

	def lastIndexOf(self,x):
		cnt = self.count(x)
		cnt2 = 0
		curr = self.__head.next  # 0번 노드:  더미 헤드 다음 노드
		for index in range(self.__numItems):
			if curr.item == x:
				cnt2 += 1
			if cnt2 == cnt:
				return index
			else:
				curr = curr.next
		return -2  # 안 쓰는 인덱스
		return idx


# 코드 5-15
