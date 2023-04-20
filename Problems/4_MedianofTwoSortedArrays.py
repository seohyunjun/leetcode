from util.python2Markdown import Block 
from util.func import getInfo
num = 4
subject = 'Median of Two Sorted Arrays'        
leetcode_addr = 'https://leetcode.com/problems/median-of-two-sorted-arrays/description/'
info = 'Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.'
sub = 'The overall run time complexity should be O(log (m+n)).'
sub_context = 'Answer'
code = """
    class Solution:
        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            p = nums1 + nums2
            p.sort()
            if len(p)%2!=0:
                median = p[len(p)//2]    
            else:
                median = (p[len(p)//2]+p[len(p)//2-1])/2
            return median
"""
sec = 93
memory = 14


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
