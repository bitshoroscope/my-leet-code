# Definition for singly-linked list.
from typing import Optional

class LinkedList:
  def __init__(self):
    self.head = None

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

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      result = ListNode()
