from util.python2Markdown import Block 
from util.func import getInfo
num = 23
subject = 'Merge k Sorted Lists'        
leetcode_addr = 'https://leetcode.com/problems/merge-k-sorted-lists/description/'
info = 'You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.'
sub = 'Merge all the linked-lists into one sorted linked-list and return it.'
sub_context = 'MyAnswer'
code = """
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            root = result = ListNode(None)
            heap = []

            for i in range(len(lists)):
                if lists[i]:
                    heapq.heappush(heap, (lists[i].val, i, lists[i]))

            while heap:

                node = heapq.heappop(heap)
                idx = node[1]
                result.next = node[2]
                result = result.next
                if result.next:
                    heapq.heappush(heap, (result.next.val, idx, result.next))
            return root.next
"""
sec = 97
memory = 17.9


content = getInfo(subject)


block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)
block.result.append(content)

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
