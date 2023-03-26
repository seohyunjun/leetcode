from util.python2Markdown import Block 

num = 92
subject = ' Reverse Linked List II'        
leetcode_addr = 'https://leetcode.com/problems/reverse-linked-list-ii/description/'
info = 'Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.'
sub = '1 <= left <= right <= n'
sub_context = 'Answer'
code = """
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
            
            if not head or left == right:
                return head

            root = start = ListNode(None)
            root.next = head

            for _ in range(left-1):
                start = start.next
            end = start.next

            for _ in range(right-left):
                tmp, start.next, end.next = start.next, end.next, end.next.next
                start.next.next = tmp
            return root.next
"""
sec = 34
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
