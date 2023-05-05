from util.python2Markdown import Block 
from util.func import getInfo
num = 48
subject = 'Rotate Image'        
leetcode_addr = 'https://leetcode.com/problems/rotate-image/description/'
info = 'You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).'
sub = 'You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.'
sub_context = 'Answer'
code = """
    class Solution:
        def rotate(self, matrix: List[List[int]]) -> None:
            if len(matrix[0])==1:
                return None
            
            
            max_length = len(matrix[0])
            
            matrix = collections.deque(matrix)
            
            for i in range(max_length):
                for j in range(max_length):
                    matrix[j].append(matrix[max_length-i-1].pop(0))
"""
sec = 43
memory = 16.3

# sub_context2 = ''
# code2 = """"""
# sec2 = 0
# memory2 = 0

content = getInfo(subject)


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
