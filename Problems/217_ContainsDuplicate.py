from util.python2Markdown import Block 
from util.func import getInfo
num = 217
subject = 'Contains Duplicate'        
leetcode_addr = 'https://leetcode.com/problems/contains-duplicate/'
info = 'Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'
sub = '1 <= nums.length <= 105'
sub_context = 'Answer'
code = """
    class Solution:
        def containsDuplicate(self, nums: List[int]) -> bool:
            if len(nums)==1:
                return False
            nums.sort()
            left = 0
            while left+1 <= len(nums)-1:
                if nums[left]==nums[left+1]:
                    return True
                left += 1
            return False
"""
sec = 634
memory = 27.9

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
