from util.python2Markdown import Block 

num = 206
subject = 'Reverse Linked List'        
leetcode_addr = 'https://leetcode.com/problems/reverse-linked-list/'
info = 'Reverse Linked List'
sub = '연결 리스트 역순으로 정렬'
sub_context = ''
code = """
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            def reverse(node: ListNode, prev: ListNode = None):
                if not node:
                    return prev
                next, node.next = node.next, prev
                return reverse(next, node)
            return reverse(head)
"""


sec = 36
memory = 20.4

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
