from typing import List


class ListNode: 
    # Function to initialise the node object
    def __init__(self, val=0, next=None):
        self.val = val  # Assign data
        self.next = next  # Initialize next as null
  
  
# Linked List class contains a Node object
class LinkedList:
  
    # Function to initialize head
    def __init__(self):
        self.head = None
  
    # This function prints contents of linked list
    # starting from head
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val)
            temp = temp.next
            
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)
        return reverse(head)
rev = reverse(head)

revlink = LinkedList
revlink.head = rev
revlink.printList

l1 = ListNode(val=1, next=ListNode(val=2,next=ListNode(3)))
l2 = ListNode(val=9, next=ListNode(val=1,next=ListNode(9)))
head = ListNode()
p = []
i=0
while l1 or l2:
    p.append((l1.val + l2.val)*10**i)
       
    l1 = l1.next
    l2 = l2.next
    i+=1 
    
sum_p = sum(p)

i=0
while sum_p < 10:
    

    new_node = ListNode((sum_p)//(10**i))
    head.next = new_node
    head=head.next
    
    
    l3 = l3.next
    i+=1 
head.val
head.next

l3.val
l3.next.val
l3.next.next.val
l3.next.next.next.val
node = head
prev = None