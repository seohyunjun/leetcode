from util.python2Markdown import Block 
from util.func import getInfo
num = 7
subject = 'Reverse Integer'        
leetcode_addr = 'https://leetcode.com/problems/reverse-integer/description/'
info = 'Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.'
sub = 'Assume the environment does not allow you to store 64-bit integers (signed or unsigned).'
sub_context = 'Answer'
code = """
    class Solution:
        def reverse(self, x: int) -> int:
            if x > 0:
                x = int(str(x)[::-1])

            else:
                x = -1*int(str(x*-1)[::-1])

            if (-2**31 > x) or (x > 2**31 - 1):
                return 0
            else:
                return x

"""
sec = 34
memory = 13.8


content = getInfo(subject)


block = Block()

title_block = f"""## LeetCode-[{num}]({leetcode_addr})

##### {subject} : {info}
##### note : {sub}
"""
block.titleblock(title_block)
block.addcode_block(sub_context, code, sec, memory)
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
