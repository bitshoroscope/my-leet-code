# Definition for singly-linked list.
from typing import Optional

class LinkedList:
  def __init__(self):
    self.head = None

  def __init__(self, list):
    self.head = None
    for element in list:
      self.insert(element)

  def insert(self, data):
    newNode = ListNode(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

  def __str__(self):
    result = "["
    node = self.head
    if node != None:
      result += str(node.val)
      node = node.next
      while node.next != None:
        result += ", " + str(node.val)
        node = node.next
    result += ", " + str(node.val)
    result += "]"
    return result

  def __eq__(self, listb):
    a = self.head
    b = listb.head

    while (a != None and b != None):
      if (a.val != b.val):
        return False

      a = a.next
      b = b.next

    return (a == None and b == None)

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      result = LinkedList([1,1,2,3,4,4])
      return result
