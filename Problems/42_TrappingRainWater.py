from util.python2Markdown import Block 

num = 42
subject = 'Trapping Rain Water'        
leetcode_addr = 'https://leetcode.com/problems/trapping-rain-water/'
info = 'Trapping rain water. find volume'
sub = 'Tip: swap'
sub_context = 'Answer'
code = """
    class Solution:
        def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

"""
sec = 126
memory = 16

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

with open(f"{num}_{subject}.md",'w') as f:
    f.write(print_result)
    

####### using slicing
