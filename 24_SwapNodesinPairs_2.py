from util.python2Markdown import Block 

num = 24
subject = 'swap-nodes-in-pairs_2'        
leetcode_addr = 'https://leetcode.com/problems/swap-nodes-in-pairs/'
info = "Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes"
sub = 'only nodes themselves may be changed.'
sub_context = 'MyAnswer'


code = """
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

            root = prev = ListNode(None)
            prev.next = head
            while head and head.next:
                b = head.next
                head.next = b.next
                b.next = head
                
                prev.next = b

                head = head.next
                prev = prev.next.next
                
            return root.next

"""
sec = 32
memory = 13.9

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
\