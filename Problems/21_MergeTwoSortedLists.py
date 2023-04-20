from util.python2Markdown import Block 

num = 21
subject = 'Merge Two Sorted Lists'        
leetcode_addr = 'https://leetcode.com/problems/merge-two-sorted-lists/'
info = 'Merge Two lists'
sub = 'recursive'
sub_context = ''
code = """
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            if (not list1) or (list2 and list1.val > list2.val):
                list1, list2 = list2, list1

            if list1:
                list1.next = self.mergeTwoLists(list1.next, list2)
            return list1

"""
sec = 42
memory = 13.8

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
    
