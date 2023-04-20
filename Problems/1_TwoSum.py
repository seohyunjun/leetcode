from util.python2Markdown import Block 

num = 1
subject = 'Two Sum'        
leetcode_addr = 'https://leetcode.com/problems/two-sum/'
info = 'target과 일치하는 리스트 두개의 합'
sub = 'O'
sub_context = 'MyAnswer (O(n * n))'
code = """
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:
        len_nums = len(nums)
        if len_nums==2:
            return [0,1]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target==(nums[i]+nums[j]):        
                    return [i, j]
"""
sec = 3649
memory = 14.9


sub_context2 = "Answer O(n * n) (in의 시간 복잡도 n)"
code2 = """
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:

            for i, n in enumerate(nums):
                complement = target - n
                
                if complement in nums[i+1:]:
                    return [nums.index(n), nums[i+1:].index(complement)+(i+1)] #(i+1) 보정
"""
sec2 = 606
memory2 = 15


sub_context3 = "Answer O(n)"
code3 = """
    class Solution:
        def twoSum(self, nums: List[int], target: int) -> List[int]:

        d = {}
        for i, j in enumerate(nums):
            r = target - j
            if r in d: return [d[r], i]
            d[j] = i
        
        # An Upvote will be encouraging
"""
sec3 = 57
memory3 = 15.2

block = Block()
title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)

subtitle = f'### {sub_context}'
block.titleblock(subtitle)

code1 = f"""
    :::python
    {code}
"""
block.codeblock(code1)

performance_title = f'##### Result : {sec}ms Memory: {memory}mb'
block.titleblock(performance_title)
####################################################
subtitle2 = f'### {sub_context2}'
block.titleblock(subtitle2)

code2_ = f"""
    :::python
    {code2}
"""
block.codeblock(code2_)

performance_title2 = f'##### Result : {sec2}ms Memory: {memory2}mb'
block.titleblock(performance_title2)

####################################################
subtitle3 = f'### {sub_context3}'
block.titleblock(subtitle3)

code3_ = f"""
    :::python
    {code3}
"""
block.codeblock(code3_)

performance_title2 = f'##### Result : {sec3}ms Memory: {memory3}mb'
block.titleblock(performance_title3)


print_result = ''.join(block.result)

with open(f"{num}_{subject}.md",'w') as f:
    f.write(print_result)
    

####### using slicing
