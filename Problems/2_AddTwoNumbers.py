from util.python2Markdown import Block 

num = 2
subject = 'Add Two Numbers'        
leetcode_addr = 'https://leetcode.com/problems/add-two-numbers/'
info = 'Add Two Numbers in Linked List'
sub = 'You may assume the two numbers do not contain any leading zero, except the number 0 itself.'
sub_context = 'myAnswer'
code = """
    #Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
        class Solution:
            def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
                root = head = ListNode(0)

                carry = 0

                while l1 or l2 or carry:
                    sum = 0
                    if l1:
                        sum += l1.val
                        l1 = l1.next
                    if l2:
                        sum += l2.val
                        l2 = l2.next
                    
                    carry, val = divmod(sum+carry, 10)
                    head.next = ListNode(val)
                    head = head.next
                return root.next
"""
sec = 72
memory = 14

block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)

# subtitle = f'### {sub_context}'
# block.titleblock(subtitle)

# code1 = f"""
#     :::python
#     {code}
# """
# block.codeblock(code1)

# performance_title = f'##### Result : {sec}ms Memory: {memory}mb'
# block.titleblock(performance_title)

print_result = ''.join(block.result)

with open(f"markdown/{num}_{subject}.md",'w') as f:
    f.write(print_result)
    

####### using slicing
