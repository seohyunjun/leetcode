from util.python2Markdown import Block 
from util.func import getInfo
num = 238
subject = 'Product of Array Except Self'        
leetcode_addr = 'leetcode'
info = 'Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].'
sub = 'Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)'
sub_context = 'Answer'
code = """
    class Solution:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            out = []
            p = 1
            for i in range(0, len(nums)):
                out.append(p)
                p = p*nums[i]
                
            p = 1
            for i in range(len(nums)-1, 0-1, -1):
                out[i] = out[i]*p
                p = p * nums[i]
            return out

"""
sec = 221
memory = 21.2

# sub_context2 = ''
# code2 = """"""
# sec2 = 0
# memory2 = 0

content = getInfo(subject,code)


block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)
#block.addcode_block(sub_context2, code2, sec2, memory2)
block.result.append(f"\n {content}")

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
