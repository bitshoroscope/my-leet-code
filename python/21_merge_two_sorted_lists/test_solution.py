from solution import Solution as sol
from solution import LinkedList as LinkedList

def test_merge():
  linkedList = LinkedList()
  linkedList.insert(1)
  linkedList.insert(2)
  linkedList.insert(3)
  print(linkedList)

def test_creation_from_list():
  list = [1,2,3]
  linkedList = LinkedList(list)
  print(linkedList)

def test_merge_two_lists():
  list1 = [1,2,4]
  list2 = [1,3,4]
  result = [1,1,2,3,4,4]
  linkedList1 = LinkedList(list1)
  linkedList2 = LinkedList(list2)
  linkedListResult = LinkedList(result)
  res = sol.mergeTwoLists(sol,linkedList1,linkedList2)
  assert res == linkedListResult


